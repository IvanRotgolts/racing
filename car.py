import arcade
from constants import *

class Car(arcade.Sprite):
    """Описывает машину"""
    def __init__(self, center_x, center_y, file_name = BASE_PATH + "//blue_car.png"):
        #Через функцию super вызываем метод конструктор init родителя
        super().__init__(file_name, 0.7)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 0

    def update(self):
        self.center_x += self.change_x

        if self.left <= 0:
            self.left = 0

        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH