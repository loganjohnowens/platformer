import pygame
import sys
import time
from pictures import import_sprites


def make_screen():
    global screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("platformer")
    screen.fill((0, 0, 0))


def movemnt():
    global image
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pos[0] += 1
    if keys[pygame.K_a]:
        pos[0] -= 1
    if keys[pygame.K_s]:
        crouch = True
    if keys[pygame.K_w]:
        jump = True
    image = 0
    if keys[pygame.K_d]:
        image = 1
    if keys[pygame.K_a]:
        image = 2
    screen.blit(images[image], (pos[0], pos[1]))


def gravity():
    pos[1] += 1


def ground(ground_pos, size):
    global pos
    if pos[0] > ground_pos[0] and pos[0] < ground_pos[0] + size[0] and pos[1] == ground_pos[1] - 121:
        pos[1] -= 1
    if pos[0] + 50 > ground_pos[0] and pos[0] + 50 < ground_pos[0] + size[0] and pos[1] == ground_pos[1] - 121:
        pos[1] -= 1
    screen.blit(images[3], (ground_pos[0] + 1, ground_pos[1]))
    number = 0
    while number < size[0] - 18:
        number += 18
        screen.blit(images[5], (ground_pos[0] + number, ground_pos[1]))
    screen.blit(images[4], (ground_pos[0] + number + 11, ground_pos[1]))


def level():
    global level_number
    if level_number == 1:
        ground([-1, 200,], [300, 10])


level_number = 1
image = 0
pos = [0, 0]
pygame.init()
make_screen()
images = import_sprites()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    level()
    movemnt()
    gravity()
    pygame.display.flip()
    time.sleep(.001)
