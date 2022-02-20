import pygame
import sys
import random


class MouseImg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("crosshair2.png")
        self.rect = self.image.get_rect()
        self.shot = pygame.mixer.Sound("gun_shot.aiff")

    def shoot(self):
        self.shot.play()
        pygame.sprite.spritecollide(cursor, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
  

class Target(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("target.png")
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# initiates
pygame.init()
