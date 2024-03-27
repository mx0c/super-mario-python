import pygame
import math
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

# Initialize lives
lives = 3

# Initialize Pygame's font module
pygame.font.init()

# Create a font object
font_size = 24
game_font = pygame.font.SysFont('Arial', font_size)


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
    # Exclude the last item assuming it's a "door" placeholder
    platforms = level[:-1]
    
    # Sort platforms based on their y-value, from lowest to highest on the screen
    sorted_platforms = sorted(platforms, key=lambda x: x[1])
    
    # Select the second tallest platform (second smallest y-value)
    # If there's only one platform, this still selects the first due to how indexing works
    second_tallest_platform = sorted_platforms[1] if len(sorted_platforms) > 1 else sorted_platforms[0]
    
    # Define the door's size
    door_size = (50, 100)
    
    # Place the door on top of the second tallest platform
    door_x = second_tallest_platform[0] + second_tallest_platform[2] - door_size[0]
    door_y = second_tallest_platform[1] - door_size[1]
    
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

# Before the game loop, find the tallest platform for the current level
tallest_platform = min(platforms[:-1], key=lambda x: x[1])  # Exclude the door, assuming it's the last item

# Calculate the circle's position to be on top of the tallest platform
circle_radius = 25  # Example radius size for the circle
circle_x = tallest_platform[0] + tallest_platform[2] // 2  # Center of the platform
circle_y = tallest_platform[1] - circle_radius * 2  # Above the platform, adjust as needed

# Function to draw a heart for representing lives
def draw_heart(surface, x, y, size, color):
    half_size = size // 2
    quarter_size = size // 4
    end_point = x + size, y + half_size

    # Left half circle
    pygame.draw.circle(surface, color, (x + quarter_size, y + quarter_size), quarter_size)
    # Right half circle
    pygame.draw.circle(surface, color, (x + 3*quarter_size, y + quarter_size), quarter_size)
    # Bottom triangle
    pygame.draw.polygon(surface, color, [(x, y + quarter_size), end_point, (x + half_size, y + size)])

# Lives settings
life_size = 20  # Size of the heart
life_spacing = 5  # Space between each heart


# Game loop
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

    # Infinite looping logic
    if player_x < 0 - player_size:  # Exit screen left
        player_x = SCREEN_WIDTH  # Enter from the right
    elif player_x > SCREEN_WIDTH:  # Exit screen right
        player_x = 0 - player_size  # Enter from the left

    player_y += player_velocity_y
    if player_y > ground:
        player_y = ground
        player_velocity_y = 0
        jumping = False
    else:
        player_velocity_y += gravity

    # Rest of your game loop code where you handle collisions, draw objects, etc.

       

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

        # Collision detection with the circle
    distance_to_circle = math.hypot(player_x - circle_x, player_y - circle_y)
    if distance_to_circle < circle_radius + player_size // 2:
        print("Circle reached! Moving to the next level...")
        current_level += 1
        if current_level >= len(level_data):
            print("You've completed all levels! Congratulations!")
            running = False
            break  # Exit the game loop
        else:
            # Load the new level data
            platforms = level_data[current_level]
            # Recalculate the tallest platform and circle position for the new level
            tallest_platform = min(platforms[:-1], key=lambda x: x[1])  # Assume door is the last item again
            circle_x = tallest_platform[0] + tallest_platform[2] // 2
            circle_y = tallest_platform[1] - circle_radius * 2
            # Reset player position
            player_x, player_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150
            # Optionally reset the villain's position
            villain_x, villain_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 - villain_size

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
        
    # Draw the circle on top of the tallest platform
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    # The door is the last item in the list
    door = platforms[-1]
    pygame.draw.rect(screen, RED, pygame.Rect(door))  # Draw the door in RED for visibility


    for i in range(lives):
        draw_heart(screen, 10 + i * (life_size + life_spacing), 10, life_size, RED)


     # Collision detection with the villain
    villain_rect = pygame.Rect(villain_x, villain_y, villain_size, villain_size)
    if player_rect.colliderect(villain_rect):
        lives -= 1  # Decrement lives
        if lives <= 0:
            print("Out of lives! Game Over.")
            running = False
        else:
            print("Collision with villain! You lost a life.")
            # Reset player and villain positions after losing a life
            player_x, player_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150
            villain_x, villain_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 - villain_size

    # Collision detection with the villain
    villain_rect = pygame.Rect(villain_x, villain_y, villain_size, villain_size)
    if player_rect.colliderect(villain_rect):
        print("Collision with villain! Game Over.")
        running = False

  # Detect collision with the door
    if player_rect.colliderect(pygame.Rect(door)):
        print("Door reached! Returning to the starting point...")
        # Instead of changing levels, reset the player position to the start of the current level
        player_x, player_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150
        # You may want to reset the villain's position as well
        villain_x, villain_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 - villain_size



    # Update display
    pygame.display.update()

    # Cap the FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()