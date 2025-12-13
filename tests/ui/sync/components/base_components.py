from abc import ABC, abstractmethod


class BaseComponent(ABC):
    @abstractmethod
    def is_components_present(self) -> bool:
        pass
