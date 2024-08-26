import pygame

pygame.init()


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Adding a backgroung image")

background = pygame.transform.scale(pygame.image.load('background.jpeg').convert(),(500,500))
penguin = pygame.transform.scale(pygame.image.load('penguin2.png.png').convert_alpha(),(200,200))

penguin_rect = penguin.get_rect(center=(250,250))

text = pygame.font.Font(None, 36).render('Hello World ',True,pygame.Color('black'))
text_rect = text.get_rect(center=(250,450))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))        
    screen.blit(penguin,penguin_rect)        
    screen.blit(text,text_rect)        
    pygame.display.flip()