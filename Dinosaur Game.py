import pygame
from sys import exit
from random import randint,choice




def collision(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True


def display_score():
    global start_time,font,screen

    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font.render(f'{current_time}',True,(64,64,64))
    score_rect = score_surf.get_rect(center = (770,10))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement():
    global obstacle_rect_list, screen, cactus, bird_surf
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.x -= 5 

            if obstacle_rect.bottom == 350:
                screen.blit(cactus,obstacle_rect)
            else:
                screen.blit(bird_surf,obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_rect_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []



def dino_animation():
    global dino_walk, dino_index, dino_idle

    dino_index += 0.1
    if dino_index >= len(dino_walk) : dino_index = 0
    dino_idle = dino_walk[int(dino_index)]


pygame.init()
pygame.mixer.init()
pygame.font.init()
obstacle_rect_list = []

def main():
    global screen, font, start_time, obstacle_rect_list, cactus, bird_surf, dino_walk, dino_index, dino_idle
   
    

    screen = pygame.display.set_mode((800,400))
    pygame.display.set_caption('Dinosaur Game Clone')
    clock= pygame.time.Clock()
    dino_gravity = 0 
    game_active = False 
    start_time = 0
    score = 0
    play_die_sound = True 

    #assets
    ground_png = pygame.image.load('Background/Ground.png').convert_alpha()

    background = pygame.Surface((800,400))
    background.fill('White')

    bird_1 = pygame.image.load('Bird/Bird_01.png').convert_alpha()
    bird_2 = pygame.image.load('Bird/Bird_02.png').convert_alpha()
    bird_frames = [bird_1,bird_2]
    bird_index = 0
    bird_surf = bird_frames[int(bird_index)]


    cactus = pygame.image.load('Cactus/Cactus.png').convert_alpha()
    cactus_rect = cactus.get_rect(midbottom = (800,350))


    jump_sound = pygame.mixer.Sound('Sound/jump.mp3')
    die_sound = pygame.mixer.Sound('Sound/die.mp3')

    dino_1 = pygame.image.load('Dino/Dino_Run01.png').convert_alpha()    
    dino_2 = pygame.image.load('Dino/Dino_Run02.png').convert_alpha()
    dino_walk = [dino_1,dino_2]
    dino_index = 0
    dino_idle = dino_walk[dino_index]

    dino_idle_rect = dino_idle.get_rect(midbottom = (200,360))

    font = pygame.font.Font('Font/PublicPixel.ttf',17)
    jump_sound.set_volume(1.0)


    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer,1500)

    bird_animation_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(bird_animation_timer,500)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if game_active:
                if event.type == bird_animation_timer:
                    if bird_index == 0 : bird_index = 1
                    else: bird_index = 0
                    bird_surf = bird_frames[bird_index]

            if event.type == obstacle_timer and game_active:
                if randint(0,1):
                    obstacle_rect_list.append(cactus.get_rect(midbottom = (randint(900,1100),350)))
                else: 
                    obstacle_rect_list.append(bird_surf.get_rect(midbottom = (randint(900,1100),210)))
                
            
            if game_active:
                if event.type == pygame.KEYDOWN and dino_idle_rect.bottom == 360:
                    if event.key == pygame.K_SPACE:
                        dino_gravity = -22
                        jump_sound.play()
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_active = True
                    cactus_rect.left = 800
                    start_time = int(pygame.time.get_ticks()/1000)
                    play_die_sound = True 
            
        
        if game_active:
            screen.blit(background,(0,0))
            screen.blit(ground_png,(0,250))
            
            score = display_score()
    
            # screen.blit(cactus,cactus_rect)

            game_active = collision(dino_idle_rect,obstacle_rect_list)

            obstacle_rect_list = obstacle_movement()   
                
            dino_gravity += 1
            dino_idle_rect.y += dino_gravity
            if dino_idle_rect.bottom > 360: dino_idle_rect.bottom = 360
            
            dino_animation()
                
            screen.blit(dino_idle,dino_idle_rect)
        


            if dino_idle_rect.colliderect(cactus_rect):
                game_active = False

            play_die_sound = True

            
        else:
            dino_cover = pygame.image.load('Dino/Dino_Idle.png').convert_alpha()
            screen.fill('White')
            screen.blit(dino_cover,(360,100))
            obstacle_rect_list.clear()

            
            
        
            score_message = font.render(f'your score:{score}',True,(64,64,64))
            score_message_rect = score_message.get_rect(center = (400,300))
            
            game_message = font.render('press any mouse button to start',True,(64,64,64))
            game_message_rect = game_message.get_rect(center = (400,350))
            
            screen.blit(game_message,game_message_rect)
            if score != 0:

                screen.blit(score_message,score_message_rect)
                if play_die_sound:
                    die_sound.play()
                    play_die_sound = False

            

    
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()