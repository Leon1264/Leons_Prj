import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))
pygame.display.set_caption("Pygame Color Changing Sprite")
colors = {
    'red': pygame.Color('red'),
    'green': pygame.Color('green'),
    'blue': pygame.Color('blue'),
    'yellow': pygame.Color('yellow'),
    'white': pygame.Color('white'),
}

current_color = colors['white']

clock = pygame.time.Clock()
x,y=30,30
sprite_size = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    x+=(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])*3
    y+=(keys[pygame.K_DOWN] - keys[pygame.K_UP])*3

    x = min(max(0,x),500 - sprite_size)
    y = min(max(0,y),500 - sprite_size)

    if x ==0:
        current_color = colors['blue']
    elif x == 500-sprite_size:
        current_color = colors['yellow']
    elif y == 0:
        current_color = colors['red']
    elif y == 500-sprite_size:
        current_color = colors['green']
    else:
        current_color = colors['white']

    screen.fill((0,0,0))
    pygame.draw.rect(screen, current_color,(x,y,sprite_size,sprite_size))
    pygame.display.flip()
    clock.tick(90)