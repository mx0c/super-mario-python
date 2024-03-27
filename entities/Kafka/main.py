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
DARK_RED = (139, 0, 0)  # Villain color
BACKGROUND_COLOR = (135, 206, 250)  # Sky blue
platform_color = GREEN  # Platform color


# Level configurations
level_data = [
    # Level 1 updated with a vertical platform
    [
        (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 100),
        (50, SCREEN_HEIGHT - 250, 200, 50),
        (400, SCREEN_HEIGHT - 400, 200, 50),
        (500, SCREEN_HEIGHT - 200, 200, 50),
        (650, SCREEN_HEIGHT - 300, 50, 150),  # Vertical platform added
    ],
    # Level 2 updated with a vertical platform
    [
        (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 100),
        (100, SCREEN_HEIGHT - 150, 200, 50),
        (350, SCREEN_HEIGHT - 300, 200, 50),
        (600, SCREEN_HEIGHT - 450, 200, 50),
        (700, SCREEN_HEIGHT - 300, 50, 150),  # Vertical platform added
    ],
    # Level 3 updated with a vertical platform
    [
        (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 100),
        (150, SCREEN_HEIGHT - 250, 200, 50),
        (500, SCREEN_HEIGHT - 350, 200, 50),
        (250, SCREEN_HEIGHT - 450, 200, 50),
        (550, SCREEN_HEIGHT - 300, 50, 150),  # Vertical platform added
    ]
]


# Function to add a door to the level based on the tallest platform
def add_door_to_level(level):
    # Assuming the last item is a "door" placeholder
    platforms = level[:-1]
    
    # Find the tallest platform (smallest y value)
    tallest_platform = min(platforms, key=lambda x: x[1])
    
    # Define the door's size
    door_size = (50, 100)
    
    # Place the door on top of the tallest platform
    door_x = tallest_platform[0] + tallest_platform[2] - door_size[0]  # Adjust this as necessary
    door_y = tallest_platform[1] - door_size[1]
    
    # Replace the placeholder with the actual door
    level[-1] = (door_x, door_y, door_size[0], door_size[1])

# Process each level to include a door
for level in level_data:
    add_door_to_level(level)

current_level = 0  # Start with the first level
platforms = level_data[current_level]  # Load the platform data for the current level


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

# Villain settings
villain_size = 50
villain_color = DARK_RED
villain_x, villain_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 - villain_size  # Initial position
villain_speed = 2

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

    # Player movement and gravity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_y += player_velocity_y
    if player_y > ground:
        player_y = ground
        player_velocity_y = 0
        jumping = False
    else:
        player_velocity_y += gravity

    # Collision detection with platforms
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for platform in platforms[:-1]:  # Assuming the last item is always the door
        # Define platform_rect here, inside the loop
        platform_rect = pygame.Rect(platform)
        pygame.draw.rect(screen, platform_color, platform_rect)  # Drawing the platform
        if player_rect.colliderect(platform_rect) and player_velocity_y >= 0:
            player_y = platform_rect.top - player_size
            player_velocity_y = 0  # Resetting vertical velocity to 0
            jumping = False  # Indicate that the player is no longer jumping

    # Villain movement (chase player horizontally and vertically)
    villain_move_direction = 1 if player_x > villain_x else -1
    villain_x += villain_speed * villain_move_direction

    if player_y < villain_y:
        villain_y -= villain_speed  # Chase upward
    elif player_y > villain_y:
        villain_y += villain_speed  # Chase downward

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, villain_color, (villain_x, villain_y, villain_size, villain_size))

    # Drawing platforms and the door
    for platform in platforms[:-1]:  # Draw all but the last item as platforms
        pygame.draw.rect(screen, platform_color, pygame.Rect(platform))

    # The door is the last item in the list
    door = platforms[-1]
    pygame.draw.rect(screen, RED, pygame.Rect(door))  # Draw the door in RED for visibility

    # Detect collision with the door
    if player_rect.colliderect(pygame.Rect(door)):
        print("Door reached! Progress to the next level or trigger an event...")
        # Implement level progression or event triggering here


    # Collision detection with the villain
    villain_rect = pygame.Rect(villain_x, villain_y, villain_size, villain_size)
    if player_rect.colliderect(villain_rect):
        print("Collision with villain! Game Over.")
        running = False

    # Inside the collision detection with the door
    if player_rect.colliderect(pygame.Rect(door)):
        current_level += 1
        if current_level >= len(level_data):
            print("Congratulations! You've completed the game!")
            running = False
        else:
            platforms = level_data[current_level]
            player_x, player_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150  # Reset player position for the new level
            # You may also want to reset or update the villain's position here

            player_x, player_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150  # Reset player position
            # Reset villain to a new position for the next level
            villain_x, villain_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 - villain_size
            # Optionally, adjust villain speed or other parameters for increased difficulty

    # Update display
    pygame.display.update()

    # Cap the FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()

