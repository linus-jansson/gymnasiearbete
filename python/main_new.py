import pygame, sys, time
from random import randint

class Ball:
    def __init__(self, screen, color, x, y, radius):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.show()

        self.xSpeed = 1
        self.ySpeed = 1

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


    def update(self):
        # print((self.x, WIDTH), (self.y, HEIGHT))

        # Kolla om det finns något bättre sätt
        # Om x positionen på bollen är större eller lika med bredden
        if self.x >= WIDTH:
            self.x = WIDTH - self.radius
            self.xSpeed = -self.xSpeed

        # Om x positionen på bollen är mindre eller lika med bredden
        if self.x <= 0:
            self.x = self.radius
            self.xSpeed = -self.xSpeed

        if self.y >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.ySpeed = -self.ySpeed

        # Om x positionen på bollen är mindre eller lika med bredden
        if self.y <= 0:
            self.y = self.radius
            self.ySpeed = -self.ySpeed


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


        self.speed = 1

        self.show()

        self.r = pygame.Rect((self.x, self.y), (self.width, self.height))

    
    def show(self):
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    
    # def show(self):
    #     self.r = pygame.draw.rect(self.screen, self.color, self.r)



    def update(self, newY):
        # if (self.y + newY) > screen.width: 
        # Kontrollerar så att inte spelaren hamnar utanför boxen
        if self.y >= HEIGHT - self.height:
            self.y = HEIGHT - self.height
        if self.y < 0:
            self.y = 0
        else:
            self.y += newY

    def getRect(self):
        return self.r

    def collide(self, obj):
        return self.r.colliderect(obj)

class GameBoard: 
    # Defines the middle line, and scoreboard
    # varje gång det blir ett score så kör den update score funktionen
    def __init__(self, screen):
        pass

    def updateScore(self):
        pass
    



class Game: 

    def __init__(self, width, height, tickspeed):
        # Pygame init och settings
        pygame.init()
        pygame.display.set_caption("PONG")

        self.running = True

        self.WIDTH = width
        self.WIDTH_CENTER = self.WIDTH // 2
        self.HEIGHT = height
        self.HEIGHT_CENTER = self.WIDTH // 2
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.clock = pygame.time.Clock()

        self.clock.tick(tickspeed)

        self.DEBUG = False


        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        ball = Ball(self.screen, self.WHITE, self.WIDTH_CENTER, self.WIDTH_CENTER, 10)
        playerOne = Paddle(self.screen, self.WHITE, 15, HEIGHT//2 - 60, 20, 120)
        playerTwo = Paddle(self.screen, self.WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120 )
        # WIDTH - 20 - 15 ? ^^^


    def collide(self, O1, O2):
        pass

    def DEBUG(self):
        pass

    def run(self):
        while running:
            self.screen.fill(self.BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        DEBUG = not DEBUG
                        print("DEBUG:", DEBUG)
            
            if DEBUG:
                DEBUG()
            # Hämtar status på alla knappar
            key=pygame.key.get_pressed()

            # time.sleep(0.01)


            pygame.display.update()


# DÅLIGT MED GLOBALA VARIABLER
WIDTH = 1080
HEIGHT = 720

def main():

    pygame.init()
    running = True


    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    clock = pygame.time.Clock()


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG")



    def mid_line():
        pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)
        

    ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2 , 15)
    paddle1 = Paddle(screen, WHITE, 15, HEIGHT//2 - 60, 20, 120)
    paddle2 = Paddle( screen, WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120 )

    DEBUG = False

    # def game_update():
    #     pass
    while running:
        dt = clock.tick(500)

        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    DEBUG = not DEBUG
                    print("DEBUG:", DEBUG)
                
        # Hämtar status på alla knappar
        key=pygame.key.get_pressed()

        # Kommer bli -1, 0, eller 1 vilket kommer orsaka att paddeln åker upp eller ner
        paddle1.update((key[pygame.K_s] - key[pygame.K_w]) * dt)
        paddle2.update((key[pygame.K_DOWN] - key[pygame.K_UP]) *dt)


        ball.update()

        # print(paddle1.collide(ball.getRect()))
        # print(paddle2.collide(ball.getRect()))


        paddle1.show()
        paddle2.show()

        mid_line()

        # time.sleep(0.01)


        pygame.display.update()

if __name__ == "__main__":
    main()