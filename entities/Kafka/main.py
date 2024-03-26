import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Mario')

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (135, 206, 250)  # Sky blue

# Main platform
platforms = [(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)]

platforms = [
    (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 100),  # Main ground platform
    (50, SCREEN_HEIGHT - 250, 200, 50),        # First platform
    (400, SCREEN_HEIGHT - 400, 200, 50),        # Second platform
    (500, SCREEN_HEIGHT - 200, 200, 50)         # Third platform
]

platform_color = GREEN

# FPS settings
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_size = 50
player_color = RED
player_x, player_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150
player_speed = 5
player_velocity_y = 0
gravity = 0.5
jump_height = -15
ground = SCREEN_HEIGHT - player_size - 50
jumping = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                player_velocity_y = jump_height
                jumping = True

    # Key presses for horizontal movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Gravity and jumping
    player_y += player_velocity_y
    player_velocity_y += gravity
    if player_y > ground:
        player_y = ground
        jumping = False

    # Collision detection with platforms
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for platform in platforms:
        platform_rect = pygame.Rect(platform)
        if player_rect.colliderect(platform_rect) and player_velocity_y >= 0:
            player_y = platform[1] - player_size
            jumping = False
            player_velocity_y = 0
            break

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, platform_color, platform)

    # Update display
    pygame.display.update()

    # Cap the FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
