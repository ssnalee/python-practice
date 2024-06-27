import pygame
from random import *
pygame.init()

screen_width = 480
screen_hegiht = 640
screen = pygame.display.set_mode((screen_width,screen_hegiht))

pygame.display.set_caption('avoid game')

clock = pygame.time.Clock()

background = pygame.image.load('image\\bg.png')

player = pygame.image.load('image\\character.png')
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = screen_width /2 - player_width /2
player_y_pos = screen_hegiht - player_height

to_x = 0

enemy = pygame.image.load('image\\enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0,screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

player_speed = 0.6
game_font = pygame.font.Font(None,40)
total_time =10
start_tick = pygame.time.get_ticks()

running = True
while running : 
    dt = clock.tick(60)
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                to_x -= player_speed
            elif event.key == pygame.K_RIGHT :
                to_x += player_speed           
        
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0

    player_x_pos += to_x * dt
    
    if player_x_pos < 0 :
        player_x_pos = 0
    elif player_x_pos > screen_width - player_width :
        player_x_pos = screen_width - player_width
    
    
    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_hegiht :
        enemy_y_pos = 0
        enemy_x_pos = randint(0,screen_width - enemy_width)
        enemy_speed = randint(7,15)
        
    player_rect = player.get_rect()
    player_rect.left = player_x_pos
    player_rect.top = player_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    if player_rect.colliderect(enemy_rect) :
        print('충돌했어요')
        running = False
        
    screen.blit(background,(0,0))
    screen.blit(player,(player_x_pos,player_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer,(10,10))
    
    if total_time - elapsed_time <= 0 :
        print('타임 아웃')
        running = False
    pygame.display.update()
    
pygame.time.delay(2000)

pygame.quit()