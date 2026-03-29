from abc import ABC, abstractmethod

class Object(ABC):
    @abstractmethod
    def update(self, dt):
        pass