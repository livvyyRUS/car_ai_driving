from .map import Map
from src.objects.wall import Wall
from pyglet.graphics import Batch


class Map5(Map):
    """
    Highway-style track with fast sections and gentle curves.
    Features: long straights, wide turns, oval layout with inner obstacles.
    """
    def __init__(self, batch: Batch) -> None:
        self.car_pos_x = 180
        self.car_pos_y = 400

        self.walls = [
            # =========================
            # OUTER BOUNDARY
            # =========================
            Wall(batch, 40, 40, 40, 760),
            Wall(batch, 40, 760, 180, 790),
            Wall(batch, 180, 790, 500, 800),
            Wall(batch, 500, 800, 800, 790),
            Wall(batch, 800, 790, 1100, 760),
            Wall(batch, 1100, 760, 1180, 600),
            Wall(batch, 1180, 600, 1190, 400),
            Wall(batch, 1190, 400, 1180, 200),
            Wall(batch, 1180, 200, 1100, 40),
            Wall(batch, 1100, 40, 800, 30),
            Wall(batch, 800, 30, 500, 20),
            Wall(batch, 500, 20, 180, 30),
            Wall(batch, 180, 30, 40, 40),

            # =========================
            # MAIN HIGHWAY LOOP
            # =========================
            Wall(batch, 120, 120, 120, 680),
            Wall(batch, 120, 680, 220, 710),
            Wall(batch, 220, 710, 450, 720),
            Wall(batch, 450, 720, 680, 710),
            Wall(batch, 680, 710, 900, 680),
            Wall(batch, 900, 680, 1050, 620),
            Wall(batch, 1050, 620, 1080, 500),
            Wall(batch, 1080, 500, 1080, 300),
            Wall(batch, 1080, 300, 1050, 180),
            Wall(batch, 1050, 180, 900, 120),
            Wall(batch, 900, 120, 680, 110),
            Wall(batch, 680, 110, 450, 100),
            Wall(batch, 450, 100, 220, 110),
            Wall(batch, 220, 110, 120, 120),

            # =========================
            # INNER OBSTACLES - TOP
            # =========================
            Wall(batch, 300, 580, 450, 590),
            Wall(batch, 450, 590, 470, 640),
            Wall(batch, 470, 640, 300, 650),
            Wall(batch, 300, 650, 300, 580),

            Wall(batch, 550, 570, 700, 580),
            Wall(batch, 700, 580, 720, 650),
            Wall(batch, 720, 650, 550, 640),
            Wall(batch, 550, 640, 550, 570),

            # =========================
            # INNER OBSTACLES - CENTER
            # =========================
            Wall(batch, 350, 420, 500, 430),
            Wall(batch, 500, 430, 520, 500),
            Wall(batch, 520, 500, 350, 490),
            Wall(batch, 350, 490, 350, 420),

            Wall(batch, 600, 400, 750, 410),
            Wall(batch, 750, 410, 770, 480),
            Wall(batch, 770, 480, 600, 470),
            Wall(batch, 600, 470, 600, 400),

            # =========================
            # INNER OBSTACLES - BOTTOM
            # =========================
            Wall(batch, 300, 250, 450, 260),
            Wall(batch, 450, 260, 470, 330),
            Wall(batch, 470, 330, 300, 320),
            Wall(batch, 300, 320, 300, 250),

            Wall(batch, 550, 240, 700, 250),
            Wall(batch, 700, 250, 720, 340),
            Wall(batch, 720, 340, 550, 330),
            Wall(batch, 550, 330, 550, 240),

            # =========================
            # PIT LANE AREA
            # =========================
            Wall(batch, 180, 350, 260, 360),
            Wall(batch, 260, 360, 280, 450),
            Wall(batch, 280, 450, 180, 440),
            Wall(batch, 180, 440, 180, 350),

            # =========================
            # CHICANE ON STRAIGHT
            # =========================
            Wall(batch, 800, 150, 850, 160),
            Wall(batch, 850, 160, 870, 220),
            Wall(batch, 870, 220, 800, 230),
            Wall(batch, 800, 230, 800, 150),

            Wall(batch, 820, 580, 870, 590),
            Wall(batch, 870, 590, 890, 650),
            Wall(batch, 890, 650, 820, 640),
            Wall(batch, 820, 640, 820, 580),

            # =========================
            # BANKED TURN SIMULATION
            # =========================
            Wall(batch, 950, 280, 1020, 300),
            Wall(batch, 1020, 300, 1030, 380),
            Wall(batch, 1030, 380, 950, 360),
            Wall(batch, 950, 360, 950, 280),

            Wall(batch, 970, 450, 1040, 470),
            Wall(batch, 1040, 470, 1050, 530),
            Wall(batch, 1050, 530, 970, 510),
            Wall(batch, 970, 510, 970, 450),

            # =========================
            # SPEED TRAP SECTION
            # =========================
            Wall(batch, 500, 150, 650, 160),
            Wall(batch, 650, 160, 660, 200),
            Wall(batch, 660, 200, 500, 190),
            Wall(batch, 500, 190, 500, 150),

            Wall(batch, 520, 620, 670, 630),
            Wall(batch, 670, 630, 680, 670),
            Wall(batch, 680, 670, 520, 660),
            Wall(batch, 520, 660, 520, 620),
        ]

    def load(self):
        return self.walls
