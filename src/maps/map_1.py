from .map import Map
from src.objects.wall import Wall
from pyglet.graphics import Batch

class Map1(Map):
    def __init__(self, batch: Batch) -> None:
        self.car_pos_x = 130
        self.car_pos_y = 230
        # Все стены задаются координатами (x1, y1, x2, y2)
        self.walls = [
            Wall(batch, 91, 96, 96, 308),
            Wall(batch, 96, 308, 151, 469),
            Wall(batch, 151, 469, 92, 594),
            Wall(batch, 92, 594, 148, 690),
            Wall(batch, 148, 690, 336, 714),
            Wall(batch, 336, 714, 583, 670),
            Wall(batch, 583, 670, 690, 720),
            Wall(batch, 690, 720, 1070, 680),
            Wall(batch, 1070, 680, 860, 320),
            Wall(batch, 860, 320, 430, 440),
            Wall(batch, 430, 440, 400, 300),
            Wall(batch, 400, 300, 1170, 144),
            Wall(batch, 1170, 144, 1026, 16),
            Wall(batch, 1026, 16, 260, 39),
            Wall(batch, 260, 39, 91, 96),
            
            Wall(batch, 180, 170, 190, 300),
            Wall(batch, 190, 300, 245, 481),
            Wall(batch, 245, 481, 187, 592),
            Wall(batch, 187, 592, 900, 600),
            Wall(batch, 900, 600, 780, 460),
            Wall(batch, 780, 460, 591, 533),
            Wall(batch, 591, 533, 350, 540),
            Wall(batch, 350, 540, 270, 300),
            Wall(batch, 270, 300, 350, 180),
            Wall(batch, 350, 180, 940, 100),
            Wall(batch, 940, 100, 290, 120),
            Wall(batch, 290, 120, 180, 170)
        ]
    
    def load(self):
        return self.walls