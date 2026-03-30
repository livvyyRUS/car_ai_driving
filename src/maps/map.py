from abc import ABC, abstractmethod
from src.objects.wall import Wall

class Map(ABC):
    walls: list[Wall]
    car_pos_x: int
    car_pos_y: int
    reward_lines: list[Wall]
    
    @abstractmethod
    def load(self):
        ...