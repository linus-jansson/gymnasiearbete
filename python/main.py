import pygame, sys

    
class player:
    def __init__(self):
        self.yPos = 0

    def getPos(self):
        return self.yPos

class Pong:

    def __init__(self, w, h):
        pygame.init()

        self.running = True

        self.size = (w, h)
        self.screen = pygame.display.set_mode(self.size)
        
        # Sätter "tickspeeden"
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        pygame.display.set_caption("PONG")
    
    def update(self):
        pass

    def run(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    continue

            self.update()

            # self.screen.fill(0,0,0)
            

x = Pong(800, 600)
x.run()