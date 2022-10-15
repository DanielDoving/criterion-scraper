import json
from classes.Formatters.FormatterInterface import FormatterInterface
from classes.CriterionSpine import CriterionSpine


class JsonFormatter(FormatterInterface):
    @staticmethod
    def format(spines: set[CriterionSpine]) -> str:
        spines = map(lambda e: e.__dict__, spines)
        return json.dumps(list(spines), indent=4)
