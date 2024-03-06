from abc import ABC, abstractmethod


class UseCaseBase(ABC):

    @abstractmethod
    def run(self, data):
        pass
