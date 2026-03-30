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
        
        self.reward_lines = [
            Wall(batch, 95, 309, 190, 300, color=(0, 255, 0, 255)),
            Wall(batch, 139, 434, 223, 415, color=(0, 255, 0, 255)),
            Wall(batch, 130, 513, 211, 547, color=(0, 255, 0, 255)),
            Wall(batch, 108, 625, 191, 590, color=(0, 255, 0, 255)),
            Wall(batch, 247, 700, 262, 592, color=(0, 255, 0, 255)),
            Wall(batch, 376, 705, 376, 592, color=(0, 255, 0, 255)),
            Wall(batch, 518, 680, 479, 595, color=(0, 255, 0, 255)),
            Wall(batch, 581, 672, 582, 597, color=(0, 255, 0, 255)),
            Wall(batch, 687, 720, 708, 596, color=(0, 255, 0, 255)),
            Wall(batch, 856, 702, 825, 599, color=(0, 255, 0, 255)),
            Wall(batch, 900, 600, 1025, 600, color=(0, 255, 0, 255)),
            Wall(batch, 844, 534, 972, 512, color=(0, 255, 0, 255)),
            Wall(batch, 779, 461, 917, 417, color=(0, 255, 0, 255)),
            Wall(batch, 757, 469, 715, 361, color=(0, 255, 0, 255)),
            Wall(batch, 652, 508, 600, 390, color=(0, 255, 0, 255)),
            Wall(batch, 450, 536, 455, 434, color=(0, 255, 0, 255)),
            Wall(batch, 319, 449, 423, 407, color=(0, 255, 0, 255)),
            Wall(batch, 270, 301, 402, 301, color=(0, 255, 0, 255)),
            Wall(batch, 529, 274, 423, 168, color=(0, 255, 0, 255)),
            Wall(batch, 661, 247, 616, 144, color=(0, 255, 0, 255)),
            Wall(batch, 779, 224, 775, 123, color=(0, 255, 0, 255)),
            Wall(batch, 880, 108, 909, 198, color=(0, 255, 0, 255)),
            Wall(batch, 934, 100, 1093, 76, color=(0, 255, 0, 255)),
            Wall(batch, 881, 101, 881, 20, color=(0, 255, 0, 255)),
            Wall(batch, 750, 105, 750, 24, color=(0, 255, 0, 255)),
            Wall(batch, 616, 109, 616, 28, color=(0, 255, 0, 255)),
            Wall(batch, 484, 113, 484, 32, color=(0, 255, 0, 255)),
            Wall(batch, 356, 117, 356, 36, color=(0, 255, 0, 255)),
            Wall(batch, 230, 150, 169, 67, color=(0, 255, 0, 255)),
            Wall(batch, 91, 178, 182, 178, color=(0, 255, 0, 255))
        ]
        
        print(len(self.reward_lines))
    
    def load(self):
        return self.walls