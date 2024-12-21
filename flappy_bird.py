import pygame 
import random
import math

pygame.init()

bird = pygame.image.load('bird.png')
bg = pygame.image.load('bg.png')
score = 0

fps = 60
x = 0
width,height = 1000,800
bg_color = (173, 216, 230)
rect_color = (1, 50, 32)
rect_width = 100
pair_spacing = rect_width + 200
bird_x,bird_y = width//2-75,height//2
gravity =0.47
bird_speed_up = 7.85
bird_velocity = 0
barrel_speed = 3
gap = 150
pause = False
#font 
pygame.font.init()
font = pygame.font.Font(None,50)
font2 = pygame.font.Font(None,150)

#rect_1 (upper)
rect1_height = random.randint(150,600)
rect1_x = width
rect1_y = 0 
barrel_rect1 = pygame.Rect(rect1_x,rect1_y,rect_width,rect1_height)

#rect_2 (lower)
rect2_height = height-rect1_height-gap
rect2_x = rect1_x
rect2_y = height-rect2_height
barrel_rect2 = pygame.Rect(rect2_x,rect2_y,rect_width,rect2_height)

#rect_3 (upper)
rect3_height = random.randint(150,600)
rect3_x = rect1_x+pair_spacing 
rect3_y = 0
barrel_rect3 = pygame.Rect(rect3_x,rect3_y,rect_width,rect3_height)

#rect_4 (lower)
rect4_height = height-rect3_height-gap
rect4_x = rect3_x
rect4_y = height-rect4_height
barrel_rect4 = pygame.Rect(rect4_x,rect4_y,rect_width,rect4_height)

#rect_5 (upper)
rect5_height =random.randint(150,600)
rect5_x = rect3_x+pair_spacing
rect5_y = 0
barrel_rect5 = pygame.Rect(rect5_x,rect5_y,rect_width,rect5_height)

#rect_6 (lower)
rect6_height = height-rect5_height-gap
rect6_x = rect5_x
rect6_y = height-rect6_height
barrel_rect6 = pygame.Rect(rect6_x,rect6_y,rect_width,rect6_height)

#rect_7 (upper)
rect7_height = random.randint(150,600)
rect7_x = rect5_x+pair_spacing-50
rect7_y = 0
barrel_rect7 = pygame.Rect(rect5_x,rect7_y,rect_width,rect7_height)

#rect_8 (lower)
rect8_height = height-rect7_height-gap
rect8_x = rect7_x
rect8_y = height-rect8_height
barrel_rect8 = pygame.Rect(rect8_x,rect8_y,rect_width,rect8_height)


#CREATING BIRD RECT 
bird_width = 50
bird_height = 36
bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

#DISPLAY MODE 

window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
run = True

#GAME LOOP - 

while run:
    
    keys = pygame.key.get_pressed()
    clock.tick(fps)
    window.fill(bg_color)
    window.blit(bg,(0,0))    
    window.blit(bird,(bird_x,bird_y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -bird_speed_up
            if event.key == pygame.K_p:
                pause = not pause
    if not pause:
        rect1_x-=barrel_speed
        barrel_rect1.x = rect1_x
        rect2_x-=barrel_speed
        barrel_rect2.x = rect2_x
        rect3_x-=barrel_speed
        barrel_rect3.x = rect3_x
        rect4_x-=barrel_speed
        barrel_rect4.x = rect4_x
        rect5_x-=barrel_speed
        barrel_rect5.x = rect5_x
        rect6_x-=barrel_speed
        barrel_rect6.x = rect6_x
        rect7_x-=barrel_speed
        barrel_rect7.x = rect7_x
        rect8_x-=barrel_speed
        barrel_rect8.x = rect8_x


    
    #drawing the barrels
    pygame.draw.rect(window,rect_color,barrel_rect1)
    pygame.draw.rect(window,rect_color,barrel_rect2)
    pygame.draw.rect(window,rect_color,barrel_rect3)
    pygame.draw.rect(window,rect_color,barrel_rect4)
    pygame.draw.rect(window,rect_color,barrel_rect5)
    pygame.draw.rect(window,rect_color,barrel_rect6)
    pygame.draw.rect(window,rect_color,barrel_rect7)
    pygame.draw.rect(window,rect_color,barrel_rect8)


    if rect1_x+rect_width<=0:
        rect1_x = width 
        barrel_rect1.x = rect1_x
        rect1_height = random.randint(150,600)

    if rect2_x+rect_width<=0:
        rect2_x = width 
        barrel_rect2.x = rect2_x
    if rect3_x+rect_width<=0:
        rect3_x = width 
        barrel_rect3.x = rect3_x
        rect3_height = random.randint(150,600)

    if rect4_x+rect_width<=0:
        rect4_x = width 
        barrel_rect4.x = rect4_x
    if rect5_x+rect_width<=0:
        rect5_x = width 
        barrel_rect5.x = rect5_x
        rect5_height = random.randint(150,600)

    if rect6_x+rect_width<=0:
        rect6_x = width 
        barrel_rect6.x = rect6_x
    if rect7_x+rect_width<=0:
        rect7_x = width 
        barrel_rect7.x = rect7_x
        rect7_height = random.randint(150,600)
         
    if rect8_x+rect_width<=0:
        rect8_x = width   
        barrel_rect8.x = rect8_x

    if bird_rect.colliderect(barrel_rect1) or bird_rect.y > height or bird_rect.y<-10 or bird_rect.colliderect(barrel_rect2) or bird_rect.colliderect(barrel_rect3) or bird_rect.colliderect(barrel_rect4)  or bird_rect.colliderect(barrel_rect5) or  bird_rect.colliderect(barrel_rect6) or bird_rect.colliderect(barrel_rect7) or bird_rect.colliderect(barrel_rect8): 
        pause = True
        x = 1
        end_font = font.render((f'GAME OVER'),True,(255,0,0)) 
        window.blit(end_font,(400,400))

    if not pause:  
        bird_velocity+=gravity
        bird_y+=bird_velocity
        bird_rect.y = bird_y 
    
    if pause and x!=1:
        pause_font = font.render((f'PAUSED'),True,(255,0,0))
        window.blit(pause_font,(500,400))
        
    pygame.display.update()


pygame.quit()
  