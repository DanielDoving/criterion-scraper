from bs4 import BeautifulSoup, PageElement

from classes.CriterionSpine import CriterionSpine


class Parser:
    @staticmethod
    def parse_response(content: str):
        soup = BeautifulSoup(content, 'html.parser')
        spines = list()
        for spine in soup.find_all("tr", class_="gridFilm"):
            spines.append(Parser.parse_spine(spine))
        return spines

    @staticmethod
    def parse_spine(spine: PageElement):
        spine_no = spine.find(class_="g-spine").text.strip()
        title = spine.find(class_="g-title").text.strip()
        director = spine.find(class_="g-director").text.strip()
        country = spine.find(class_="g-country").text.strip()
        year = spine.find(class_="g-year").text.strip()
        return CriterionSpine(
            spine_no if spine_no else "N/A",
            title,
            director,
            country,
            year
        )
