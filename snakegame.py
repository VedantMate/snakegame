import pygame
import sys
import random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load(r"graphics\head_up.png").convert_alpha()
        self.head_down = pygame.image.load(r"graphics\head_down.png").convert_alpha()
        self.head_right = pygame.image.load(r"graphics\head_right.png").convert_alpha()
        self.head_left = pygame.image.load(r"graphics\head_left.png").convert_alpha()

        self.tail_up = pygame.image.load(r"graphics\tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load(r"graphics\tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load(r"graphics\tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load(r"graphics\tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load(r"graphics\body_vr.png").convert_alpha()
        self.body_horizontal = pygame.image.load(r"graphics\body_hr.png").convert_alpha()

        self.body_ur = pygame.image.load(r"graphics\up_right.png").convert_alpha()
        self.body_ul = pygame.image.load(r"graphics\up_left.png").convert_alpha()
        self.body_dr = pygame.image.load(r"graphics\down_right.png").convert_alpha()
        self.body_dl = pygame.image.load(r"graphics\down_left.png").convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body): #reactions for the position
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)

            elif index == len(self.body) -1 :
                screen.blit(self.tail,block_rect)

            else:
                previous_block = self.body[index+1] - block
                next_block = self.body[index-1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x ==-1 and next_block.y ==-1 or previous_block.y ==-1 and next_block.x ==-1:
                        screen.blit(self.body_dl,block_rect)
                    elif previous_block.x ==-1 and next_block.y ==1 or previous_block.y ==1 and next_block.x ==-1:
                        screen.blit(self.body_ul,block_rect)
                    elif previous_block.x ==1 and next_block.y ==-1 or previous_block.y ==-1 and next_block.x ==1:
                        screen.blit(self.body_dr,block_rect)
                    elif previous_block.x ==1 and next_block.y ==1 or previous_block.y ==1 and next_block.x ==1:
                        screen.blit(self.body_ur,block_rect)

            #else: 
                #pygame.draw.rect(screen,(150,100,100),block_rect)
       
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): 
            self.head=self.head_left
        elif head_relation == Vector2(-1,0): 
            self.head=self.head_right
        elif head_relation == Vector2(0,1): 
            self.head=self.head_up
        elif head_relation == Vector2(0,-1): 
            self.head=self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): 
            self.tail=self.tail_right
        elif tail_relation == Vector2(-1,0): 
            self.tail=self.tail_left
        elif tail_relation == Vector2(0,1): 
            self.tail=self.tail_down
        elif tail_relation == Vector2(0,-1): 
            self.tail=self.tail_up
        


    def move_snake(self):

        if self.new_block == True:
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction) #direction is player input
            self.body = body_copy[:]
            self.new_block = False
        else :
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
         

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        #create  a rectangle
        #draw the rectangle

        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_number,cell_size)
        #pygame.draw.rect(screen,(126,166,114),fruit_rect)
        screen.blit(apple,fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = pygame.math.Vector2(self.x,self.y)

class MAIN: 
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self): 
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: 
            #reposition the fruit
            #add another block to the snack
            self.fruit.randomize()
            self.snake.add_block()
        
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            
    def check_fail(self):
        #check if snake hits wall
        #check if snake hits itself

        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_colour = (144,238,144)

        for row in range(cell_number): 
            if row%2 ==0:
                for col in range(cell_number):
                    if col %2 ==0:
                        grass_rect = pygame.Rect(col * cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_colour,grass_rect)
            else:
                for col in range(cell_number):
                    if col %2 !=0:
                        grass_rect = pygame.Rect(col * cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_colour,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface =game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size*cell_number-50)
        score_y = int(cell_size*cell_number -40)
        score_rect = score_surface.get_rect(center =(score_x,score_y))
        apple_rect=apple.get_rect(midright= (score_rect.left,score_rect.right))
        bg_rect = pygame.Rect(apple_rect.left-10,apple_rect.top,apple_rect.width + score_rect.width +15,apple_rect.height+10)

        pygame.draw.rect(screen,(135,206,250),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(106,90,205),bg_rect,2)

pygame.init()
cell_size = 30
cell_number= 20
screen = pygame.display.set_mode((cell_number * cell_size , cell_number * cell_size ))  #size of screen
clock = pygame.time.Clock() #frame rate
apple = pygame.image.load("graphics\ple.png").convert_alpha()
game_font = pygame.font.Font(r'text\lemon_milk\LEMONMILK-Medium.otf',25)

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
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1: 
                    main_game.snake.direction = Vector2(-1,0)

         
    screen.fill((152,251,152))
    main_game.draw_elements()
    #screen.blit(test_surface,test_rect)
    pygame.display.update()
    clock.tick(30)