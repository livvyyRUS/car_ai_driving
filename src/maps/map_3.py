from .map import Map
from src.objects.wall import Wall
from pyglet.graphics import Batch


class Map3(Map):
    def __init__(self, batch: Batch) -> None:
        self.car_pos_x = 140
        self.car_pos_y = 220

        self.walls = [
            # =========================
            # ВНЕШНИЙ КОНТУР
            # =========================
            Wall(batch, 70, 70, 70, 760),
            Wall(batch, 70, 760, 260, 810),
            Wall(batch, 260, 810, 540, 790),
            Wall(batch, 540, 790, 760, 820),
            Wall(batch, 760, 820, 1110, 760),
            Wall(batch, 1110, 760, 1230, 560),
            Wall(batch, 1230, 560, 1200, 310),
            Wall(batch, 1200, 310, 1120, 120),
            Wall(batch, 1120, 120, 820, 55),
            Wall(batch, 820, 55, 520, 65),
            Wall(batch, 520, 65, 260, 45),
            Wall(batch, 260, 45, 70, 70),

            # =========================
            # ОСНОВНОЕ ВНЕШНЕЕ КОЛЬЦО
            # =========================
            Wall(batch, 160, 140, 160, 690),
            Wall(batch, 160, 690, 320, 730),
            Wall(batch, 320, 730, 560, 715),
            Wall(batch, 560, 715, 800, 735),
            Wall(batch, 800, 735, 980, 700),
            Wall(batch, 980, 700, 1080, 560),
            Wall(batch, 1080, 560, 1050, 380),
            Wall(batch, 1050, 380, 960, 230),
            Wall(batch, 960, 230, 780, 170),
            Wall(batch, 780, 170, 560, 185),
            Wall(batch, 560, 185, 350, 160),
            Wall(batch, 350, 160, 160, 140),

            # =========================
            # ЛЕВЫЙ ЛАБИРИНТ
            # =========================
            Wall(batch, 220, 210, 220, 340),
            Wall(batch, 220, 340, 300, 360),
            Wall(batch, 300, 360, 320, 260),
            Wall(batch, 320, 260, 220, 210),

            Wall(batch, 220, 420, 360, 430),
            Wall(batch, 360, 430, 340, 540),
            Wall(batch, 340, 540, 210, 520),
            Wall(batch, 210, 520, 220, 420),

            Wall(batch, 260, 580, 420, 600),
            Wall(batch, 420, 600, 410, 670),
            Wall(batch, 410, 670, 250, 650),
            Wall(batch, 250, 650, 260, 580),

            # =========================
            # ЦЕНТРАЛЬНЫЕ ПЕРЕГОРОДКИ
            # =========================
            Wall(batch, 380, 230, 520, 250),
            Wall(batch, 520, 250, 540, 340),
            Wall(batch, 540, 340, 400, 360),
            Wall(batch, 400, 360, 380, 230),

            Wall(batch, 460, 420, 620, 440),
            Wall(batch, 620, 440, 640, 540),
            Wall(batch, 640, 540, 480, 560),
            Wall(batch, 480, 560, 460, 420),

            Wall(batch, 520, 620, 700, 640),
            Wall(batch, 700, 640, 720, 710),
            Wall(batch, 720, 710, 540, 700),
            Wall(batch, 540, 700, 520, 620),

            # =========================
            # ПРАВЫЙ ЛАБИРИНТ
            # =========================
            Wall(batch, 760, 230, 920, 250),
            Wall(batch, 920, 250, 900, 360),
            Wall(batch, 900, 360, 770, 340),
            Wall(batch, 770, 340, 760, 230),

            Wall(batch, 810, 430, 980, 450),
            Wall(batch, 980, 450, 960, 560),
            Wall(batch, 960, 560, 790, 540),
            Wall(batch, 790, 540, 810, 430),

            Wall(batch, 820, 610, 1010, 630),
            Wall(batch, 1010, 630, 990, 720),
            Wall(batch, 990, 720, 800, 700),
            Wall(batch, 800, 700, 820, 610),

            # =========================
            # НИЖНИЕ КОРИДОРЫ
            # =========================
            Wall(batch, 340, 760, 360, 690),
            Wall(batch, 360, 690, 470, 670),
            Wall(batch, 470, 670, 490, 760),
            Wall(batch, 490, 760, 340, 760),

            Wall(batch, 620, 770, 640, 680),
            Wall(batch, 640, 680, 760, 660),
            Wall(batch, 760, 660, 780, 760),
            Wall(batch, 780, 760, 620, 770),

            # =========================
            # ДОПОЛНИТЕЛЬНЫЕ УЗКИЕ ПРОХОДЫ
            # =========================
            Wall(batch, 360, 470, 460, 485),
            Wall(batch, 460, 485, 450, 520),
            Wall(batch, 450, 520, 350, 505),
            Wall(batch, 350, 505, 360, 470),

            Wall(batch, 650, 300, 760, 320),
            Wall(batch, 760, 320, 750, 380),
            Wall(batch, 750, 380, 640, 360),
            Wall(batch, 640, 360, 650, 300),

            Wall(batch, 600, 500, 710, 515),
            Wall(batch, 710, 515, 700, 585),
            Wall(batch, 700, 585, 590, 570),
            Wall(batch, 590, 570, 600, 500),
        ]

    def load(self):
        return self.walls