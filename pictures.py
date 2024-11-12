import pygame
import os
image = []


def import_sprites():
    image.append(pygame.image.load(os.path.join("images", "main_guy_standing.png")).convert_alpha())
    image[0] = pygame.transform.scale(image[0], (200, 200))
    image.append(pygame.image.load(os.path.join("images", "main_guy_walking_right.png")).convert_alpha())
    image[1] = pygame.transform.scale(image[1], (200, 200))
    image.append(pygame.image.load(os.path.join("images", "main_guy_walking_left.png")).convert_alpha())
    image[2] = pygame.transform.scale(image[2], (200, 200))
    image.append(pygame.image.load(os.path.join("images", "left_side_of_ground.png")).convert_alpha())
    image[3] = pygame.transform.scale(image[3], (200, 200))
    image.append(pygame.image.load(os.path.join("images", "right_side_of_ground.png")).convert_alpha())
    image[4] = pygame.transform.scale(image[4], (200, 200))
    image.append(pygame.image.load(os.path.join("images", "middle_ground.png")).convert_alpha())
    image[5] = pygame.transform.scale(image[5], (200, 200))
    image.append(pygame.image.load(os.path.join("images", "main_guy_crouching.png")).convert_alpha())
    image[6] = pygame.transform.scale(image[6], (200, 200))
    image.append(pygame.image.load(os.path.join("images", "main_guy_crouching_and_walking_left.png")).convert_alpha())
    image[7] = pygame.transform.scale(image[7], (200, 200))
    image.append(pygame.image.load(os.path.join("images", "main_guy_crouching_and_walking_right.png")).convert_alpha())
    image[8] = pygame.transform.scale(image[8], (200, 200))
    image.append(pygame.image.load(os.path.join("images", "backround.png")).convert_alpha())
    image[9] = pygame.transform.scale(image[9], (800, 600))
    image.append(pygame.image.load(os.path.join("images", "window.png")).convert_alpha())
    image[10] = pygame.transform.scale(image[10], (800, 600))
    return image
