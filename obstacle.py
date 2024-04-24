import arcade
from constants import *
import random
import time

class Obstacle(arcade.Sprite):
    """класс описывает препятствие"""
    def __init__(
                self,
                x, 
                y, 
                speed, 
                window,
                file_name = BASE_PATH + "//wall.png",
                ):
        #через super вызываем метод класса - родителяrr
        super().__init__(file_name, 0.7)
        #устанавливаем значения атрибутов положения
        self.center_x = x
        self.center_y = y
        self.change_y = speed
        self.window = window #Ссылка на объект game
        

    def update(self):
        self.center_y -= self.change_y
        if self.bottom <= 0:
            self.set_position(random.randint(0,SCREEN_WIDTH), SCREEN_HEIGHT - 100)
            self.window.change_obstacle_index()
            self.window.score += 1

        if self.window.collision:
            self.set_position(random.randint(0,SCREEN_WIDTH), SCREEN_HEIGHT - 100)
            

    
class Deer(arcade.Sprite):
    def __init__(
                self,
                x, 
                y, 
                speed,
                window,
                file_name = BASE_PATH + "//deer.png",
                ):
        super().__init__(file_name, 0.1)
        self.center_x = x
        self.center_y = y
        self.change_x = speed
        self.spawn_time = time.time()
        self.window = window

    def update(self):
        self.center_x -= self.change_x
        self.center_y -= self.change_x
        if self.bottom < 0:
            if (time.time() - self.spawn_time) >= 8:
                self.spawn_time = time.time()
                self.center_x = 600
                self.center_y = 600

        collision = arcade.check_for_collision(self.window.car, self)

        if collision:
            self.set_position(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100)
            self.window.lives -= 1

