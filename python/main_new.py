import pygame, sys, time


class Ball:
    def __init__(self, screen, color, x, y, radius):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.show()

        self.xSpeed = -1
        self.ySpeed = 0

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


    def update(self):
        print((self.x, WIDTH), (self.y, HEIGHT))
        # Om x positionen på bollen är större eller lika med bredden
        if self.x >= WIDTH and self.xSpeed == 1:
            self.x = WIDTH - self.radius
            self.xSpeed = -1
            print(self.xSpeed)

        if self.x <= WIDTH and self.xSpeed == -1:
            self.x = self.radius
            self.xSpeed = 1
            print(self.xSpeed)


        self.x += self.xSpeed
        self.y += self.ySpeed
    
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

class Paddle:
    def __init__(self, screen, color, x, y, width, height):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.show()

    
    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self, newX, newY):
        # if (self.y + newY) > screen.width: 
        pygame.draw.rect(self.screen, self.color, (self.x, self.y + newY, self.width, self.height))

        self.y += newY

        

pygame.init()

WIDTH = 900
HEIGHT = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

clock.tick(30)


def mid_line():
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)
    

ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2 , 15)
paddle1 = Paddle(screen, WHITE, 15, HEIGHT//2 - 60, 20, 120)
paddle2 = Paddle( screen, WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120 )

def game_update():
    screen.fill(BLACK)
    ball.update()
    paddle1.update(0, 0)
    paddle2.update(0, 0)
    mid_line()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    time.sleep(0.01)
    game_update()

    pygame.display.update()
