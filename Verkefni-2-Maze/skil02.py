# Atli Óskarsson
# Skilaverkefni 2

import os
import random
import pygame
pygame.font.init()


font = pygame.font.SysFont("Calibri", 15)
# Class for the orange dude
class Player(object):

    def __init__(self, antibombcount = 0, defusedBombs = 0):
        self.rect = pygame.Rect(16, 16, 16, 16)
        self.defusedBombs = defusedBombs
        self.antibombcount = antibombcount

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def anti(self):
        return self.antibombcount

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy


        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                   # print("Left")
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                   # print("Right")
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                   # print("Top")
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                   # print("Bottom")

        for bomb in bombs:
            if self.rect.colliderect(bomb.rect):
                if self.antibombcount >= 1:
                    print(self.antibombcount)
                    if dx > 0:  # Moving right; Hit the left side of the wall
                        self.rect.right = bomb.rect.left
                        bombs.remove(bomb)
                        self.defusedBombs -= 1
                        self.antibombcount -= 1
                    if dx < 0:  # Moving left; Hit the right side of the wall
                        self.rect.left = bomb.rect.right
                        bombs.remove(bomb)
                        self.defusedBombs += 1
                        self.antibombcount -= 1
                    if dy > 0:  # Moving down; Hit the top side of the wall
                        self.rect.bottom = bomb.rect.top
                        bombs.remove(bomb)
                        self.defusedBombs += 1
                        self.antibombcount -= 1
                    if dy < 0:  # Moving up; Hit the bottom side of the wall
                        self.rect.top = bomb.rect.bottom
                        bombs.remove(bomb)
                        self.defusedBombs += 1
                        self.antibombcount -= 1
                else:
                    print(bomb)
                    raise SystemExit("You hit something")

                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = bomb.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = bomb.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = bomb.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = bomb.rect.bottom

        for antibomb in antibombs:
            if self.rect.colliderect(antibomb.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.antibombcount+=1
                    antibombs.remove(antibomb)
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.antibombcount+=1
                    antibombs.remove(antibomb)
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.antibombcount+=1
                    antibombs.remove(antibomb)
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.antibombcount+=1
                    antibombs.remove(antibomb)



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

class Entrance(object):

    def __init__(self, pos):
        entranceExit.append(self)
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
entranceExit = []
player = Player()  # Create the player

counter = 0
count = 0

# Holds the level layout in a list of strings.
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W WA      W     AAAAA                         WW           W",
    "W WWWBWBWBWWWWWWWWWWW WWWWWWWWWWWWWWWWWWWWWWWBWWBWWWWWWWWWBW",
    "WA    W W         AAW W                          W         W",
    "WBWWWWW WWWWWWBWWWWWWBWBWWWWWWWWWWWWWWWWWWWWWWWWWW WWWWWBWWW",
    "W W       W           W W                        W   W   W W",
    "W WWWWWWWWWBWWWWWWBWWWW W WWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W",
    "W W      AW W    W W  W   W       AW        W   W   W  W   W",
    "W W WWWWWWW W WW W W WWWWWW WWWWWWWW WWWWWW W W W W W WWWW W",
    "W W         W WW W W W      W        W        W   W W    W W",
    "W WWW WWWWWWW W  W W W WWW  W WWWW WWW WWWWWWWWWWWW WWWWBW W",
    "W W   W       WWWW W W W WWWW WW   W    W W   W   W    W W W",
    "W W WWW WWWWWWW    W W W       W WWW WWWW W W W W W WWWW W W",
    "W W W   W       WWWW W W WWWWW W W   WAA    W W W   W    W W",
    "W W W WWW WWWWWWW    B W     W W WWWWWWWWWWWW W WWWWW WWWW W",
    "W W W  W  W       WWWWWWWWWW W W              W   AAW    W W",
    "W W WW WBWW WWWWWWW          W W WWWWWWWWWWWWWWWWWWWWWWW WWW",
    "W        WW W     W WWWWWWWWWW W W  BW  BW   W   W   W   W W",
    "W WWWWWBWW  W WWWWW W          W   W   W   W   W   W   W   W",
    "W W     WW WW W AAW WBWWWWBWWWWWWWWWWWWWWW WWWWWWWWWWWWWWWWW",
    "W W WWWWW  W  W W W W W  W WAA           W W               W",
    "W W W     WW WWBWWWWW WW W WWWWWWWWWWWWW W W WWWWWWWWWWWW BW",
    "W   W WWWWWA W           W               W   WAA        W  W",
    "W W WBWW     WBWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W  W",
    "W W      WWW W        W         W           W         W WB W",
    "W WWWWWWWW W WWWWWWWWBW WWWWWWW W WWWWWWWWW W WWWWWWWWW W  W",
    "W W        B W        W W       W W         W W       W W  W",
    "W   WWWWWWWWWWBWWWWWWWW WWWWWWWWW W WWWWWWWWW W WWWWW W W BW",
    "W WWW   W W    W        W         W           W W W W W W  W",
    "W B W W   W WWWW WWWW WWWWW WWWWWWWWWWWWWWWWWWW W W W      W",
    "W W W WWW W W    W          W       B         WWWWWWWWWWWWWW",
    "W W W   W   W WWWWWWWWWWWWWWW WWWWWWWWWWWWWWW              W",
    "W W WWW WWW W   W           W               WWWWWWWWWWWWWW W",
    "W W W  AW   WWW W WWWWWWWWWWWWWWWWWWWWWWWWW              W W",
    "W W W WWWWW   W W W                       WWWWWWWWWWWWWW W W",
    "W WAW     WWW W W W WWWWWWWWWWWWWWWWWWWWW              W W W",
    "W WWWWWWW W W W   W W   W              WWWWWWWWWWWWWWWWW W W",
    "W W     W W W W WWW W W W WWWWWWWWWWWW                   W W",
    "W WWWWW W W W W W W W WWW W          WWWWWWWWWWWWWWWWWWWWW W",
    "W W   W W W   W                      W                   W W",
    "W W W W W WWWWWWWWWWWWWWWWWWWWWWWWWWWW WWWWWW WWWWWWWWWWWW W",
    "W W W W W               W            W      W W   W   W    W",
    "W WWW W WWWWWWWWWWWWWWW WWWWWWWWWWWWWWWWWWW W W W W W W W WW",
    "W     W                                     W   W   W   W  E",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",

]

# Parse the level string above. W = wall, B = bomb, A = AntiBomb, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            endakubbur = pygame.Rect(x, y, 16, 16)
        if col == "B":
            Bomb((x, y))
        if col == "A":
            AntiBomb((x, y))
        if col == "X":
            Entrance((x, y))
        x += 16
    y += 16
    x = 0

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
    if key[pygame.K_a]:
        player.move(-1,0)
    if key[pygame.K_d]:
        player.move(1, 0)
    if key[pygame.K_w]:
        player.move(0, -1)
    if key[pygame.K_s]:
        player.move(0, 1)


    # If Player hits the end
    if player.rect.colliderect(endakubbur):
        raise SystemExit("You Win!")

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (209, 209, 209), wall.rect)
    for bomb in bombs:
        pygame.draw.rect(screen, (255,0,255), bomb.rect)
    for antibomb in antibombs:
        pygame.draw.rect(screen, (50,150,120), antibomb.rect)
    for exit in entranceExit:
        pygame.draw.rect(screen, (248, 64, 12), exit.rect)

    pygame.draw.rect(screen, (0, 255, 255), endakubbur)

    # Takes from antibombcounts in the class Player
    if player.antibombcount >= 1:
        pygame.draw.rect(screen, (186, 188, 47), player.rect)
    else:
        pygame.draw.rect(screen, (255, 200, 0), player.rect)

    playersbombs = font.render(str(player.antibombcount), True, (0,0,0))
    screen.blit(playersbombs, player.rect)

    time = font.render("Seconds: " + str(count), True, (0,0,0))
    screen.blit(time, (0,0))

    counterOfBombs = font.render("Bombs: " + str(len(bombs)), True, (0,0,0))
    screen.blit(counterOfBombs, (100, 0))

    counterOfAntiBombs = font.render("Anti-bombs left: " + str(len(antibombs)), True, (0,0,0))
    screen.blit(counterOfAntiBombs, (200, 0))



    counter += 1
    if counter % 60 == 0:
        count += 1

    pygame.display.flip()