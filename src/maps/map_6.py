from .map import Map
from src.objects.wall import Wall
from pyglet.graphics import Batch


class Map6(Map):
    """
    City block track with 90-degree turns and grid-like layout.
    Features: sharp corners, intersections, parking lot sections.
    """
    def __init__(self, batch: Batch) -> None:
        self.car_pos_x = 140
        self.car_pos_y = 180

        self.walls = [
            # =========================
            # OUTER BOUNDARY
            # =========================
            Wall(batch, 30, 30, 30, 770),
            Wall(batch, 30, 770, 150, 790),
            Wall(batch, 150, 790, 400, 780),
            Wall(batch, 400, 780, 650, 790),
            Wall(batch, 650, 790, 900, 780),
            Wall(batch, 900, 780, 1150, 770),
            Wall(batch, 1150, 770, 1200, 600),
            Wall(batch, 1200, 600, 1210, 400),
            Wall(batch, 1210, 400, 1200, 200),
            Wall(batch, 1200, 200, 1150, 30),
            Wall(batch, 1150, 30, 900, 20),
            Wall(batch, 900, 20, 650, 30),
            Wall(batch, 650, 30, 400, 20),
            Wall(batch, 400, 20, 150, 30),
            Wall(batch, 150, 30, 30, 30),

            # =========================
            # MAIN CITY GRID - STREETS
            # =========================
            Wall(batch, 100, 100, 100, 700),
            Wall(batch, 100, 700, 200, 720),
            Wall(batch, 200, 720, 350, 710),
            Wall(batch, 350, 710, 500, 720),
            Wall(batch, 500, 720, 650, 710),
            Wall(batch, 650, 710, 800, 720),
            Wall(batch, 800, 720, 950, 710),
            Wall(batch, 950, 710, 1080, 700),
            Wall(batch, 1080, 700, 1120, 550),
            Wall(batch, 1120, 550, 1130, 400),
            Wall(batch, 1130, 400, 1120, 250),
            Wall(batch, 1120, 250, 1080, 100),
            Wall(batch, 1080, 100, 950, 90),
            Wall(batch, 950, 90, 800, 100),
            Wall(batch, 800, 100, 650, 90),
            Wall(batch, 650, 90, 500, 100),
            Wall(batch, 500, 100, 350, 90),
            Wall(batch, 350, 90, 200, 100),
            Wall(batch, 200, 100, 100, 100),

            # =========================
            # BLOCK 1 - TOP LEFT
            # =========================
            Wall(batch, 160, 550, 280, 560),
            Wall(batch, 280, 560, 290, 650),
            Wall(batch, 290, 650, 160, 640),
            Wall(batch, 160, 640, 160, 550),

            Wall(batch, 170, 420, 270, 430),
            Wall(batch, 270, 430, 280, 500),
            Wall(batch, 280, 500, 170, 490),
            Wall(batch, 170, 490, 170, 420),

            # =========================
            # BLOCK 2 - TOP CENTER
            # =========================
            Wall(batch, 420, 560, 560, 570),
            Wall(batch, 560, 570, 570, 660),
            Wall(batch, 570, 660, 420, 650),
            Wall(batch, 420, 650, 420, 560),

            Wall(batch, 430, 430, 550, 440),
            Wall(batch, 550, 440, 560, 510),
            Wall(batch, 560, 510, 430, 500),
            Wall(batch, 430, 500, 430, 430),

            # =========================
            # BLOCK 3 - TOP RIGHT
            # =========================
            Wall(batch, 680, 550, 820, 560),
            Wall(batch, 820, 560, 830, 650),
            Wall(batch, 830, 650, 680, 640),
            Wall(batch, 680, 640, 680, 550),

            Wall(batch, 690, 420, 810, 430),
            Wall(batch, 810, 430, 820, 500),
            Wall(batch, 820, 500, 690, 490),
            Wall(batch, 690, 490, 690, 420),

            # =========================
            # BLOCK 4 - BOTTOM LEFT
            # =========================
            Wall(batch, 160, 280, 300, 290),
            Wall(batch, 300, 290, 310, 380),
            Wall(batch, 310, 380, 160, 370),
            Wall(batch, 160, 370, 160, 280),

            Wall(batch, 170, 150, 290, 160),
            Wall(batch, 290, 160, 300, 230),
            Wall(batch, 300, 230, 170, 220),
            Wall(batch, 170, 220, 170, 150),

            # =========================
            # BLOCK 5 - BOTTOM CENTER
            # =========================
            Wall(batch, 420, 270, 580, 280),
            Wall(batch, 580, 280, 590, 390),
            Wall(batch, 590, 390, 420, 380),
            Wall(batch, 420, 380, 420, 270),

            Wall(batch, 430, 140, 570, 150),
            Wall(batch, 570, 150, 580, 220),
            Wall(batch, 580, 220, 430, 210),
            Wall(batch, 430, 210, 430, 140),

            # =========================
            # BLOCK 6 - BOTTOM RIGHT
            # =========================
            Wall(batch, 700, 280, 850, 290),
            Wall(batch, 850, 290, 860, 390),
            Wall(batch, 860, 390, 700, 380),
            Wall(batch, 700, 380, 700, 280),

            Wall(batch, 710, 140, 840, 150),
            Wall(batch, 840, 150, 850, 230),
            Wall(batch, 850, 230, 710, 220),
            Wall(batch, 710, 220, 710, 140),

            # =========================
            # INTERSECTION DETAILS
            # =========================
            Wall(batch, 320, 300, 380, 310),
            Wall(batch, 380, 310, 390, 370),
            Wall(batch, 390, 370, 320, 360),
            Wall(batch, 320, 360, 320, 300),

            Wall(batch, 600, 300, 660, 310),
            Wall(batch, 660, 310, 670, 370),
            Wall(batch, 670, 370, 600, 360),
            Wall(batch, 600, 360, 600, 300),

            # =========================
            # PARKING LOT AREAS
            # =========================
            Wall(batch, 880, 450, 1000, 460),
            Wall(batch, 1000, 460, 1010, 550),
            Wall(batch, 1010, 550, 880, 540),
            Wall(batch, 880, 540, 880, 450),

            Wall(batch, 890, 250, 990, 260),
            Wall(batch, 990, 260, 1000, 350),
            Wall(batch, 1000, 350, 890, 340),
            Wall(batch, 890, 340, 890, 250),

            # =========================
            # ALLEYWAYS
            # =========================
            Wall(batch, 320, 440, 380, 450),
            Wall(batch, 380, 450, 390, 520),
            Wall(batch, 390, 520, 320, 510),
            Wall(batch, 320, 510, 320, 440),

            Wall(batch, 600, 440, 660, 450),
            Wall(batch, 660, 450, 670, 520),
            Wall(batch, 670, 520, 600, 510),
            Wall(batch, 600, 510, 600, 440),
        ]

    def load(self):
        return self.walls
