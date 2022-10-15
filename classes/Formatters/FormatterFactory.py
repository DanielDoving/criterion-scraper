from classes.Formatters import FormatterInterface
from classes.Formatters.JsonFormatter import JsonFormatter

from Config import Config


class FormatterFactory:
    @staticmethod
    def getInstance() -> FormatterInterface:
        if Config.OUTPUT_FORMAT == 'json':
            return JsonFormatter()
        # -- Add more Formatters here --
        else:
            raise Exception('Output Format [i]"{}"[/i] is invalid!'.format(Config.OUTPUT_FORMAT))
