import pygame

pygame.init()

#screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Smol Game")
icon = pygame.image.load('galaxy.png')
pygame.display.set_icon(icon)

#player

playerimg = pygame.image.load('ship.png')
playerX = 360
playerY = 470

def player():
    screen.blit(playerimg,(playerX, playerY))
#game running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.update()