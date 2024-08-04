import random

import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_block_size = 10
snake_speed = 15
clock = pygame.time.Clock()

# Font for displaying score
font_style = pygame.font.SysFont(None, 30)

def display_score(score):
    """Displays the current score on the screen."""
    value = font_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

def draw_snake(snake_block_size, snake_list):
    """Draws the snake on the screen."""
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_block_size, snake_block_size])

def message(msg, color):
    """Displays a message on the screen."""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/6, screen_height/3])

def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    # Food position
    foodx = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            screen.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            # Event handling in game over loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    ifimport random

import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_block_size = 10
snake_speed = 15
clock = pygame.time.Clock()

# Font for displaying score
font_style = pygame.font.SysFont(None, 30)

def display_score(score):
    """Displays the current score on the screen."""
    value = font_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

def draw_snake(snake_block_size, snake_list):
    """Draws the snake on the screen."""
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_block_size, snake_block_size])

def message(msg, color):
    """Displays a message on the screen."""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/6, screen_height/3])

def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    # Food position
    foodx = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            screen.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()