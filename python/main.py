"""
    Detta python script är spelet pong...

"""

import pygame, sys

class Sprite():
    def __init__(self, RGB, width, height):

        self.RGB = RGB

        self.xPos = 0
        self.yPos= 0

        self.width = width
        self.height = height
    def properties(self):
        print((self.xPos, self.yPos, self.width, self.height))
        return (self.xPos, self.yPos, self.width, self.height)

    def color(self):
        return self.RGB

class Ball(pygame.sprite.Sprite):

        def __init__(self, xPos, yPos, width, height):
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
        - Boarden ritas ut i spelet
    """
    def __init__(self):
        self.background_color = 0,0,0
        self.ball_pos = (0, 0)
        
        # # TESTING
        # self.black = 0, 0, 0
        # self.ball = pygame.image.load("test.gif")
        # self.ballrect = self.ball.get_rect()

        # Sätter "tickspeeden" på spelet


    def update(self):
        pass

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

        self.surface = pygame.Surface(self.size)
        self.screen = pygame.display.set_mode(self.size)

        self.ball = Sprite((255, 255, 255), 50, 50)

        self.rect = pygame.draw.rect(self.screen, self.ball.color(), self.ball.properties())
        # Sätter "tickspeeden" på spelet
        self.clock.tick(60)

    def run(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    continue
            
            self.ball.xPos += 1

            self.redraw()
        

    def redraw(self):
        pygame.display.update(self.rect)
        pygame.display.flip()
        #board.update()
        pass


def main():
    x = Game(1200, 500)
    x.run()


if __name__ == "__main__":
    main()