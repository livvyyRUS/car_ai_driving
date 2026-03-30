from .map import Map
from src.objects.wall import Wall
from pyglet.graphics import Batch


class Map8(Map):
    """
    Complex figure-8 track with crossing sections.
    Features: crossover bridge, loops, technical sections.
    """
    def __init__(self, batch: Batch) -> None:
        self.car_pos_x = 200
        self.car_pos_y = 400

        self.walls = [
            # =========================
            # OUTER BOUNDARY
            # =========================
            Wall(batch, 30, 30, 30, 770),
            Wall(batch, 30, 770, 150, 795),
            Wall(batch, 150, 795, 400, 785),
            Wall(batch, 400, 785, 600, 795),
            Wall(batch, 600, 795, 800, 785),
            Wall(batch, 800, 785, 1050, 795),
            Wall(batch, 1050, 795, 1170, 770),
            Wall(batch, 1170, 770, 1190, 550),
            Wall(batch, 1190, 550, 1200, 400),
            Wall(batch, 1200, 400, 1190, 250),
            Wall(batch, 1190, 250, 1170, 30),
            Wall(batch, 1170, 30, 1050, 20),
            Wall(batch, 1050, 20, 800, 30),
            Wall(batch, 800, 30, 600, 20),
            Wall(batch, 600, 20, 400, 30),
            Wall(batch, 400, 30, 150, 20),
            Wall(batch, 150, 20, 30, 30),

            # =========================
            # FIGURE-8 OUTER LOOP
            # =========================
            Wall(batch, 110, 110, 110, 350),
            Wall(batch, 110, 350, 180, 420),
            Wall(batch, 180, 420, 280, 400),
            Wall(batch, 280, 400, 380, 450),
            Wall(batch, 380, 450, 500, 420),
            Wall(batch, 500, 420, 600, 450),
            Wall(batch, 600, 450, 720, 420),
            Wall(batch, 720, 420, 820, 450),
            Wall(batch, 820, 450, 920, 400),
            Wall(batch, 920, 400, 1020, 420),
            Wall(batch, 1020, 420, 1090, 350),
            Wall(batch, 1090, 350, 1090, 110),
            Wall(batch, 1090, 110, 1000, 90),
            Wall(batch, 1000, 90, 850, 100),
            Wall(batch, 850, 100, 720, 90),
            Wall(batch, 720, 90, 600, 100),
            Wall(batch, 600, 100, 480, 90),
            Wall(batch, 480, 90, 360, 100),
            Wall(batch, 360, 100, 240, 90),
            Wall(batch, 240, 90, 110, 110),

            # =========================
            # FIGURE-8 INNER LOOP (TOP)
            # =========================
            Wall(batch, 200, 480, 200, 600),
            Wall(batch, 200, 600, 280, 650),
            Wall(batch, 280, 650, 380, 630),
            Wall(batch, 380, 630, 480, 660),
            Wall(batch, 480, 660, 520, 600),
            Wall(batch, 520, 600, 520, 480),
            Wall(batch, 520, 480, 450, 500),
            Wall(batch, 450, 500, 380, 480),
            Wall(batch, 380, 480, 300, 500),
            Wall(batch, 300, 500, 200, 480),

            # =========================
            # FIGURE-8 INNER LOOP (BOTTOM)
            # =========================
            Wall(batch, 680, 480, 680, 600),
            Wall(batch, 680, 600, 760, 650),
            Wall(batch, 760, 650, 860, 630),
            Wall(batch, 860, 630, 960, 660),
            Wall(batch, 960, 660, 1000, 600),
            Wall(batch, 1000, 600, 1000, 480),
            Wall(batch, 1000, 480, 930, 500),
            Wall(batch, 930, 500, 860, 480),
            Wall(batch, 860, 480, 780, 500),
            Wall(batch, 780, 500, 680, 480),

            # =========================
            # CROSSOVER BRIDGE SECTION
            # =========================
            Wall(batch, 480, 380, 520, 380),
            Wall(batch, 520, 380, 540, 420),
            Wall(batch, 540, 420, 480, 440),
            Wall(batch, 480, 440, 460, 400),
            Wall(batch, 460, 400, 480, 380),

            # =========================
            # LEFT SIDE TECHNICAL
            # =========================
            Wall(batch, 150, 200, 220, 210),
            Wall(batch, 220, 210, 240, 280),
            Wall(batch, 240, 280, 150, 290),
            Wall(batch, 150, 290, 150, 200),

            Wall(batch, 150, 520, 230, 530),
            Wall(batch, 230, 530, 250, 600),
            Wall(batch, 250, 600, 150, 610),
            Wall(batch, 150, 610, 150, 520),

            # =========================
            # RIGHT SIDE TECHNICAL
            # =========================
            Wall(batch, 980, 200, 1050, 210),
            Wall(batch, 1050, 210, 1070, 280),
            Wall(batch, 1070, 280, 980, 290),
            Wall(batch, 980, 290, 980, 200),

            Wall(batch, 950, 520, 1030, 530),
            Wall(batch, 1030, 530, 1050, 600),
            Wall(batch, 1050, 600, 950, 610),
            Wall(batch, 950, 610, 950, 520),

            # =========================
            # CENTER COMPLEX
            # =========================
            Wall(batch, 420, 320, 500, 330),
            Wall(batch, 500, 330, 520, 380),
            Wall(batch, 520, 380, 420, 370),
            Wall(batch, 420, 370, 420, 320),

            Wall(batch, 680, 320, 760, 330),
            Wall(batch, 760, 330, 780, 380),
            Wall(batch, 780, 380, 680, 370),
            Wall(batch, 680, 370, 680, 320),

            # =========================
            # TOP LOOPS
            # =========================
            Wall(batch, 300, 680, 380, 690),
            Wall(batch, 380, 690, 400, 740),
            Wall(batch, 400, 740, 300, 730),
            Wall(batch, 300, 730, 300, 680),

            Wall(batch, 800, 680, 880, 690),
            Wall(batch, 880, 690, 900, 740),
            Wall(batch, 900, 740, 800, 730),
            Wall(batch, 800, 730, 800, 680),

            # =========================
            # BOTTOM CHICANES
            # =========================
            Wall(batch, 280, 150, 340, 160),
            Wall(batch, 340, 160, 360, 210),
            Wall(batch, 360, 210, 280, 200),
            Wall(batch, 280, 200, 280, 150),

            Wall(batch, 500, 140, 580, 150),
            Wall(batch, 580, 150, 600, 200),
            Wall(batch, 600, 200, 500, 190),
            Wall(batch, 500, 190, 500, 140),

            Wall(batch, 740, 150, 800, 160),
            Wall(batch, 800, 160, 820, 210),
            Wall(batch, 820, 210, 740, 200),
            Wall(batch, 740, 200, 740, 150),

            # =========================
            # INNER OBSTACLES
            # =========================
            Wall(batch, 350, 380, 400, 390),
            Wall(batch, 400, 390, 410, 440),
            Wall(batch, 410, 440, 350, 430),
            Wall(batch, 350, 430, 350, 380),

            Wall(batch, 800, 380, 850, 390),
            Wall(batch, 850, 390, 860, 440),
            Wall(batch, 860, 440, 800, 430),
            Wall(batch, 800, 430, 800, 380),

            # =========================
            # SPIRAL SECTIONS
            # =========================
            Wall(batch, 220, 350, 280, 360),
            Wall(batch, 280, 360, 300, 420),
            Wall(batch, 300, 420, 220, 410),
            Wall(batch, 220, 410, 220, 350),

            Wall(batch, 900, 350, 960, 360),
            Wall(batch, 960, 360, 980, 420),
            Wall(batch, 980, 420, 900, 410),
            Wall(batch, 900, 410, 900, 350),

            # =========================
            # BRIDGE SUPPORTS
            # =========================
            Wall(batch, 560, 350, 600, 360),
            Wall(batch, 600, 360, 610, 400),
            Wall(batch, 610, 400, 560, 390),
            Wall(batch, 560, 390, 560, 350),

            # =========================
            # ADDITIONAL CHALLENGES
            # =========================
            Wall(batch, 180, 720, 260, 730),
            Wall(batch, 260, 730, 280, 760),
            Wall(batch, 280, 760, 180, 750),
            Wall(batch, 180, 750, 180, 720),

            Wall(batch, 920, 720, 1000, 730),
            Wall(batch, 1000, 730, 1020, 760),
            Wall(batch, 1020, 760, 920, 750),
            Wall(batch, 920, 750, 920, 720),
        ]
        
        self.reward_lines = []

    def load(self):
        return self.walls
