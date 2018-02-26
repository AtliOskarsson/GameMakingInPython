# Atli Óskarsson
# Skilaverkefni 2

import os
import random
import pygame


# Class for the orange dude
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(16, 16, 16, 16)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

        for bomb in bomblocation:
            if self.rect.colliderect(bomb.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = bomb.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = bomb.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = bomb.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = bomb.rect.bottom


# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Bomb(object):

    def __init__(self,pos):
        bombs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class AntiBomb(object):

    def __init__(self, pos):
        antibombs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)




# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "300"
pygame.init()

# Set up the display
pygame.display.set_caption("Get out!                                                                                                                                                                                                                                                Now!")
screen = pygame.display.set_mode((960, 720))

clock = pygame.time.Clock()
walls = []  # List to hold the walls
bombs = []  # List to hold the bombs
antibombs = []
bomblocation = []
player = Player()  # Create the player

# Holds the level layout in a list of strings.
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                          W",
    "W WWWW    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WWWWWWWWWWWW W",
    "W                                                          W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                  B                                     W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                 B                      W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W A                                                        W",
    "W W                                                        W",
    "W W                     B                                  W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W W                                                        W",
    "W                                                          E",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",

]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            endakubbur = pygame.Rect(x, y, 16, 16)
        if col == "B":
            Bomb((x, y))
            bomblocation.append(pygame.Rect(x, y, 16, 16))
        if col == "A":
            AntiBomb((x, y))
        x += 16
    y += 16
    x = 0

print(bomblocation)
running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(endakubbur):
        raise SystemExit("You Win!")

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    for bomb in bombs:
        pygame.draw.rect(screen, (255,0,255), bomb.rect)
    for antibomb in antibombs:
        pygame.draw.rect(screen, (50,150,120), antibomb.rect)

    pygame.draw.rect(screen, (0, 255, 255), endakubbur)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.flip()