import pygame
import random
from pygame.locals import *
import time

#change background
def changeBackground(img):
    # Change the background 
    background = pygame.image.load(img)
    #set its size
    bg = pygame.transform.scale(background, (screen_width,screen_height))
    screen.blit(bg,(0,0))
  
 
# Initialize Pygame
pygame.init()
pygame.display.set_caption('Recycle Marathon')
# Set the height and width of the screen
screen_width=900
screen_height=700
screen = pygame.display.set_mode([screen_width,screen_height])

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imgaes/bin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

class Recycleable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (20, 30))
        self.rect = self.image.get_rect()

class Non_Recycleable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imgaes/bag.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

images = ["box.png", "pencil.png", "item1.png", "him.jpg"]
recycleables = pygame.sprite.Group()
all_sprites  = pygame.sprite.Group()
non_recycleables = pygame.sprite.Group()
for i in range(32):
    item = Recycleable(random.choice(images))
    item.rect.x = random.randint(screen_width)
    item.rect.y = random.randint(screen_height)
    recycleables.add(item)
    all_sprites.add(item)


for i in range(16):
    plastic = Non_Recycleable()
    plastic.rect.x = random.randint(screen_width)
    plastic.rect.y = random.randint(screen_height)
    non_recycleables.add(plastic)
    all_sprites.add(plastic)

bin = Bin()
all_sprites.add(bin)




