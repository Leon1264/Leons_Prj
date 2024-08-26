
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful bounce")


sprite_color_change_event = pygame.USEREVENT+1
bg_color_change_event = pygame.USEREVENT+2

blue = pygame.Color('blue')
dark_blue = pygame.Color('darkblue')
light_blue = pygame.Color('lightblue')
yellow = pygame.Color('yellow')
magenta = pygame.Color('magenta')
orange = pygame.Color('orange')
white = pygame.Color('white')

def change_bgcolor():
    global bg_color
    bg_color = random.choice([blue,light_blue,dark_blue])

def change_spritecolor(sprite):
    sprite.fill(random.choice([yellow,magenta,orange,white]))

def update_sprite(sprite, rect, velocity):
    rect.move_ip(velocity)
    boundry_hit = False

    if rect.left <=0 or rect.right >=500:
        velocity[0] = -velocity[0]
        boundry_hit = True

    if rect.top <= 0 or rect.bottom >= 400:
        velocity[1] = -velocity[1]
        boundry_hit = True  

    if boundry_hit:
        pygame.event.post(pygame.event.Event(sprite_color_change_event))
        pygame.event.post(pygame.event.Event(bg_color_change_event))

pygame.event.post(pygame.event.Event(sprite_color_change_event))

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Colorfull Bounce")
bg_color = blue
screen.fill(bg_color)

sprite = pygame.Surface((30,20))
sprite.fill(white)

rect = sprite.get_rect()
rect.x = random.randint(0,489)
rect.y = random.randint(0,370)
velocity = [random.choice([-1,1]), random.choice([-1,1])]

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            exit = True
        elif event.type == sprite_color_change_event:
            change_spritecolor(sprite)
        elif event.type == bg_color_change_event:
            change_bgcolor()
    update_sprite(sprite, rect, velocity)
    screen.fill(bg_color)
    screen.blit(sprite, rect)

    pygame.display.flip()

    clock.tick(240)

pygame.quit()

