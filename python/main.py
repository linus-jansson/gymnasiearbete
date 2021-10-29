#!/usr/bin/python3
import pygame, sys, time, os
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

        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed 
    

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
        self.xPos = x
        self.yPos = y
        self.yAcceleration = 0
        self.score = 0
        self.width = width
        self.height = height

        self.obj = pygame.Rect((self.xPos, self.yPos), (self.width, self.height))
        

        self.velocity = 0
        self.friction = 0.001

        self.show()

    def show(self):
        self.obj = pygame.draw.rect(self.screen, self.color, (self.xPos, self.yPos, self.width, self.height))
    
    def update(self, dt):

        if abs(self.velocity) > 1:
            self.yAcceleration = 0

        self.velocity += self.yAcceleration * dt

        self.yPos += self.velocity * dt

        if abs(self.velocity) <= self.friction:
            self.velocity = 0
        else:

            if self.velocity >= 0:
                self.velocity -= self.friction * dt
            else:
                self.velocity += self.friction * dt


        

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
        self.acceleration_constant = 0.001


    def middle(self, k):
        return k // 2

    def draw_board(self):
        pygame.draw.line(self.screen, self.WHITE, (self.WIDTH//2, 0), (self.WIDTH//2, self.HEIGHT), 5) # middle line

        self.p1_score_surface = self.font.render(str(self.paddle1.score), False, self.WHITE)
        self.screen.blit(self.p1_score_surface, (self.middle(self.middle(self.WIDTH)), 10)) ## middle(middle(Width)) popega

        self.p2_score_surface = self.font.render(str(self.paddle2.score), False, self.WHITE)
        self.screen.blit(self.p2_score_surface, (self.middle(self.WIDTH) + self.middle(self.WIDTH) // 2, 10))

    def update(self):
        self.screen.fill(self.BLACK)

        self.draw_board()

        self.ball.show()

        self.paddle1.show()
        self.paddle2.show()

    def print_DEBUG(self, info):
            os.system("clear")
            it = 0
            for key, val in info.items():
                if  it == 0 or it == 4 or it == 8:
                    print('='*5)
                print(f"{key}: {val}")
                
                it += 1
                

            print(end="\n\n")


    def run(self):
        while self.running:
                                
                self.dt = self.clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F11:
                            self.DEBUG = not self.DEBUG
                            print("DEBUG:", self.DEBUG)
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
            
                # Om x positionen på bollen är större eller lika med bredden
                # Om x positionen på bollen är mindre eller lika med bredden
                if self.ball.x >= self.WIDTH or self.ball.x <= 0:
                    self.ball.reset()

                if self.ball.y >= self.HEIGHT:
                    self.ball.y = self.HEIGHT - self.ball.radius
                    self.ball.direction[1] = -self.ball.direction[1]

                # Om y positionen på bollen är mindre eller lika med bredden
                if self.ball.y <= 0:
                    self.ball.y = self.ball.radius
                    self.ball.direction[1] = -self.ball.direction[1]


                # Hämtar status på alla knappar
                key=pygame.key.get_pressed()

                # Kommer bli -1, 0, eller 1 vilket kommer orsaka att paddeln åker upp eller ner
                # Hanterar vilket håll som paddlarna åker åt
                if (key[pygame.K_s] - key[pygame.K_w] == 1):
                    self.paddle1.yAcceleration += self.acceleration_constant

                elif (key[pygame.K_s] - key[pygame.K_w] == -1):
                    self.paddle1.yAcceleration -= self.acceleration_constant               
                else:
                    self.paddle1.yAcceleration = 0
                

                if (key[pygame.K_DOWN] - key[pygame.K_UP] == 1):
                    self.paddle2.yAcceleration += self.acceleration_constant 
                elif (key[pygame.K_DOWN] - key[pygame.K_UP] == -1):
                    self.paddle2.yAcceleration -= self.acceleration_constant      
                else:
                    self.paddle2.yAcceleration = 0


                # if (self.y + newY) > screen.width: 
                # Kontrollerar så att inte spelaren hamnar utanför boxen
                if self.paddle1.yPos >= self.HEIGHT - self.paddle1.height:
                    self.paddle1.yPos = self.HEIGHT - self.paddle1.height
                
                if self.paddle1.yPos < 0:
                    self.paddle1.yPos = 0
                
                else:
                    self.paddle1.update(self.dt)

                if self.paddle2.yPos >= self.HEIGHT - self.paddle2.height:
                    self.paddle2.yPos = self.HEIGHT - self.paddle2.height
                
                if self.paddle2.yPos < 0:
                    self.paddle2.yPos = 0
                
                else:
                    self.paddle2.update(self.dt)

                
                self.ball.update(self.dt) # Updates ball position

                # Kollar ifall bollen kolliderar med någon av paddlarna
                if (self.ball.collide(self.paddle1.getObj()) != 0 or self.ball.collide(self.paddle2.getObj()) != 0):
                    
                    self.ball.direction[0] *= -1
                    self.ball.speed *= 1.05
                    

                if self.ball.x >= self.WIDTH:
                    self.paddle1.score += 1
                elif self.ball.x <= 0:
                    self.paddle2.score += 1
                
                self.update()
        
                if self.DEBUG: 
                    info = {
                        "player1": "",
                        "Velocity": self.paddle1.velocity,
                        "Acceleration": self.paddle1.yAcceleration,
                        "KeyDown": (key[pygame.K_s] - key[pygame.K_w]),
                        "player2": "",
                        "Velocity2": self.paddle2.velocity,
                        "Acceleration2": self.paddle2.yAcceleration,
                        "KeyDown2": (key[pygame.K_DOWN] - key[pygame.K_UP])
                    }

                    self.print_DEBUG(info)
                
                pygame.display.update()



if __name__ == "__main__":

    gameInstance = Game(1080, 720)

    gameInstance.run()