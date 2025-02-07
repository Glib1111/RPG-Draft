import pygame
from player import Player
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size_screen = (600, 400)
# screen = pygame.display.set_mode(size_screen)
font = pygame.font.Font(None, 36)

# https://www.geeksforgeeks.org/collision-detection-in-pygame/ бібліотека пайгем кей прессед
#https://stackoverflow.com/questions/6339057/draw-transparent-rectangles-and-polygons-in-pygame прозорість прямокутика

 # Класс екран, приймає розмір і стоврює екран з певню назвою та розміру
class Screen():
    def __init__(self,size,name_screen):
        self.screen = pygame.display.set_mode(size)
        self.images = pygame.sprite.Group()
        pygame.display.set_caption(name_screen)
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
    player = Player(path_image)
    screen = Screen(size_screen, "RPG_Draft")
    menu = Menu()
    screen.add_to_group(player)
    screen.add_to_group(menu)
    
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
     

        
        
        screen.update(menu_active=is_open_menu)
        pygame.display.update()
        clock.tick(60)

