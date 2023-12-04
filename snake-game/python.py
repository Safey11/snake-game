import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 400, 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake and food
snake = [(20, 20)]
snake_direction = (1, 0)
food = (random.randint(0, width // 20 - 1) * 20, random.randint(0, height // 20 - 1) * 20)

# Game variables
clock = pygame.time.Clock()
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_direction = (1, 0)

    # Update snake's position
    new_head = (snake[0][0] + snake_direction[0] * 20, snake[0][1] + snake_direction[1] * 20)
    snake.insert(0, new_head)

    # Check for collision with food
    if new_head == food:
        food = (random.randint(0, width // 20 - 1) * 20, random.randint(0, height // 20 - 1) * 20)
    else:
        snake.pop()

    # Check for collision with walls or self
    if (
        new_head[0] < 0 or new_head[0] >= width or
        new_head[1] < 0 or new_head[1] >= height or
        new_head in snake[1:]
    ):
        game_over = True

    # Clear screen
    display.fill(black)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(display, green, (segment[0], segment[1], 20, 20))

    # Draw food
    pygame.draw.rect(display, red, (food[0], food[1], 20, 20))

    # Update display
    pygame.display.update()

    # Frame rate
    clock.tick(10)

# Quit pygame
pygame.quit()

 