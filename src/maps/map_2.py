from .map import Map
from src.objects.wall import Wall
from pyglet.graphics import Batch

class Map2(Map):
    def __init__(self, batch: Batch) -> None:
        self.car_pos_x = 200
        self.car_pos_y = 150
        # Все стены задаются координатами (x1, y1, x2, y2)
        self.walls = [
            # Внешний периметр (против часовой стрелки)
            Wall(batch, 50, 50, 60, 450),
            Wall(batch, 60, 450, 180, 580),
            Wall(batch, 180, 580, 500, 590),
            Wall(batch, 500, 590, 700, 530),
            Wall(batch, 700, 530, 950, 560),
            Wall(batch, 950, 560, 1150, 480),
            Wall(batch, 1150, 480, 1180, 200),
            Wall(batch, 1180, 200, 1050, 70),
            Wall(batch, 1050, 70, 700, 40),
            Wall(batch, 700, 40, 400, 45),
            Wall(batch, 400, 45, 200, 30),
            Wall(batch, 200, 30, 50, 50),

            # Внутренние стены (формируют коридоры и препятствия)
            Wall(batch, 120, 120, 140, 350),
            Wall(batch, 140, 350, 260, 480),
            Wall(batch, 260, 480, 480, 480),
            Wall(batch, 480, 480, 620, 400),
            Wall(batch, 620, 400, 850, 430),
            Wall(batch, 850, 430, 1020, 380),
            Wall(batch, 1020, 380, 1050, 200),
            Wall(batch, 1050, 200, 900, 120),
            Wall(batch, 900, 120, 650, 110),
            Wall(batch, 650, 110, 400, 130),
            Wall(batch, 400, 130, 250, 100),
            Wall(batch, 250, 100, 120, 120),

            # Дополнительные изолирующие стены
            Wall(batch, 320, 220, 330, 360),
            Wall(batch, 330, 360, 520, 370),
            Wall(batch, 520, 370, 530, 250),
            Wall(batch, 530, 250, 320, 220),

            Wall(batch, 700, 180, 710, 300),
            Wall(batch, 710, 300, 900, 310),
            Wall(batch, 900, 310, 910, 190),
            Wall(batch, 910, 190, 700, 180),
        ]
        
        self.reward_lines = []

    def load(self):
        return self.walls