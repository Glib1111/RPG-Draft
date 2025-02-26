 import pygame, os
from person import Enemy, GameObject
from player import Player
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size_screen = (600, 400)

# screen = pygame.display.set_mode(size_screen)
font = pygame.font.Font(None, 36)
# для використання музики та звуків
#https://www.pygame.org/docs/ref/music.html 
# https://www.geeksforgeeks.org/collision-detection-in-pygame/ бібліотека пайгем кей прессед
#https://stackoverflow.com/questions/6339057/draw-transparent-rectangles-and-polygons-in-pygame прозорість прямокутика

 # Класс екран, приймає розмір і стоврює екран з певню назвою та розміру


class Cursor(GameObject):
    def __init__(self, image_folder, position):
        center_screen = (size_screen[0]/2,size_screen[1]/2)
      
        super().__init__("assets/newCursor", center_screen)

    
class Screen():
    def __init__(self,size,name_screen):
        self.screen = pygame.display.set_mode(size)
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
       
        
        self.images = pygame.sprite.Group()
        pygame.display.set_caption(name_screen)
    def remove_by_group(self,sprite):
        pass
 # додає спрайти в одну группу для наступного відоюражання одразу всіх елементах у грі
    def add_to_group(self, sprite):
        self.images.add(sprite)
# оновлює группу спрайтів 
    def update(self, menu_active=False):
        self.screen.fill(WHITE)
        self.images.draw(self.screen)
        if menu_active:
            menu_image = font.render("Press space to start game", True, BLACK)
            menu_rect = menu_image.get_rect(center=(size_screen[0] / 2, size_screen[1] / 2))
            self.screen.blit(menu_image, menu_rect)

        pygame.display.flip()
        pygame.display.update()
 # класс який створює меню( спрайт)
class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        text = "Press space to start game"
        self.image = font.render(text,True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (size_screen[0] / 2, size_screen[1] / 2)

    
    def show_menu():
        pass
       

        # screen.blit(image, rect)



def game():
    
    path_image = "maxwell.jpeg"
    path_player_idle = 'assets/idle'
    path_helth_bar ='assets/healthBar'
    path_cursor = "assets/newCursor"
    # hide mouse
    pygame.mouse.set_visible(False)

    health_bar = GameObject(path_helth_bar,(size_screen[0]-100,-10))
    image = pygame.image.load(path_image)
    player = Player(path_player_idle,(0,0))
    enemy = Enemy('assets/enemy', (50,50),20)
    
    screen = Screen(size_screen, "RPG_Draft")
    menu = Menu()
    screen.add_to_group(player)
    screen.add_to_group(menu)
    screen.add_to_group(health_bar)
    screen.add_to_group(enemy)
    
    screen.update()
    clock = pygame.time.Clock()
    x = 0
    y = 0
    is_open_menu = False
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()       
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                is_open_menu = not is_open_menu
            player.handle_player_movement(event)
            
        player_pos = player.get_rect()# (0,0)
        enemy.patrol(player_pos)
        
        screen.update(menu_active=is_open_menu)
        pygame.display.update()
        clock.tick(10)

