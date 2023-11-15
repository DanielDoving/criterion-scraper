from bs4 import BeautifulSoup, PageElement

import json
from Config import Config
from classes.CriterionSpine import CriterionSpine
from classes.Scraper import Scraper
from classes.Formatters.FormatterFactory import FormatterFactory
from classes.FileWriter import FileWriter


class Parser:
    @staticmethod
    def load():
        file = open(Config.OUTPUT_FILE, mode="r")
        data = file.read()
        file.close()
        data = json.loads(data)
        spines = list()
        for spine in data:
            spines.append(CriterionSpine(**spine))
        return spines

    @staticmethod
    def parse_response(content: str):
        soup = BeautifulSoup(content, 'html.parser')
        spines = Parser.load()
        for spine in soup.find_all("tr", class_="gridFilm"):
            spine_no = spine.find(class_="g-spine").text.strip()
            if not spine_no:
                continue
            if any(x.spineNo == spine_no for x in spines):
                print(spine_no + " already exist")
                continue
            spines.append(Parser.parse_spine(spine))
            content = FormatterFactory.getInstance().format(spines)
            FileWriter.write(content)
        return spines

    @staticmethod
    def parse_spine(spine: PageElement):
        spine_no = spine.find(class_="g-spine").text.strip()
        title = spine.find(class_="g-title").text.strip()
        director = spine.find(class_="g-director").text.strip()
        country = spine.find(class_="g-country").text.strip().strip(',')
        year = spine.find(class_="g-year").text.strip()

        cover = spine.find(class_="g-img")
        cover = cover.find('img')['src']
        cover = cover.replace('_thumbnail', '_large')
        cover = cover.replace('_small', '_large')

        url = spine['data-href']
        print('Get deets for ' + title)

        deets = Scraper.fetch_details(url)
        deets_parser = BeautifulSoup(deets, 'html.parser')

        description = deets_parser.find("div", class_="product-summary")
        if description:
            description = description.text.strip(' \t\n\r')
        else:
            description = ""

        runtime = deets_parser.find("meta", {"itemprop": "duration"})
        if runtime is not None:
            runtime = runtime.parent.text.strip()
        else:
            runtime = "N/A"

        language = deets_parser.find("li", {"itemprop": "inLanguage"})
        if language is not None:
            language = language.text.strip()

        return CriterionSpine(
            spine_no if spine_no else "N/A",
            title,
            director,
            country,
            year,
            cover,
            url,
            description,
            runtime,
            language
        )
