from .map import Map
from src.objects.wall import Wall
from pyglet.graphics import Batch


class Map4(Map):
    """
    Technical track with tight corners and chicanes.
    Features: narrow passages, multiple hairpins, complex middle section.
    """
    def __init__(self, batch: Batch) -> None:
        self.car_pos_x = 150
        self.car_pos_y = 400

        self.walls = [
            # =========================
            # OUTER BOUNDARY
            # =========================
            Wall(batch, 50, 50, 50, 750),
            Wall(batch, 50, 750, 200, 780),
            Wall(batch, 200, 780, 450, 770),
            Wall(batch, 450, 770, 700, 780),
            Wall(batch, 700, 780, 950, 770),
            Wall(batch, 950, 770, 1150, 750),
            Wall(batch, 1150, 750, 1180, 550),
            Wall(batch, 1180, 550, 1170, 350),
            Wall(batch, 1170, 350, 1150, 150),
            Wall(batch, 1150, 150, 950, 50),
            Wall(batch, 950, 50, 700, 40),
            Wall(batch, 700, 40, 450, 50),
            Wall(batch, 450, 50, 200, 40),
            Wall(batch, 200, 40, 50, 50),

            # =========================
            # MAIN TRACK - OUTER LOOP
            # =========================
            Wall(batch, 130, 130, 130, 670),
            Wall(batch, 130, 670, 250, 690),
            Wall(batch, 250, 690, 400, 680),
            Wall(batch, 400, 680, 550, 690),
            Wall(batch, 550, 690, 700, 680),
            Wall(batch, 700, 680, 850, 690),
            Wall(batch, 850, 690, 1000, 680),
            Wall(batch, 1000, 680, 1080, 600),
            Wall(batch, 1080, 600, 1090, 450),
            Wall(batch, 1090, 450, 1080, 300),
            Wall(batch, 1080, 300, 1000, 220),
            Wall(batch, 1000, 220, 850, 210),
            Wall(batch, 850, 210, 700, 220),
            Wall(batch, 700, 220, 550, 210),
            Wall(batch, 550, 210, 400, 220),
            Wall(batch, 400, 220, 250, 210),
            Wall(batch, 250, 210, 130, 230),

            # =========================
            # CHICANE SECTION 1 (LEFT)
            # =========================
            Wall(batch, 200, 280, 200, 380),
            Wall(batch, 200, 380, 280, 400),
            Wall(batch, 280, 400, 340, 340),
            Wall(batch, 340, 340, 280, 280),
            Wall(batch, 280, 280, 200, 280),

            Wall(batch, 340, 420, 420, 420),
            Wall(batch, 420, 420, 440, 500),
            Wall(batch, 440, 500, 340, 500),
            Wall(batch, 340, 500, 340, 420),

            # =========================
            # CHICANE SECTION 2 (CENTER)
            # =========================
            Wall(batch, 500, 280, 580, 280),
            Wall(batch, 580, 280, 600, 360),
            Wall(batch, 600, 360, 500, 360),
            Wall(batch, 500, 360, 500, 280),

            Wall(batch, 520, 440, 600, 440),
            Wall(batch, 600, 440, 620, 520),
            Wall(batch, 620, 520, 520, 520),
            Wall(batch, 520, 520, 520, 440),

            # =========================
            # CHICANE SECTION 3 (RIGHT)
            # =========================
            Wall(batch, 720, 300, 800, 300),
            Wall(batch, 800, 300, 820, 380),
            Wall(batch, 820, 380, 720, 380),
            Wall(batch, 720, 380, 720, 300),

            Wall(batch, 740, 460, 840, 460),
            Wall(batch, 840, 460, 860, 540),
            Wall(batch, 860, 540, 740, 540),
            Wall(batch, 740, 540, 740, 460),

            # =========================
            # HAIRPIN TURNS
            # =========================
            Wall(batch, 900, 150, 900, 280),
            Wall(batch, 900, 280, 1020, 300),
            Wall(batch, 1020, 300, 1040, 200),
            Wall(batch, 1040, 200, 900, 150),

            Wall(batch, 920, 520, 1020, 520),
            Wall(batch, 1020, 520, 1040, 620),
            Wall(batch, 1040, 620, 920, 600),
            Wall(batch, 920, 600, 920, 520),

            # =========================
            # S-SHAPED CURVES
            # =========================
            Wall(batch, 300, 550, 380, 570),
            Wall(batch, 380, 570, 420, 620),
            Wall(batch, 420, 620, 300, 640),
            Wall(batch, 300, 640, 300, 550),

            Wall(batch, 600, 150, 680, 170),
            Wall(batch, 680, 170, 720, 120),
            Wall(batch, 720, 120, 600, 100),
            Wall(batch, 600, 100, 600, 150),

            # =========================
            # NARROW GATES
            # =========================
            Wall(batch, 180, 480, 220, 490),
            Wall(batch, 220, 490, 230, 530),
            Wall(batch, 230, 530, 180, 540),
            Wall(batch, 180, 540, 180, 480),

            Wall(batch, 880, 400, 920, 410),
            Wall(batch, 920, 410, 930, 450),
            Wall(batch, 930, 450, 880, 460),
            Wall(batch, 880, 460, 880, 400),
        ]

    def load(self):
        return self.walls
