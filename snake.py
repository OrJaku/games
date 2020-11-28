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
    step = 12
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
        self.draw_lots_food = 0
        self.window = None
        self.apple_w = -1
        self.apple_h = -1        
        self.fish_w = -1
        self.fish_h = -1

    def set(self):
        self.random_x = random.randint(0, window_w - self.apple_w )
        self.random_y = random.randint(0, window_h - self.apple_h )
        self.draw_lots_food = random.randint(0,10)
        self.start_time = time.time()


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

    def fish(self, window):
        self.fish_w = 14
        self.fish_h = 14
        pygame.draw.rect(
            window, 
            (100, 50, 200), 
            (
                self.random_x, 
                self.random_y, 
                self.fish_w,
                self.fish_h
            ))


    def choose_food(self, window):
        if self.draw_lots_food >= 9:
            self.fish(window)
            self.put_fish = True
            self.put_apple = False
            food_kind = "fish"   
        else:
            self.apple(window)
            self.put_fish = False
            self.put_apple = True
            food_kind = "apple"
        return food_kind

class App:
    player = None
    level = 3

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
        time.sleep(0.5)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
 
    def on_loop(self):
        self.player.update()

    def clean(self):
        pygame.quit()

    def on_render(self):
        self.get_apple = False
        self.get_fish = False
        self.window.fill((0,0,0))
        self.snake_list.append([self.player.x, self.player.y])
        self.tail_length = self.snake_list[-self.player.length:-1]

        food_choose = self.food.choose_food(self.window)
        food_possition = [self.food.random_x, self.food.random_y]
        if food_possition in self.tail_length:
            self.food.set()

        if food_choose == "fish" and time.time() >= self.food.start_time + 6:
            self.food.set()
            self.food.choose_food(self.window)
            
        self.frame()
        self.snake()
        self.scorring()
        for i in self.tail_length:
            self.snake_tail(i[0], i[1])

        snake_x_center = self.player.x + (self.player.width/2)
        snake_y_center = self.player.y + (self.player.height/2)

        if self.food.random_x <= snake_x_center <= (self.food.random_x + self.food.apple_w) and \
            self.food.random_y <= snake_y_center <= (self.food.random_y + self.food.apple_h) and \
                self.food.put_apple:
            self.get_apple = True 

        if self.food.random_x <= snake_x_center <= (self.food.random_x + self.food.fish_w) and \
            self.food.random_y <= snake_y_center <= (self.food.random_y + self.food.fish_h) and \
                self.food.put_fish:
            self.get_fish = True 
     
        if self.get_apple:
            self.player.score += 1
            self.player.length += 1
            self.food.set()
            self.get_apple = False

        if self.get_fish:
            self.player.score += 3
            self.player.length += 3
            self.food.set()
            self.get_fish = False
        pygame.display.flip()

    def collision(self):
        self.snake_head_position = [self.player.x, self.player.y]
        if self.snake_head_position in self.tail_length:
            self.running = False
            print("COLLISION")
            print("Score: ", self.player.score)



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

            if 0 <= self.player.x <= self.window_w - self.player.width  and \
                0 <= self.player.y <= self.window_h - self.player.height: 
                self.on_loop()
                self.on_render()
            else:
                print("COLLISION")
                print("Score: ", self.player.score)
                self.running = False

            self.collision()
            time.sleep((1.0 / 4.0)/self.level)

        self.clean()


if __name__ == "__main__":
    theApp = App(window_w, window_h)
    theApp.on_execute()
