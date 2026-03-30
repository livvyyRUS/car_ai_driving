import pyglet
import math
import numpy as np

from pyglet.graphics import Batch, Group
from pyglet.window import Window
from pyglet.sprite import Sprite
from pyglet.window import key

from .object import Object
from .wall import Wall

from src.maps.map import Map


class Car(Object):
    def __init__(
        self, x_pos: float, y_pos: float, batch: Batch, window: Window, map: Map
    ) -> None:
        self.batch = batch
        self.window = window
        self.map = map

        # Загружаем изображение
        self.image = pyglet.image.load("sprites\\little_car.png")

        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2

        self.sprite = Sprite(
            self.image, batch=self.batch, x=x_pos, y=y_pos, group=Group(2)
        )
        # Сохраняем координаты центра
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.last_x_pos = x_pos
        self.last_y_pos = y_pos

        # Остальные параметры...
        self.speed = 1000
        self.max_multiplyer = 1000
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 0
        self.speed_scalar = 0
        self.turn_speed = 125
        self.controls = {
            key.UP: False,
            key.DOWN: False,
            key.LEFT: False,
            key.RIGHT: False,
        }

    def update(self, dt):
        self.last_x_pos = self.x_pos
        self.last_y_pos = self.y_pos
        
        # Управление ускорением
        acceleration = 0
        if self.controls[key.UP]:
            acceleration += self.speed
        if self.controls[key.DOWN]:
            acceleration -= self.speed

        # Управление поворотом
        turn = 0
        if self.controls[key.LEFT]:
            turn -= self.turn_speed * dt
        if self.controls[key.RIGHT]:
            turn += self.turn_speed * dt

        self.angle += turn
        self.angle %= 360

        self.speed_scalar += acceleration * dt
        max_speed = self.speed * self.max_multiplyer
        self.speed_scalar = max(-max_speed, min(max_speed, self.speed_scalar))
        self.speed_scalar *= 0.95
        if abs(self.speed_scalar) < 0.1:
            self.speed_scalar = 0

        # ⬇️ Главное исправление: добавляем смещение 90°, если нос машины смотрит вверх
        angle_rad = math.radians(self.angle + 90)  # поправка для картинки с носом вверх
        self.velocity_x = self.speed_scalar * -math.cos(angle_rad)
        self.velocity_y = self.speed_scalar * math.sin(angle_rad)

        self.x_pos += self.velocity_x * dt
        self.y_pos += self.velocity_y * dt

        # Ограничение по границам окна
        self.x_pos = max(
            self.image.anchor_x,
            min(self.window.width - self.image.anchor_x, self.x_pos),
        )
        self.y_pos = max(
            self.image.anchor_y,
            min(self.window.height - self.image.anchor_y, self.y_pos),
        )

        self.sprite.position = (self.x_pos, self.y_pos, 0)
        self.sprite.rotation = self.angle
        
        self.reward_state = len(self.map.reward_lines) - 1

    def get_rotated_corners(self):
        angle = math.radians(
            -self.sprite.rotation
        )  # В pyglet вращение по часовой стрелке

        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        corners = []
        # Смещения углов относительно точки привязки
        points = [
            (-self.image.anchor_x, -self.image.anchor_y),
            (self.image.width - self.image.anchor_x, -self.image.anchor_y),
            (
                self.image.width - self.image.anchor_x,
                self.image.height - self.image.anchor_y,
            ),
            (-self.image.anchor_x, self.image.height - self.image.anchor_y),
        ]

        for px, py in points:
            # Матрица поворота
            tx = self.x_pos + (px * cos_a - py * sin_a)
            ty = self.y_pos + (px * sin_a + py * cos_a)
            corners.append((tx, ty))
        return corners  # Возвращает [BL, BR, TR, TL]

    @staticmethod
    def ccw(A: tuple[int, int], B: tuple[int, int], C: tuple[int, int]):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    @staticmethod
    def intersect(
        a: tuple[int, int], b: tuple[int, int], c: tuple[int, int], d: tuple[int, int]
    ):
        """Проверка пересечения двух отрезков AB и CD"""
        return Car.ccw(a, c, d) != Car.ccw(b, c, d) and Car.ccw(a, b, c) != Car.ccw(
            a, b, d
        )

    def sprite_wall_collision(
        self, line_start: tuple[int, int], line_end: tuple[int, int]
    ):
        corners = self.get_rotated_corners()
        # Проверяем все 4 стороны спрайта
        edges = [
            (corners[0], corners[1]),
            (corners[1], corners[2]),
            (corners[2], corners[3]),
            (corners[3], corners[0]),
        ]
        for edge_start, edge_end in edges:
            if self.intersect(line_start, line_end, edge_start, edge_end):
                return True
        return False

    def wall_colisions(self):
        for wall in self.map.walls:
            if self.sprite_wall_collision((wall.x1, wall.y1), (wall.x2, wall.y2)):
                return True
        return False
    
    def reward_colisions(self):
        for index, wall in enumerate(self.map.reward_lines):
            if self.sprite_wall_collision((wall.x1, wall.y1), (wall.x2, wall.y2)):
                return index
        return -1

    def func_when_dead(self):
        self.x_pos = self.last_x_pos
        self.y_pos = self.last_y_pos

    def func_when_alive(self):
        self.sprite.color = (255, 255, 255)
        
    def cast_ray(self, angle_deg, max_distance=400):
        """Пустить луч от центра машинки под углом angle_deg (глобальный угол).
        Вернуть расстояние до ближайшей стены или max_distance."""
        angle_rad = math.radians(angle_deg)
        dx = math.cos(angle_rad)
        dy = math.sin(angle_rad)
        # Начальная точка
        x0, y0 = self.x_pos, self.y_pos
        min_dist = max_distance
        for wall in self.map.walls:
            # wall – объект с атрибутами x1,y1,x2,y2
            # Проверяем пересечение луча (x0,y0)-(x0+dx*max_dist, y0+dy*max_dist) со стеной
            intersect_point = self.ray_segment_intersection(
                (x0, y0), (x0+dx*max_distance, y0+dy*max_distance),
                (wall.x1, wall.y1), (wall.x2, wall.y2)
            )
            if intersect_point:
                dist = math.hypot(intersect_point[0]-x0, intersect_point[1]-y0)
                if dist < min_dist:
                    min_dist = dist
        return min_dist

    @staticmethod
    def ray_segment_intersection(ray_start, ray_end, seg_start, seg_end):
        # Решение системы параметрических уравнений. Можно использовать готовый алгоритм.
        # Возвращает точку пересечения или None.
        # (Здесь упрощённо – для реального кода нужна проверка)
        # Приведу рабочий вариант:
        x1, y1 = ray_start
        x2, y2 = ray_end
        x3, y3 = seg_start
        x4, y4 = seg_end
        
        denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if denom == 0:
            return None
        t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
        u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / denom
        if 0 <= t <= 1 and 0 <= u <= 1:
            x = x1 + t*(x2-x1)
            y = y1 + t*(y2-y1)
            return (x, y)
        return None
        
    def get_sensor_readings(self, max_dist=400):
        angles = list(range(0, 360, 45))  # углы относительно направления машины
        readings = []
        for rel_angle in angles:
            global_angle = self.angle + rel_angle
            dist = self.cast_ray(global_angle, self.map.walls, max_dist)
            norm_dist = dist / max_dist
            readings.append(norm_dist)
        # Добавим скорость и ориентацию
        speed_norm = self.speed_scalar / (self.speed * self.max_multiplyer)
        angle_rad = math.radians(self.angle)
        readings.extend([speed_norm, math.sin(angle_rad), math.cos(angle_rad)])
        return np.array(readings, dtype=np.float32)


    def remove(self):
        if self.sprite:
            self.sprite.delete()
            self.sprite = None
            
            
    def get_reward(self):
        if self.wall_colisions():
            return -10
        
        get_wall = self.get_reward()
        if get_wall == -1:
            return 0.1
        
        waited_wall = self.reward_state + 1 if self.reward_state + 1 < len(self.map.reward_lines) else 0
        
        if get_wall == waited_wall == 29:
            return 20
        
        if get_wall == waited_wall:
            return 10
        
        
        
        