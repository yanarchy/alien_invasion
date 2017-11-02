import pygame
import random

class Alien():

  def __init__(self, ai_settings, screen):
    self.screen = screen
    self.ai_settings = ai_settings

    self.image = pygame.image.load('alien.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    self.rect.centerx = self.screen_rect.centerx
    self.rect.top = self.screen_rect.top

    self.center = float(self.rect.centerx)

    self.y = float(self.rect.y)

    self.moving_right = 0
    self.moving_left = 0
    self.moving_down = 0

  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def update(self):
    self.y += 2
    self.rect.y = self.y