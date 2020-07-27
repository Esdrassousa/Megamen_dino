import pygame , random

from pygame.locals import*
import pyautogui

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600


SPEED = 5
SPEED2 = 7
SUST = 0.1
GRAVITY  = 5
x = 290
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT)) 

VeloG = 15
clock = pygame.time.Clock()
# int i;
class Mega(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.images = [pygame.image.load('mega1.png').convert_alpha(),
                       pygame.image.load('mega2.png').convert_alpha(),
                       pygame.image.load('mega3.png').convert_alpha(),
                       pygame.image.load('mega4.png').convert_alpha(),
                       pygame.image.load('mega5.png').convert_alpha()]
        
        
        
        
        self.current_image = 0
        self.image = pygame.image.load('mega1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = 320
    
    def velocit(self):
        
        self.speed = SPEED
        self.speed += GRAVITY
        self.rect[1] += self.speed 
    
    def update(self):
        self.current_image = (self.current_image + 1) %5
        self.image = self.images[self.current_image]
        

        self.speed  = 0; 
        self.speed = SPEED
        self.speed += GRAVITY
        self.rect[1] += self.speed 
            

        
        if self.rect[1] > 320:
        
            self.rect[1] = 320
    
    def up(self):
        
        self.rect[1] = 150

    # def down(self):
        
    #     self.rect[1] = x+1

class Cena(pygame.sprite.Sprite):
    
    
    def __init__(self,xdepois):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("cena.jpg")
        self.image = pygame.transform.scale(self.image,(SCREEN_WIDTH ,SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xdepois
    def update(self):
        self.rect[0] -=VeloG
    

class Cac(pygame.sprite.Sprite):
    
    def __init__(self,xpos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('cac.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = 320
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        
        self.rect[0] -= VeloG 
        
# def get_random_cac(xpos):
    
    

        

def is_off(sprite):
    return sprite.rect[0] < -(sprite.rect[2])        
        
BACKGROUND = pygame.image.load('cena.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND,(SCREEN_WIDTH ,SCREEN_HEIGHT))

mega_group = pygame.sprite.Group()
mega = Mega()
mega_group.add(mega)

cena_group = pygame.sprite.Group()
for i in range(10):
        cena  = Cena(SCREEN_WIDTH*i)
        cena_group.add(cena)
 
clock = pygame.time.Clock()


cac_group = pygame.sprite.Group()
for i in range(10):
        cac = Cac(SCREEN_WIDTH*i + 600)
        cac_group.add(cac)
        # cac_group.add(cac[1])

while True:
    
    clock.tick(15)
    for event in  pygame.event.get():
        if event.type==QUIT:
            pygame.quit()

        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                 mega.up()
                 mega.velocit()
                 
        # if event.type == KEYDOWN:
        #     if event.key == K_DOWN:
        #          mega.down()

    screen.blit(BACKGROUND,(0,0)) 
    
    if is_off(cena_group.sprites()[0]):
        cena_group.remove(cena_group.sprites()[0])
        
        new_cena = Cena(2*SCREEN_WIDTH -SCREEN_WIDTH)
        cena_group.add(new_cena)
    
    
    if is_off(cac_group.sprites()[0]):
        cac_group.remove(cac_group.sprites()[0])
        
        new_cac = Cac(SCREEN_WIDTH*i + 600)
        cac_group.add(new_cac)
    
    cena_group.update()
    cena_group.draw(screen)
    
    cac_group.update()
    mega_group.update()
    
    
    
    
    
    mega_group.draw(screen)
    cac_group.draw(screen)
    
    if pygame.sprite.groupcollide(mega_group,cac_group, False, False):
        
        
        pygame.quit()
    
    pygame.display.update()
