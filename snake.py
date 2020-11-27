import pygame
import time
import random
import os 
from importlib import reload


dir_path = os.path.dirname(os.path.realpath(__file__))
window_h = 400
window_w = 400


class Player:
    x = 50
    y = 50
    direction = 0
    score = 0
    width = 12
    height = 12
    step = 6
    length = 4

    def update(self):
        if self.direction == 0:
            self.x = self.x + self.step
        if self.direction == 1:
            self.x = self.x - self.step
        if self.direction == 2:
            self.y = self.y - self.step
        if self.direction == 3:
            self.y = self.y + self.step

    def right(self):
        self.direction = 0

    def left(self):
        self.direction = 1

    def up(self):
        self.direction = 2

    def down(self):
        self.direction = 3

class Food:

    def __init__(self, window_w, window_h):
        self.random_x = 120
        self.random_y = 120


    def set(self):
        self.random_x = random.randint(0, window_w - self.apple_w )
        self.random_y = random.randint(0, window_h - self.apple_h )

    def apple(self, window):
        self.apple_w = 12
        self.apple_h = 12
        pygame.draw.rect(
            window, 
            (250, 250, 200), 
            (
                self.random_x, 
                self.random_y, 
                self.apple_w,
                self.apple_h
            ))


class App:
    player = None
    level = 2


    def __init__(self, window_w, window_h):
        self.running = True
        self.windows = None
        self.player = Player()
        self.food = Food(window_w, window_h)
        self.window_h = window_h
        self.window_w = window_w
        self.snake_list = []

    def snake(self):
        pygame.draw.rect(
            self.window, 
            (250, 100, 0), 
            (
                self.player.x, 
                self.player.y, 
                self.player.width,
                self.player.height
            ))
    def snake_tail(self, x , y):
        pygame.draw.rect(
            self.window, 
            (180, 100, 0), 
            (
                x, 
                y, 
                self.player.width,
                self.player.height
            ))
    
    def scorring(self):
        self.font_path = "dir_path" + "\\" + "\\" + "AGENCYR.TTF"
        self.myfont = pygame.font.SysFont(self.font_path, 20)
        self.textsurface = self.myfont.render(f'Score: {self.player.score}', False, (250, 255, 255))
        self.window.blit(self.textsurface,(3,3))
    
    def frame(self):
        pygame.draw.rect(self.window, (20, 25, 100), (0, 0, self.window_w, self.window_h), 2)

    def on_init(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.window_w, self.window_h), pygame.HWSURFACE)
        pygame.display.set_caption("The Game")
        self.running = True
        self.snake()
        self.frame()
        self.scorring()
        pygame.display.flip()
        time.sleep(1)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        self.player.update()

    def clean(self):
        pygame.quit()

    def on_render(self):
        get_apple = False
        self.window.fill((0,0,0))
        self.apple = self.food.apple(self.window)
        self.frame()
        self.snake()
        self.snake_list.append([self.player.x, self.player.y])
        self.scorring()
        for i in self.snake_list[-self.player.length:]:
            self.snake_tail(i[0], i[1])

        snake_x_center = self.player.x + (self.player.width/2)
        snake_y_center = self.player.y + (self.player.height/2)

        if self.food.random_x <= snake_x_center <= (self.food.random_x + self.food.apple_w) and \
            self.food.random_y <= snake_y_center <= (self.food.random_y + self.food.apple_h):
            get_apple = True 
     
        if get_apple:
            self.player.score += 1
            self.player.length += 2
            self.food.set()
            get_apple = False
        pygame.display.flip()

    def on_execute(self):
        self.on_init()
        if self.on_init == False:
            self.running = False
        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                self.player.right()

            if keys[pygame.K_LEFT]:

                self.player.left()

            if keys[pygame.K_UP]:
                self.player.up()

            if keys[pygame.K_DOWN]:
                self.player.down()

            if (keys[pygame.K_ESCAPE]):
                self.running = False

            if (keys[pygame.K_a]):
                self.player.width = 70
            if 0 <= self.player.x <= self.window_w - self.player.width  and \
                0 <= self.player.y <= self.window_h - self.player.height: 
                self.on_loop()
                self.on_render()
            else:
                self.running = False
            
            time.sleep((1.0 / 10.0)/self.level)

        self.clean()


if __name__ == "__main__":
    theApp = App(window_w, window_h)
    theApp.on_execute()
