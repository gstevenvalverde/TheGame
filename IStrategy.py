from abc import ABC, abstractmethod


class IStrategy(ABC):

    @abstractmethod
    def execute(self, x, y, rect):
        pass
