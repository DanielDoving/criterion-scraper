import requests
from Config import Config


class Scraper:
    @staticmethod
    def fetch():
        response = requests.get(Config.CRITERION_URL)
        if response.status_code != 200:
            raise Exception(
                'GET {} failed (Status: {}).'.format(Config.CRITERION_URL, response.status_code)
            )
        return response.content
