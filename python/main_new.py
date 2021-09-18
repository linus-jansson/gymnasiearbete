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
        if self.x >= WIDTH:
            self.x = WIDTH - self.radius
            self.xSpeed = -1

        # Om x positionen på bollen är mindre eller lika med bredden
        if self.x <= 0:
            self.x = self.radius
            self.xSpeed = 1

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

    def update(self, newY):
        # if (self.y + newY) > screen.width: 
        self.y += newY



        

pygame.init()
running = True
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

DEBUG = False

def game_update():
    pass

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass
            # if key[pygame.K_UP]:
            #     paddle1.update(-1)
            #     paddle2.update(-1)
            # if key[pygame.K_DOWN]:
            #     paddle1.update(1)
            #     paddle2.update(1)
    
    key=pygame.key.get_pressed()


    paddle1.update(key[pygame.K_DOWN] - key[pygame.K_UP])
    paddle2.update(key[pygame.K_DOWN] - key[pygame.K_UP])


    ball.update()
    paddle1.show()
    paddle2.show()

    mid_line()

    # time.sleep(0.01)


    pygame.display.update()
