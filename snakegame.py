import pygame
import sys
import random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
     
    def draw_snake(self):
        for block in self.body:
            #create a react
            #draw the reactangle
            block_rect = pygame.Rect(int(block.x *cell_size),int(block.y * cell_size),cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self):
        body_copy=self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction) #direction is player input
        self.body = body_copy[:]

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = pygame.math.Vector2(self.x,self.y)

    def draw_fruit(self):
        #create  a rectangle
        #draw the rectangle

        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_number,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
    
    def draw_elements(self): 
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            print('snack')
        



pygame.init()
cell_size = 30
cell_number= 20
screen = pygame.display.set_mode((cell_number * cell_size , cell_number * cell_size ))  #size of screen
clock = pygame.time.Clock() #frame rate

#test_surface = pygame.Surface((100,200))  
#test_rect = test_surface.get_rect(center = (200,250))

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)

         
    screen.fill((152,251,152))
    main_game.draw_elements()
    #screen.blit(test_surface,test_rect)
    pygame.display.update()
    clock.tick(60)