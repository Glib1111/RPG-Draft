import pygame, os
class GameObject(pygame.sprite.Sprite):
  def __init__(self, image_folder, position):
    super().__init__()
    self.images_list = self.load_images_from_folder(image_folder)
    self.image = self.images_list[0]
    self.rect = self.image.get_rect()
    self.rect.x = position[0]
    self.rect.y = position[1]
   
    

  def load_images_from_folder(self,folder):
    images = []
    for file_name in os.listdir(folder):
      img = pygame.image.load(os.path.join(folder,file_name))
      if img is not None:
        images.append(img)
    return images

  
  def switch_image(self, new_image):
    self.image = new_image
  
  def get_rect(self):
    return self.rect

  def set_rect(self, x, y):
    self.rect.x = x
    self.rect.y = y 

    
class Character(GameObject):

  def __init__(self,img,position, helth):
   
    super().__init__(img,position)
    self.helth = helth
    self.step = 5
   

  def get_helth(self):
    return self.helth
    
  def set_helth(self, new_helth):
    self.helth = new_helth

  def hit(self, get_damage):
    self.helth 
# ф-ції для руху персонажа
  def move_right(self):
    self.rect.x += self.step
    
  def move_left(self):
    self.rect.x -= self.step
 
  def move_up(self):
    self.rect.y -= self.step
    
  def move_down(self):
    self.rect.y += self.step



class NPC(Character):
  def __init__(self, image, position, health):
    super().__init__(image, position, health)

  
class Enemy(NPC):
  def __inti(self,image, position, health, damage_attack):
    super().__init__(image,position, health)
    self.damage_attack = damage_attack
    self.patrol_distance = 50
    
  def attack(self, damage_character):
    helth_npc = damage_character.get_helth()
    damage_character.set_helth(helth_npc - self.damage_attack)
   

  #distance = pygame.Vector2(player.rect.center).distance_to(pygame.Vector2(other.rect.center))

  def check_distance(self,player):
    distance = pygame.Vector2(player.rect.center).distance_to(pygame.Vector2(self.rect.center))
    vision = 20
    print(distance)# check distance return true/ false 
   
  def move_to_player(self, player):
    pass
    # якщо гравець.х < ворог.х -> тоді ворог наліво іде 
    # якщо гравець.х > ворог.х -> тоді ворог направо іде
    # якщо гравець.у < ворог.у -> тоді ворог вверх
    # якщо гравець.у > ворог.у -> тоді ворог вниз
    
    
  def patrol(self, target_pos):  
    if self.rect.x < target_pos[0]:
      self.move_right()
    elif self.rect.x > target_pos[0]:
      self.move_left()
    elif self.rect.y < target_pos[1]:
      self.move_down() 
    elif self.rect.y > target_pos[1]:
      self.move_up()
    
    

    
    

  


