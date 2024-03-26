import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Mario')

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (135, 206, 250)  # Sky blue

# FPS settings
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_size = 50
player_color = RED
player_x, player_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - player_size - 100
player_speed = 5
player_velocity_y = 0
gravity = 0.5
jump_height = -10
ground = SCREEN_HEIGHT - player_size - 100
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

    # Gravity
    player_y += player_velocity_y
    if player_y >= ground:
        player_y = ground
        jumping = False
    player_velocity_y += gravity

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Update display
    pygame.display.update()

    # Cap the FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
