import requests
from Config import Config


class Scraper:
    @staticmethod
    def fetch():
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(Config.CRITERION_URL, headers=headers)
        if response.status_code != 200:
            raise Exception(
                'GET {} failed (Status: {}).'.format(Config.CRITERION_URL, response.status_code)
            )
        return response.content

    @staticmethod
    def fetch_details(url: str):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(
                'GET {} failed (Status: {}).'.format(url, response.status_code)
            )
        return response.content
