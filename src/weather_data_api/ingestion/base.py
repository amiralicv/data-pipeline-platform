from abc import ABC, abstractmethod


class Source(ABC):
    name: str

    @abstractmethod
    def fetch(self) -> dict:
        pass
