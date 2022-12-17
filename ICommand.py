from abc import ABC, abstractmethod


class ICommand(ABC):

    def __init__(self, player):
        self.boy = player

    @abstractmethod
    def execute(self):
        pass
