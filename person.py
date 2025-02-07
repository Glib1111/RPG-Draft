import pygame
class Person(pygame.sprite.Sprite):
  def __init__(self,path_image):
    super().__init__()
    self.image = pygame.image.load(path_image)
    self.rect = self.image.get_rect()
    self.rect.x = 0
    self.rect.y = 0


  def get_rect(self):
    return self.rect

  def set_rect(self, x, y):
    self.rect.x = x
    self.rect.y = y 

  def move_right(self):
    self.rect.x += 10
  def move_left(self):
    self.rect.x -= 10
  def move_up(self):
    self.rect.y -= 10
  def move_down(self):
    self.rect.y += 10