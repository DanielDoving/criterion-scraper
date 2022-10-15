import abc
from classes.CriterionSpine import CriterionSpine


class FormatterInterface(abc.ABC):
    @abc.abstractmethod
    def format(spines: set[CriterionSpine]) -> str:
        pass
