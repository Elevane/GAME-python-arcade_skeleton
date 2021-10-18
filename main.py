
import sys, pygame


SIZE = 20
speed = 5
GRAVITY = 5


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("arcade_skeleton")
        self.x = 400
        self.y = 300
        self.movex = 0
        self.vel = pygame.Vector2(0, 0)
        self.acc = 1
        self.speed = 5
        self.jumpspeed = 50
        self.jumping = False

    def event(self):
        
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]: 
            self.move(-1)
        if keys[pygame.K_RIGHT]:
            self.move(1)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jumping = True
                    self.jump()
                elif not event.key == pygame.K_SPACE:
                    self.jumping = False

                    
    def jump(self):
        if not self.rect.colliderect(self.char):
            self.vel.y = -20

    def move(self, vector):     
        if self.rect.colliderect(self.char):
            if self.acc < 5:
                self.acc = self.acc + 0.5
            self.speed = self.speed + self.acc
            self.x = self.x + vector * speed
        

    def draw(self):
        self.char = pygame.draw.rect(self.screen, (125,125,125), (self.x, self.y, 20, 40))
        self.rect = pygame.draw.rect(self.screen, (255,255,255), (0, 550, 800,200))

    def update(self):
        if not self.rect.colliderect(self.char) and not self.jumping:
            self.y = self.y + self.speed + self.acc
            self.acc = self.acc + 0.5
        else :
            self.acc = 0
        pygame.display.flip()
        
    def run(self):
        while True:
            self.clock.tick(60) 
            self.screen.fill((0,0,0))
            self.draw()
            self.update()
            self.event()


game = Game()
game.run()
    

