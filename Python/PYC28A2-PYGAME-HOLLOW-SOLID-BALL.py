import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))
green = (0,255,0)
black = (0,0,0)
pygame.display.set_caption("Pygame hollow solid ball")
pygame.draw.circle(screen, green , (300,300),50)
pygame.draw.circle(screen, black , (100,100),50,3)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()