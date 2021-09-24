
import pygame, sys, time
from random import randint

class Ball:
    def __init__(self, screen, color, x, y, radius):
        self.screen = screen
        self.color = color
        self.standardX = x
        self.standardY = y
        self.x = x
        self.y = y
        self.radius = radius
        self.xSpeed = 0
        self.ySpeed = 0

        self.speed = 2

        self.direction = [randint(-5, 5), randint(-2, 2)]

        self.obj = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

        self.reset()
        self.show()



    def show(self):
        self.obj = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


    def reset(self):
        self.x = self.standardX
        self.y = self.standardY

        self.direction = [ -self.direction[0],  randint(-5, 5)]

        # Ser till så att direction antingen x eller y aldrig är 0
        for count, dire in enumerate(self.direction):
            while dire == 0:
                print(dire)
                dire = randint(-5, 5)
                self.direction[count] = dire

        self.speed = 2
        


    def update(self, dt):
        # Om x positionen på bollen är större eller lika med bredden
        # Om x positionen på bollen är mindre eller lika med bredden
        if self.x >= WIDTH or self.x <= 0:
            self.reset()
            # time.sleep(0.5)
            

        if self.y >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.direction[1] = -self.direction[1]

        # Om y positionen på bollen är mindre eller lika med bredden
        if self.y <= 0:
            self.y = self.radius
            self.direction[1] = -self.direction[1]


        self.x += self.direction[0] * self.speed 
        self.y += self.direction[1] * self.speed 
    
        self.show()

    def getObj(self):
        return self.obj
    
    def collide(self, obj2):
        return self.obj.colliderect(obj2)

class Paddle:
    def __init__(self, screen, color, x, y, width, height):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.score = 0
        self.width = width
        self.height = height
        self.obj = pygame.Rect((self.x, self.y), (self.width, self.height))

        self.speed = 1

        self.show()

    # def show(self):
    #     self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    
    def show(self):
        self.obj = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self, newY):
        # if (self.y + newY) > screen.width: 
        # Kontrollerar så att inte spelaren hamnar utanför boxen
        if self.y >= HEIGHT - self.height:
            self.y = HEIGHT - self.height
        if self.y < 0:
            self.y = 0
        else:
            self.y += newY

        self.show()

    def getObj(self):
        return self.obj

    def collide(self, obj2):
        return self.obj.colliderect(obj2)

    def incrementScore(self):
        self.score += 1
        return self.score

class GameBoard: 
    # Defines the middle line, and scoreboard
    # varje gång det blir ett score så kör den update score funktionen
    def __init__(self, screen):
        self.p1_score = 0
        self.p2_score = 0
        self.WHITE = (255, 255, 255)
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = self.myfont.render(str("scoreA"), 1, self.WHITE)
        self.screen.blit(self.text, (250,10))
        self.text = self.myfont.render(str("scoreB"), 1, self.WHITE)
        self.screen.blit(self.text, (420,10))

    def updateScore(self):
        if self.x >= WIDTH:
            self.p1_score += 1
        elif self.x <= 0:
            self.p2_score += 1
    
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
        dt = clock.tick(60)

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

        # print(paddle1.getObj(), paddle2.getObj())
        if (ball.collide(paddle1.getObj()) != 0 or ball.collide(paddle2.getObj()) != 0):
            print("paddle collission")
            ball.direction[0] *= -1
            ball.speed *= 1.05

        ball.update(dt)

        mid_line()

        # time.sleep(0.01)


        pygame.display.update()

if __name__ == "__main__":
    main()      