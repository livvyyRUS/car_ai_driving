from pyglet.graphics import Batch, Group
from pyglet.shapes import Line

from .object import Object

class Wall(Object):
    def __init__(self, batch: Batch, x1: int, y1: int, x2: int, y2: int, thickness: int = 3, color: tuple[int, int, int, int] = (255, 255, 255, 255)) -> None:
        self.batch = batch
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.thickness = thickness
        
        self.line = Line(self.x1, self.y1, self.x2, self.y2, self.thickness, self.color, batch=self.batch, group=Group(1))
        
    def update(self, dt):
        pass