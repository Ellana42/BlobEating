import pygame
import random
import math

# Game setup
pygame.init()
running = True
score = 0

# Display setting
icon = pygame.image.load('ufo-2.png')
screen = pygame.display.set_mode((800, 600), flags=pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)

# Graphics
background = pygame.image.load("Planet.jpg").convert_alpha()
player_img = pygame.image.load("battleship.png").convert_alpha()
enemy_img = pygame.image.load("ufo.png").convert_alpha()
bullet_img = pygame.image.load("bullet.png").convert_alpha()

# Player setup
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 40


def display_player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Bullet
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"  # ready = bullet invisible fire = moving


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y))


def is_colliding(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < 35


# Game loop
while running:
    #screen.blit(background, (0, 0))
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = +3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player mvt
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy mvt
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    # Bullet mvt
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    if is_colliding(enemyX, enemyY, bulletX, bulletY):
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print("Score :", score)
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    display_player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
