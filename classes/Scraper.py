import requests
from Config import Config


class Scraper:
    @staticmethod
    def make_call(url: str):
        # spoof user agent to chrome. Otherwise requests result in HTTP 403
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(
                'GET {} failed (Status: {}).'.format(url, response.status_code)
            )
        return response.content

