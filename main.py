import arcade
from constants import *
from car import *
from obstacle import *

class Game(arcade.Window):
    def __init__(self, width, height, title) :
        super().__init__(width, height, title) 
        #это объект машины
        self.car = Car (300, 200)
        #фон для игры
        self.background = arcade.load_texture(BASE_PATH + "//bg.png")
        self.obstacles = list()
        self.set_up()
        self.current_obstacle_index = 0
        self.deer = Deer(600, 600, 3)

    def set_up(self):
        for i in range(5):
            self.generate_obsticle()

    def generate_obsticle(self):
        #задаем начальное положение препятствию
        obstacle_position_x = random.randint(0,SCREEN_WIDTH)
        obstacle_position_y = SCREEN_HEIGHT - 100

        #создаем объект препятствие
        obstacle = Obstacle(obstacle_position_x, 
                            obstacle_position_y,
                            3,
                            self)
        self.obstacles.append(obstacle)


    def on_draw(self):
        self.clear()
        #отрисовываем фон
        arcade.draw_texture_rectangle(
            SCREEN_HEIGHT/2,
            SCREEN_WIDTH/2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.background
        )
        self.car.draw()
        self.obstacles[self.current_obstacle_index].draw()
        self.deer.draw()

    def update(self, delta_time):
        self.car.update()
        self.obstacles[self.current_obstacle_index].update()
        self.deer.update()


    def on_key_press(self, symbol: int, modifiers: int):
        #метод работаетс клавиатурой(нажатие клавиш)
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.car.change_x = -CAR_SPEED_X
            self.car.angle = CAR_ANGLE

        
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.car.change_x = CAR_SPEED_X
            self.car.angle = -CAR_ANGLE
    
    def on_key_release(self, symbol: int, modifiers: int):
        self.car.change_x = 0
        self.car.angle = 0


    def change_obstacle_index(self):
        """изменяет индекс препятсвия"""
        self.current_obstacle_index += 1
        #проверяем, что индекс не перешел за недопустимый интервал
        if self.current_obstacle_index > len(self.obstacles) - 1:
            self.current_obstacle_index = 0
        




































window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, 'Пинг-Понг') 
arcade.run()