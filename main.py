
import sys, pygame


SIZE = 20
speed = 5
GRAVITY = 5
WHITE = (255, 255, 255)
BLUE= (0,0,255)

class Platform:
    def __init__(self, x, y, w, h, screen, game):
        self.x = x
        self.y = y
        self.screen = screen
        self.game = game
        self.w = w
        self.h = h
        self.acc = 1
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.hitbox = pygame.Rect(self.x - 4, self.y - 4, self.w + 8, self.h + 8)

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.w , self.h ))
        pygame.draw.rect(self.screen, BLUE, (self.x , self.y+ 25, self.w, self.h / 2), 1)




class Player:
    def __init__(self, x, y, w, h,screen, game):
        self.x = x
        self.game =game
        self.y = y
        self.screen = screen
        self.w = w
        self.h = h
        self.acc = 1
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.hitbox = pygame.Rect(self.x - 4, self.y - 4, self.w +8, self.h+8)

    def draw(self):
        self.draw_char()
        pygame.draw.rect(self.screen, (0, 0, 255), (self.x - 4, self.y-4, self.w + 8, self.h+ 8), 1)

    def draw_char(self):
        pygame.draw.rect(self.screen, (125, 125, 125), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(self.screen, WHITE, (self.x + 12, self.y + 4, 4, 4))
        pygame.draw.rect(self.screen,WHITE, (self.x + 4, self.y + 4, 4, 4))

    def move(self, axis, vector):
        if not self.hitbox.colliderect(self.game.platform.hitbox):
            if axis == "x":
                self.speed = self.speed + self.acc
                self.x = self.x + vector * speed
            elif axis == "y":
                self.speed = self.speed + self.acc
                self.y = self.y + vector * speed


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("arcade_skeleton")

        self.char = Player(400, 300, 20, 40, self.screen, self)
        self.platform = Platform(0, 550, 800, 200, self.screen, self)

    def event(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]:
            self.char.move("x", -1)
        elif keys[pygame.K_RIGHT]:
            self.char.move("x", 1)
        elif keys[pygame.K_UP]:
            self.char.move("y", -1)
        elif keys[pygame.K_DOWN]:
            self.char.move("y", 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def draw(self):
        self.platform.draw()
        self.char.draw()


    def update(self):
        ##self.char.update(self)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))

    def run(self):
        while True:
            self.clock.tick(60)
            self.draw()
            self.event()
            self.update()

game = Game()
game.run()
    

