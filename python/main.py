
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

    def move(self):
        pass

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

# DÅLIGT MED GLOBALA VARIABLER


class Game():
    def __init__(self, w, h):
        pygame.init()
        self.running = True


        # CONSTANTS
        self.WIDTH = w
        self.HEIGHT = h

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font = pygame.font.SysFont('Monospace', 50)
        pygame.display.set_caption("PONG - Created by Linus, Vilhelm and Erik")

        

        self.ball = Ball(self.screen, self.WHITE, self.middle(self.WIDTH), self.middle(self.HEIGHT) , 15)
        
        self.paddle1 = Paddle(self.screen, self.WHITE, 15, self.middle(self.HEIGHT) - 60, 20, 120)
        self.paddle2 = Paddle(self.screen, self.WHITE, self.WIDTH - 20 - 15, self.middle(self.HEIGHT) - 60, 20, 120)

        self.DEBUG = False

        self.main_menu = False
        self.dt = 0


    def middle(self, k):
        return k // 2

    def draw_board(self):
        pygame.draw.line(self.screen, self.WHITE, (self.WIDTH//2, 0), (self.WIDTH//2, self.HEIGHT), 5) # middle line

        self.p1_score_surface = self.font.render(str(self.paddle1.score), False, self.WHITE)
        self.screen.blit(self.p1_score_surface, (self.middle(self.middle(WIDTH)), 10)) ## middle(middle(Width)) popega

        self.p2_score_surface = self.font.render(str(self.paddle2.score), False, self.WHITE)
        self.screen.blit(self.p2_score_surface, (self.middle(WIDTH) + self.middle(WIDTH) // 2, 10))

    def run(self):
        while self.running:
                                
                self.dt = self.clock.tick(60)

                self.screen.fill(self.BLACK)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F11:
                            self.DEBUG = not self.DEBUG
                            print("DEBUG:", self.DEBUG)
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
            
                # Hämtar status på alla knappar
                key=pygame.key.get_pressed()

                # Kommer bli -1, 0, eller 1 vilket kommer orsaka att paddeln åker upp eller ner
                # Hanterar vilket håll som paddlarna åker åt
                self.paddle1.update((key[pygame.K_s] - key[pygame.K_w]) * self.dt)
                self.paddle2.update((key[pygame.K_DOWN] - key[pygame.K_UP]) * self.dt)

                
                self.ball.update(self.dt) # Updates ball position

                # Kollar ifall bollen kolliderar med någon av paddlarna
                if (self.ball.collide(self.paddle1.getObj()) != 0 or self.ball.collide(self.paddle2.getObj()) != 0):
                    print("paddle collission")
                    self.ball.direction[0] *= -1
                    self.ball.speed *= 1.05

                if self.ball.x >= self.WIDTH:
                    self.paddle1.score += 1
                elif self.ball.x <= 0:
                    self.paddle2.score += 1

                self.draw_board()

                pygame.display.update()



if __name__ == "__main__":
    WIDTH = 1080
    HEIGHT = 720

    gameInstance = Game(WIDTH, HEIGHT)

    gameInstance.run()