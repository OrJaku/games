import pygame
import time
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
          
class Player:
    x = 50
    y = 50
    direction = 0
    score = 0
    width = 10
    height = 10
    speed = 2

    def update(self):
        if self.direction == 0:
            self.x = self.x + self.speed
        if self.direction == 1:
            self.x = self.x - self.speed
        if self.direction == 2:
            self.y = self.y - self.speed
        if self.direction == 3:
            self.y = self.y + self.speed

    def right(self):
        self.direction = 0

    def left(self):
        self.direction = 1

    def up(self):
        self.direction = 2

    def down(self):
        self.direction = 3


class App:
    window_h = 300
    window_w = 400
    player = None
    level = 5
    pygame.font.init() 

    def __init__(self):
        self.running = True
        self.windows = None
        self.player = Player()

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
    def food(self):
        pygame.draw.rect(
            self.window, 
            (250, 250, 200), 
            (
                100, 
                200, 
                8,
                8
            ))

    def scorring(self):
        self.font_path = "dir_path" + "\\" + "\\" + "AGENCYR.TTF"
        self.myfont = pygame.font.SysFont(self.font_path, 20)
        self.textsurface = self.myfont.render(f'Score: {self.player.score}', False, (250, 255, 255))
        self.window.blit(self.textsurface,(0,0))

    def on_init(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.window_w, self.window_h), pygame.HWSURFACE)
        pygame.display.set_caption("The Game")
        self.running = True
        self.snake()
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
        self.window.fill((0,0,0))
        self.snake()
        self.scorring()
        self.food()
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
    theApp = App()
    theApp.on_execute()
