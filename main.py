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
    global jump
    global crouch
    global jump_time
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pos[0] += 1
    if keys[pygame.K_a]:
        pos[0] -= 1
    if keys[pygame.K_w] and on_ground is True:
        jump = True
    image = 0
    if keys[pygame.K_d]:
        image = 1
    if keys[pygame.K_a]:
        image = 2
    if keys[pygame.K_s]:
        image = 6
    if keys[pygame.K_s] and keys[pygame.K_a]:
        image = 7
    if keys[pygame.K_s] and keys[pygame.K_d]:
        image = 8
    if keys[pygame.K_s] is not True:
        screen.blit(images[image], (pos[0], pos[1]))
    if keys[pygame.K_s]:
        screen.blit(images[image], (pos[0], pos[1] + 52))


def gravity():
    pos[1] += 1


def ground(ground_pos, size):
    global pos
    global on_ground
    if on_ground is not True:
        on_ground = False
    if pos[0] > ground_pos[0] and pos[0] < ground_pos[0] + size[0] and pos[1] == ground_pos[1] - 121:
        pos[1] -= 1
        on_ground = True
    if pos[0] + 50 > ground_pos[0] and pos[0] + 50 < ground_pos[0] + size[0] and pos[1] == ground_pos[1] - 121:
        pos[1] -= 1
        on_ground = True
    screen.blit(images[3], (ground_pos[0] + 1, ground_pos[1]))
    number = 0
    while number < size[0] - 18:
        number += 18
        screen.blit(images[5], (ground_pos[0] + number, ground_pos[1]))
    screen.blit(images[4], (ground_pos[0] + number, ground_pos[1] - 2))


def level():
    global level_number
    global sub_level_number
    global on_ground
    on_ground = False
    if level_number == 1:
        backround(9)
        if sub_level_number == 1:
            screen.blit(images[10], (310, 150))
            ground([-1, 200,], [300, 10])
            ground([300, 340,], [480, 10])
        if sub_level_number == 2:
            screen.blit(images[11], (310, 50))
            text_maker(['I want to go out side.', 'one day', ''])
            ground([-1, 200], [150, 0])
            ground([149, 450], [650, 0])


def jumping():
    global jump
    global jump_time
    jump_height = 10
    if jump:
        if jump_time < 20:
            pos[1] -= jump_height - (jump_time * 0.5)
            jump_time += 1
        else:
            jump = False
            jump_time = 0


def backround(number):
    screen.blit(images[number], (0, 0))


def make_exit_butten_work():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def update_and_time():
    pygame.display.flip()
    time.sleep(.001)


def level_updating():
    global pos
    global sub_level_number
    global sub_level_spawn
    if pos[0] > 799:
        sub_level_number += 1
        pos = sub_level_spawn[sub_level_number - 1]


def text_maker(lines):
    global pos
    screen.blit(images[12], (pos[0], pos[1] - 50))
    font = pygame.font.Font(None, 15)
    line_height = font.get_height() + 5  # Add a bit of spacing between lines

    for index, words in enumerate(lines):
        text_surface = font.render(words, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(pos[0] + 60, pos[1] - 20 + index * line_height))
        screen.blit(text_surface, text_rect)


level_number = 1
sub_level_number = 2
sub_level_spawn = [[-1, 0], [-1, 50]]
image = 0
pos = [0, 0]
jump = False
crouch = False
on_ground = True
jump_time = 0
pygame.init()
make_screen()
images = import_sprites()
while True:
    make_exit_butten_work()
    level()
    movemnt()
    jumping()
    gravity()
    level_updating()
    update_and_time()
