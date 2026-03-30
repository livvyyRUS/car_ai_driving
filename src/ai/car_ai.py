import gymnasium as gym
import numpy as np
from gymnasium import spaces
from pyglet.graphics import Batch
from pyglet.window import Window, key

from src.maps.map import Map
from src.objects.car import Car


class CarEnv(gym.Env):
    def __init__(self, map: Map, batch: Batch, window: Window):
        super(CarEnv, self).__init__()
        
        self.map = map
        self.batch = batch
        self.window = window
        
        self.car = Car(map.car_pos_x, map.car_pos_y, batch, window, self.map)
        # 11 входов: 8 лучей, скорость, угол поворота L, угол поворота R
        self.observation_space = spaces.Box(low=0, high=1, shape=(11,), dtype=np.float32)
        
        # 4 выхода: вперед, назад, влево, вправо (значения от 0 до 1)
        self.action_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)
        
        self.dt = 1 / 60

    def reset(self, seed=None, options=None):
        # Тут сбрасываешь машину на старт и возвращаешь 11 начальных параметров
        self.car.remove()
        
        self.car = Car(self.map.car_pos_x, self.map.car_pos_y, self.batch, self.window, self.map)
        observation = self.car.get_sensor_readings()
        return observation, {}
    
    

    def step(self, action):
        self.car.controls[key.UP] = True if action[0, 0] >= 0.5 else False
        self.car.controls[key.DOWN] = True if action[0, 1] >= 0.5 else False
        self.car.controls[key.LEFT] = True if action[0, 2] >= 0.5 else False
        self.car.controls[key.RIGHT] = True if action[0, 3] >= 0.5 else False
        
        self.car.update(self.dt)
            
        
        observation = self.car.get_sensor_readings()
        
        reward = self.car.get_reward()
        terminated = self.car.wall_colisions()
        truncated = False
        
        return observation, reward, terminated, truncated, {}
