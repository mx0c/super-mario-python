import pygame
import math
import sys
import random


pygame.init()
pygame.mixer.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Mario')

CHARACTER_WIDTH = 64
CHARACTER_HEIGHT = 64
VILLAIN_WIDTH = 64
VILLAIN_HEIGHT = 64
characters_folder = 'characters/player/'
villains_folder = 'characters/player/villain/'
lives_folder = 'characters/player/lives/'
prizes_folder = 'characters/player/prize/'
doors_folder = 'characters/player/doors/'
background_folder = 'characters/backgrounds/'
music_folder = 'music/'


background_images = {
    1: pygame.transform.scale(pygame.image.load(background_folder + 'b1.png'), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    2: pygame.transform.scale(pygame.image.load(background_folder + 'b2.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    3: pygame.transform.scale(pygame.image.load(background_folder + 'b3.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT)),
}

music_files = {
    1: music_folder + 'm1.mp3',
    2: music_folder + 'm2.mp3',
    3: music_folder + 'm3.mp3',
}

player_images = {
    1: pygame.transform.scale(pygame.image.load(characters_folder + 'K.png'), (21, 70)),
    2: pygame.transform.scale(pygame.image.load(characters_folder + 'Beau.gif'), (80, 80)),  
    3: pygame.transform.scale(pygame.image.load(characters_folder + 'Gregor.png'), (45, 64)),
}

villain_images = {
    1: pygame.transform.scale(pygame.image.load(villains_folder + 'v1.png'), (110, 85)),
    2: pygame.transform.scale(pygame.image.load(villains_folder + 'v2.png'), (VILLAIN_WIDTH, VILLAIN_HEIGHT)),
    3: pygame.transform.scale(pygame.image.load(villains_folder + 'v3.png'), (110, 85)),
}

life_images = {
    1: pygame.transform.scale(pygame.image.load(lives_folder+ 'l1.png'), (25, 25)),
    2: pygame.transform.scale(pygame.image.load(lives_folder+ 'l2.webp'), (25, 25)),
    3: pygame.transform.scale(pygame.image.load(lives_folder+ 'l3.png'), (25, 25)),
}

prize_images = {
    1: pygame.transform.scale(pygame.image.load(prizes_folder + 'p1.png'), (50, 50)),
    2: pygame.transform.scale(pygame.image.load(prizes_folder + 'p2.png'), (60, 60)),
    3: pygame.transform.scale(pygame.image.load(prizes_folder + 'p3.png'), (50, 70)),
}

door_images = {
    1: pygame.transform.scale(pygame.image.load(doors_folder + 'd1.png'), (150, 150)),
    2: pygame.transform.scale(pygame.image.load(doors_folder + 'd2.png'), (80, 110)),
    3: pygame.transform.scale(pygame.image.load(doors_folder + 'd3.png'), (75, 75)),
}

# Colors
RED = (255, 0, 0)
GREEN = (165, 42, 42)
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

def play_music_for_level(level_number):
    pygame.mixer.music.stop()  # Stop any music that might be playing
    pygame.mixer.music.load(music_files[level_number])  # Load the new song
    
    # Determine the start time based on the level
    if level_number == 3:  # Adjust if your level numbering starts from 0 or 1
        start_time = 350.0  # Start 5 minutes in for the last level
    else:
        start_time = 120.0  # Start 2 minutes in for the first two levels
    
    pygame.mixer.music.play(-1, start_time)  # Play the music

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
    return door_x, door_y 


door_positions = []  # This will store the door positions for each level

# Assuming add_door_to_level now returns door_x and door_y
for level in level_data:
    door_x, door_y = add_door_to_level(level)  # This captures the returned values
    door_positions.append((door_x, door_y))  # Store them in the list


# Process each level to include a door
for level in level_data:
    add_door_to_level(level)
    
# Level 1 
current_level = 0 
play_music_for_level(current_level + 1) 
platforms = level_data[current_level]  


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

current_player_image = player_images[current_level + 1] 
current_villain_image = villain_images[current_level + 1]
current_lives_image = life_images[current_level + 1]
current_prize_image = prize_images[current_level + 1]

game_over = False
game_over_message = ""

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

       

    # Collision detection with platforms
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for platform in platforms[:-1]:  
        platform_rect = pygame.Rect(platform)
        pygame.draw.rect(screen, platform_color, platform_rect)  
        if player_rect.colliderect(platform_rect) and player_velocity_y >= 0:
            player_y = platform_rect.top - player_size
            player_velocity_y = 0  
            jumping = False  

    distance_to_circle = math.hypot(player_x - circle_x, player_y - circle_y)
    
    if distance_to_circle < circle_radius + player_size // 2:
        print("Circle reached! Moving to the next level...")
        current_level += 1
        if current_level >= len(level_data):
            print("You've completed all levels! Congratulations!")
            running = False
        else:
            # Update this section
            platforms = level_data[current_level]
            tallest_platform = min(platforms[:-1], key=lambda x: x[1])
            circle_x = tallest_platform[0] + tallest_platform[2] // 2
            circle_y = tallest_platform[1] - circle_radius * 2
            player_x, player_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150
            villain_x, villain_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 - villain_size
            play_music_for_level(current_level + 1)
            
            # Add the following line to update the villain image for the new level
            current_player_image = player_images[current_level + 1]
            current_villain_image = villain_images[current_level + 1]
            current_lives_image = life_images[current_level + 1]
            current_prize_image = prize_images[current_level + 1]


    # Villain movement (chase player horizontally and vertically)
    villain_move_direction = 1 if player_x > villain_x else -1
    villain_x += villain_speed * villain_move_direction

    if player_y < villain_y:
        villain_y -= villain_speed  # Chase upward
    elif player_y > villain_y:
        villain_y += villain_speed  # Chase downward

    current_player_image = player_images[current_level + 1] 

    player_image_rect = current_player_image.get_rect()
    player_image_rect.center = (player_x + player_size // 2, player_y + player_size // 2)


    # Drawing
    current_background = background_images[current_level + 1]  # Adjust if necessary
    screen.blit(current_background, (0, 0))
    for platform in platforms[:-1]: 
        pygame.draw.rect(screen, platform_color, pygame.Rect(platform))
        
    # Draw the circle on top of the tallest platform
    screen.blit(current_prize_image, (circle_x - current_prize_image.get_width() / 2, circle_y - current_prize_image.get_height() / 2))
    screen.blit(current_player_image, (player_x, player_y))
    screen.blit(current_villain_image, (villain_x, villain_y))
    move_left_amount = 50 
    # Draw the door
    door_x, door_y = door_positions[current_level]  
    door_x -= move_left_amount  
    current_door_image = door_images[current_level + 1]  
    if current_level == 0:  
        door_y -= 5 
    if current_level == 1:  
        door_y += 25 
    if current_level == 2:  
        door_y += 30 
    door_rect = current_door_image.get_rect(topleft=(door_x, door_y))
    screen.blit(current_door_image, door_rect)




    # The door is the last item in the list
    door = platforms[-1]
    current_door_image = door_images[current_level + 1]  
    door_rect = current_door_image.get_rect(topleft=(door_x, door_y))  
    screen.blit(current_door_image, door_rect) 


    for i in range(lives):
        screen.blit(current_lives_image, (10 + i * (20 + life_spacing), 10))



     # Collision detection with the villain
    villain_rect = pygame.Rect(villain_x, villain_y, villain_size, villain_size)
    if player_rect.colliderect(villain_rect):
        lives -= 1 
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
    if player_rect.colliderect(door_rect):
        print("Door reached! Returning to the starting point...")
        player_x, player_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150
        villain_x, villain_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 - villain_size

    if lives <= 0:
        game_over = True
        running = False  
    
        if current_level == 0:
            game_over_message = "Guilty Until Proven Innocent"
        elif current_level == 1:
            game_over_message = "I Had Not Earned Her Love"
        else:
            game_over_message = "I Cannot Make Anyone Understand"


    pygame.display.update()
    clock.tick(FPS)

if game_over:

    RED = (255, 0, 0)
    screen.fill(BACKGROUND_COLOR)
    game_over_font = pygame.font.SysFont('Arial', 48) 
    game_over_surface = game_over_font.render(game_over_message, True, RED)
    game_over_x = (SCREEN_WIDTH - game_over_surface.get_width()) // 2
    game_over_y = (SCREEN_HEIGHT - game_over_surface.get_height()) // 2
    screen.blit(game_over_surface, (game_over_x, game_over_y))

    pygame.display.update()
    pygame.time.delay(3000) 


pygame.quit()
sys.exit()