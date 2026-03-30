import pyglet

from pyglet.window import Window
from pyglet.window.key import KeyStateHandler
from pyglet.window import key
from pyglet.graphics import Batch
from src.objects.object import Object
from src.objects.car import Car
from src.maps.map_1 import Map1 as Map
from src.ai.car_ai import CarEnv


class GameWindow(Window):
    def __init__(self, width: int, height: int, *args, **kwargs) -> None:
        super().__init__(width, height, *args, **kwargs)
        self.set_caption("КЧАУ")
        self.keys = KeyStateHandler()
        self.push_handlers(self.keys)
        self.batch = Batch()
        
        self.objects: list[Object] = []
        self.updatable_objects: list[Object] = []
        
        map = Map(self.batch)
        self.walls = map.load()
        self.not_paintable = map.reward_lines
        
        # self.car = Car(map.car_pos_x, map.car_pos_y, self.batch, self, map)
        
        
        self.objects.extend(self.walls)
        
        self.fps = 60
        pyglet.clock.schedule_interval(self.update, 1/self.fps)
        
        from stable_baselines3 import PPO

        self.env = CarEnv(map, self.batch, self)

        self.model = PPO(
            "MlpPolicy",
            self.env,
            verbose=1,
        )

        self.model.learn(total_timesteps=500_000)
        
        
    # def on_key_press(self, symbol, modifiers):
    #     if symbol == key.ESCAPE:
    #         pyglet.app.exit()
    #     if symbol in self.car.controls:
    #         self.car.controls[symbol] = True

    # def on_key_release(self, symbol, modifiers):
    #     if symbol in self.car.controls:
    #         self.car.controls[symbol] = False
        
        
    def update(self, dt):
        for obj in self.objects:
            if hasattr(obj, "update"):
                obj.update(dt)
        # print(self.car.get_sensor_readings(self.walls))
        # if self.car.wall_colisions():
        #     self.car.func_when_dead()
        # else:
        #     self.car.func_when_alive()
        
        
    def on_draw(self):
        self.clear()
        pyglet.gl.glClearColor(0.5, 0.7, 1.0, 1.0) 
        self.batch.draw()
        