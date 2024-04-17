import arcade
from constants import *
import random
import time

class Border(arcade.Sprite):
    """класс описывает объект"""
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
        self.window = window