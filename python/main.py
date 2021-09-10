"""
    Detta python script är spelet pong...

"""

import pygame, sys

class Player():
    def __init__(self):
        self.yPos = 0

    def getPos(self):
        return self.yPos

class Ball(pygame.sprite.Sprite):

        def __init__(self, xPos, yPos, width, height, screen):
            pygame.sprite.Sprite.__init__(self)

            self.xPos = xPos
            self.yPos = yPos
            self.width = width
            self.height = height
                
            self.color = (255,255,255)


            # Create an image of the block, and fill it with a color.
            # This could also be an image loaded from the disk.
            self.surface = pygame.Surface([self.width, self.height])
            self.image = self.surface
            self.image.fill(self.color)

            # Fetch the rectangle object that has the dimensions of the image
            # Update the position of this object by setting the values of rect.x and rect.y
            self.rect = self.image.get_rect()

        def getSurface(self):
            return self.surface

    
class Board():
    """
        - "Boarden" Består av 2 spelare och en boll
        - Ritar ut sträcket i mitten som avskiljar spelarna och texten
    """
    def __init__(self):
        self.background_color = 0,0,0
        
        # TESTING
        self.black = 0, 0, 0
        self.ball = pygame.image.load("test.gif")
        self.ballrect = self.ball.get_rect()

        # Sätter "tickspeeden" på spelet


    def update(self):
        self.screen.fill(self.black)

    def draw(self):
        pass

    def run(self):
        pass

class Game():

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.running = True

        pygame.init()
        pygame.display.set_caption("PONG")
        self.clock = pygame.time.Clock()

        self.running = True

        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)

        # Sätter "tickspeeden" på spelet
        self.clock.tick(60)

    def run(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    continue
            
            self.redraw()
        

    def redraw(self):
        # ball.update()
        # player1.update()
        # player2.update()
        pass

x = Game(1200, 500)
x.run()