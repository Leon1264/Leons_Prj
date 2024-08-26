import pygame
import random
import math
#constants
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
enemy_start_y_2_min = 50
enemy_start_y_2_max = 150
enemy_speed_x_2 = 4
enemy_speed_y_2 = 40
bullet_speed_y = 40
collision_distance = 27

#intitilaize pygame

pygame.init()

#create the screen

screen = pygame.display.set_mode((screen_width,screen_height))


#background of screen
background = pygame.image.load("bg_1.png")

#set caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player

player_img = pygame.image.load("player.png")
player_x = player_start_x
player_y = player_start_y
player_x_change = 0

#enemy

enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
no_of_enemies = 3

enemy_img_2 = []
enemy_x_2 = []
enemy_y_2 = []
enemy_x_change_2 = []
enemy_y_change_2 = []
no_of_enemies_2 = 3


#loop to spawn enemies

for i in range(no_of_enemies):
    enemy_img.append(pygame.image.load("Enemy.png"))
    enemy_x.append(random.randint(0, screen_width-64))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

for i in range(no_of_enemies_2):
    enemy_img_2.append(pygame.image.load("Enemy_2.png"))
    enemy_x_2.append(random.randint(0, screen_width-64))
    enemy_y_2.append(random.randint(enemy_start_y_2_min, enemy_start_y_2_max))
    enemy_x_change_2.append(enemy_speed_x_2)
    enemy_y_change_2.append(enemy_speed_y_2)

#bullet

bullet_img = pygame.image.load("Bullet.png")
bullet_x = 0
bullety = player_start_y
bullet_x_change = 0
bullet_y_change = bullet_speed_y
bullet_state = "ready"

#score

score_value = 0 
font = pygame.font.Font("Times New Roman",32)
text_x = 10
text_y = 10

#game over text
game_over_font = pygame.font.Font("Times New Roman",64)

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))


def game_over_text(x,y):
    game_over_text = font.render("Game Over!", True, (255,255,255))
    screen.blit(game_over_text, (x,y))

def player(x,y):
    screen.blit(player_img(x,y))

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x +16, y + 10))
