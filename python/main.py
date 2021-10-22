
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

        self.speed = 1

        self.direction = [randint(-5, 5), randint(-2, 2)]

        self.obj = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

        self.reset()
        self.show()



    def show(self):
        self.obj = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


    def reset(self):
        self.x = self.standardX
        self.y = self.standardY

        self.direction = [ -self.direction[0],  randint(-2, 2)]

        while self.direction[1] == 0:
            self.direction[1] = randint(-2, 2)

        self.speed = 1
        


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

# DÅLIGT MED GLOBALA VARIABLER
WIDTH = 1080
HEIGHT = 720

def middle(k):
    return k // 2

# GÖR OM TILL EN KLASS SEN
def main():

    pygame.init()
    running = True


    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    clock = pygame.time.Clock()


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG - Created by Linus, Vilhelm and Erik")



    def mid_line():
        pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)
        

    ball = Ball(screen, WHITE, middle(WIDTH), middle(HEIGHT) , 15)
    paddle1 = Paddle(screen, WHITE, 15, middle(HEIGHT) - 60, 20, 120)
    paddle2 = Paddle( screen, WHITE, WIDTH - 20 - 15, middle(HEIGHT) - 60, 20, 120 )

    DEBUG = False

    WHITE = (255, 255, 255)
    font = pygame.font.SysFont('Monospace', 50)
    main_menu = False


    # def game_update():
    #     pass
    while running:
        
        while main_menu:
            print(main_menu)

        p1_score_surface = font.render(str(paddle1.score), False, WHITE)
        p2_score_surface = font.render(str(paddle2.score), False, WHITE)
        dt = clock.tick(60)

        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    DEBUG = not DEBUG
                    print("DEBUG:", DEBUG)
                if event.key == pygame.K_ESCAPE:
                    running = False
       
       
        # Hämtar status på alla knappar
        key=pygame.key.get_pressed()

        # Kommer bli -1, 0, eller 1 vilket kommer orsaka att paddeln åker upp eller ner
        # Hanterar vilket håll som paddlarna åker åt
        paddle1.update((key[pygame.K_s] - key[pygame.K_w]) * dt)
        paddle2.update((key[pygame.K_DOWN] - key[pygame.K_UP]) *dt)
        ball.update(dt) # Updates ball position

        # Kollar ifall bollen kolliderar med någon av paddlarna
        if (ball.collide(paddle1.getObj()) != 0 or ball.collide(paddle2.getObj()) != 0):
            print("paddle collission")
            ball.direction[0] *= -1
            ball.speed *= 1.05

        if ball.x >= WIDTH:
            paddle1.incrementScore()
        elif ball.x <= 0:
            paddle2.incrementScore()

        mid_line()

        # time.sleep(0.01)

        screen.blit(p1_score_surface, (middle(middle(WIDTH)), 10))
        screen.blit(p2_score_surface, (middle(WIDTH) + middle(WIDTH) // 2, 10))

        pygame.display.update()

if __name__ == "__main__":
    main()      