import pygame
from person import Character

class Player(Character):
  def __init__(self,images_folder,position):
    super().__init__(images_folder,position, 100)
    self.in_handle = False 
    self.inventory = "Axe"
    
# todo  дописати рух персонажа
  def handle_player_movement(self,event):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        self.move_right()
        self.switch_image(self.images_list[2])
    elif keys[pygame.K_a]:
        self.move_left()
        self.switch_image(self.images_list[1])
    elif keys[pygame.K_w]:
          self.move_up()
          self.switch_image(self.images_list[3])
    elif keys[pygame.K_s]:
          self.move_down()
          self.switch_image(self.images_list[0])