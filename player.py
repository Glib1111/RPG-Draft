import re
import pygame
from person import Person

class Player(Person):
  def __init__(self,path_image):
    super().__init__(path_image)
# todo  дописати рух персонажа
  def handle_player_movement(self,event):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        self.move_right()
     # elif keys[pygame.K_a]:
     #     player.move_left()
     # elif keys[pygame.K_w]:
     #      player.move_up()
     # elif keys[pygame.K_s]:
     #     player.move_down()
