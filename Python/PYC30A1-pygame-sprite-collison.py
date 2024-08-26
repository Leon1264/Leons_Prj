import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

running = True
won = False
clock = pygame.time.Clock()

background_image = pygame.transform.scale(
    pygame.image.load("bg.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT)
)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

def create_sprite(color, width, height):
    sprite = pygame.Surface([width, height])
    sprite.fill(pygame.Color("dodgerblue"))
    pygame.draw.rect(sprite, color, pygame.Rect(0, 0, width, height))
    rect = sprite.get_rect()
    rect.x = random.randint(0, SCREEN_WIDTH - rect.width)
    rect.y = random.randint(0, SCREEN_HEIGHT - rect.height)
    return sprite, rect

def move_sprite(rect, x_change, y_change):
    rect.x = max(min(rect.x + x_change, SCREEN_WIDTH - rect.width), 0)
    rect.y = max(min(rect.y + y_change, SCREEN_HEIGHT - rect.height), 0)

sprite1, rect1 = create_sprite(pygame.Color('black'), 30, 20)
sprite2, rect2 = create_sprite(pygame.Color('red'), 30, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED

        move_sprite(rect1, x_change, y_change)

        if rect1.colliderect(rect2):
            won = True

    screen.blit(background_image, (0, 0))
    screen.blit(sprite1, rect1.topleft)
    screen.blit(sprite2, rect2.topleft)

    if won:
        win_text = font.render("You win!!", True, pygame.Color("black"))
        screen.blit(
            win_text,
            ((SCREEN_WIDTH - win_text.get_width()) // 2, 
             (SCREEN_HEIGHT - win_text.get_height()) // 2)
        )

    pygame.display.flip()
    clock.tick(90)

pygame.quit()