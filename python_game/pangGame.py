#1. 모든 공을 없애면 게임 종료
#2. 캐릭터는 공에 닿으면 게임 종료
#3. 시간 제한 99초 초과 시 게임 종료


import pygame
import os
pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('pang game')
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path,'image')

background = pygame.image.load(os.path.join(image_path,'bg2.png'))

stage = pygame.image.load(os.path.join(image_path,'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

character = pygame.image.load(os.path.join(image_path,'character2.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width /2
character_y_pos = screen_height - character_height - stage_height
character_to_x_LEFT= 0
character_to_x_RIGHT= 0
character_speed = 1.5

weapon = pygame.image.load(os.path.join(image_path,'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapons = []
weapon_speed = 6 

ball_images = [
    pygame.image.load(os.path.join(image_path,'balloon1.png')),
    pygame.image.load(os.path.join(image_path,'balloon2.png')),
    pygame.image.load(os.path.join(image_path,'balloon3.png')),
    pygame.image.load(os.path.join(image_path,'balloon4.png')),
]

#공크기에 따른 최초 스피드
ball_speed_y = [-18,-15,-12,-9]

balls = []
# 최초 발생하는 큰 공 추가
balls.append({
    'pos_x' : 50,
    'pos_y' : 50, 
    'img_idx' : 1  ,#공의 이미지 인덱사
    'to_x' : 3, #x축 이동방햑, -3이면 왼쪽,3이면 오른쪽
    'to_y' : -6, #y쪽 이동방향
    'init_spd_y' : ball_speed_y[0] #y 최고속도
})

#사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

# Font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks =pygame.time.get_ticks() 
# 게임 종료 메시지
# TimeOut(시간 초과 실패) 
# Mission Complete(성공) 
# Game Over (캐릭터 공에 맞음, 실패)
game_result = "Game Over"

running = True
while running :
    dt = clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_LEFT :
                character_to_x_LEFT -= character_speed 
            elif event.key == pygame.K_RIGHT : 
                character_to_x_RIGHT += character_speed 
            elif event.key == pygame.K_SPACE :
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
                
                
        if event.type == pygame.KEYUP : 
            if event.key == pygame.K_LEFT : 
                character_to_x_LEFT = 0
            elif event.key == pygame.K_RIGHT :
                character_to_x_RIGHT = 0
    character_x_pos += (character_to_x_LEFT + character_to_x_RIGHT) * dt
    
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    # 100, 200 -> 180, 160, 140, ...
    # 500, 200 -> 180, 160, 140, ...   
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] #무기 위치를 위로 조정   
    
    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0] #천당에 닿은 무기 없애기
    
    for ball_idx, ball_val in enumerate(balls) :
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val['img_idx']
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        
        #가로 벽에 닿았을 때 공 이동 위치 변경(튕겨 나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width :
            ball_val['to_x'] = ball_val['to_x'] * -1
            
        #세로 위치
        #스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height :
            ball_val['to_y'] = ball_val['init_spd_y']
        else : # 그 외의 모든 경우에는 속도를 줄여나감
            ball_val['to_y'] += 0.5
        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']
            
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    for ball_idx, ball_val in enumerate(balls) :
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val['img_idx']
        # rhd rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        
        #공과 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect) :
            running = False
            break
        #공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons) :
            weapons_x_pos  = weapon_val[0]
            weapons_y_pos  = weapon_val[1]
            #무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapons_x_pos
            weapon_rect.top = weapons_y_pos
            
            #충돌 체크
            if weapon_rect.colliderect(ball_rect) :
                weapon_to_remove = weapon_idx #해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx #해당 공 없애기 위한 값 설정
      
                #가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                if ball_img_idx < 3 :
                    # 현재 공 크기 정보를 가지고 옴
                    ball_width = ball_rect.size[0] 
                    ball_height = ball_rect.size[1]
                    
                    #나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]
                    # 왼쪽으로 튕겨나가는 작은 공
                    balls.append({
                       'pos_x' : ball_pos_x + (ball_width /2) - (small_ball_width /2),
                       'pos_y' : ball_pos_y +( ball_width / 2) - (small_ball_height /2), 
                       'img_idx' : ball_img_idx + 1 ,
                       'to_x' : -3, 
                       'to_y' : -6,
                       'init_spd_y' : ball_speed_y[ball_img_idx+1] 
                    })
                    # 오른쪽으로 튕겨나가는 작은 공
                    balls.append({
                       'pos_x' : ball_pos_x + (ball_width /2) - (small_ball_width /2),
                       'pos_y' : ball_pos_y +( ball_width / 2) - (small_ball_height /2), 
                       'img_idx' : ball_img_idx + 1 ,
                       'to_x' : 3, 
                       'to_y' : -6, 
                       'init_spd_y' : ball_speed_y[ball_img_idx+1]
                    })                    
                break
        else : # 계속 게임을 진행
            continue #안쪽 for문 조건이 맞지 않으면 continue. 바깥 for문 계속 수행
        break #안쪽 for문에서 break를 만나면 여기로 진입 가능. 2중 for문을 한번에 탈출
    #충돌된 공 or 무기 없애기
    if ball_to_remove > -1 :
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1 :
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    
    #모든 공을 없앤 경우 게임 종료(성공)
    if len(balls) == 0 :
        game_result = "Mission Complete"
        running = False
    
    screen.blit(background,(0,0))
    
    for weapons_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))

    for idx, val in enumerate(balls) :
        ball_pos_x = val['pos_x']
        ball_pos_y = val['pos_y']
        ball_img_idx = val['img_idx']
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    
    timer = game_font.render("Time : {}".format(str(int(total_time - elapsed_time))), True, (255,255,255))
    screen.blit(timer,(10,10))
    
    if total_time - elapsed_time <= 0 : 
        game_result = "Time Over"
        running = False
    pygame.display.update()

# 게임 오버 메시지
msg = game_font.render(game_result,True,(255,255,0)) 
msg_rect = msg.get_rect(center=(screen_width /2 , screen_height /2))
screen.blit(msg,msg_rect)
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()