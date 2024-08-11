import pygame
import project 
pygame.init()
pygame.font.init()
project.obstacle_rect_list = []  
project.start_time = 0 
project.screen = pygame.display.set_mode((800, 400))  
project.font = pygame.font.Font(None, 36) 
project.cactus = pygame.Surface((50, 50))  
project.bird_surf = pygame.Surface((50, 50)) 
player_rect = pygame.Rect(100, 100, 50, 50) 


def test_display_score():
    assert project.display_score() == 0 





def test_obstacle_movement():
    project.obstacle_rect_list = [pygame.Rect(900, 350, 50, 50)] 

    
    score = project.obstacle_movement()
    assert len(score) == 1  


def test_collision():
    obstacle_rect_list = [pygame.Rect(100, 100, 50, 50)] 
    assert project.collision(player_rect, obstacle_rect_list) == False



