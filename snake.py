#chay voi python3.11 tro xuong
#python3.12 co the bi loi module
#cai dat module pygame de chay
# mo cmd chay -pip install pygame
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize the screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("game ran an tao")

# Initialize fonts
font = pygame.font.Font(None, 36)

def draw_grid():
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WINDOW_WIDTH, y))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_fruit(fruit):
    pygame.draw.rect(screen, RED, (fruit[0], fruit[1], GRID_SIZE, GRID_SIZE))

def draw_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (WINDOW_WIDTH - 150, 10))

def game_over_screen():
    screen.fill((0, 0, 0))
    game_over_text = font.render("Game Over!", True, WHITE)
    play_again_text = font.render("Press Enter to Play Again", True, WHITE)
    screen.blit(game_over_text, (150, 150))
    screen.blit(play_again_text, (100, 200))
    pygame.display.flip()

def main():
    snake = [(100, 100), (80, 100), (60, 100)]  # Snake starts with 3 body parts
    direction = RIGHT
    fruit = (200, 200)
    score = 0
    game_over = False

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT
                elif event.key == pygame.K_RETURN:
                    # Restart the game when Enter is pressed
                    snake = [(100, 100), (80, 100), (60, 100)]  # Reset the snake with 3 body parts
                    direction = RIGHT
                    fruit = (200, 200)
                    score = 0
                    game_over = False

        if not game_over:
            # Move the snake
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0] * GRID_SIZE, head_y + direction[1] * GRID_SIZE)
            snake.insert(0, new_head)

            # Check for collision with the fruit
            if snake[0] == fruit:
                score += 1
                fruit = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
            else:
                snake.pop()

            # Check for collision with walls or itself
            if (
                snake[0][0] < 0
                or snake[0][0] >= WINDOW_WIDTH
                or snake[0][1] < 0
                or snake[0][1] >= WINDOW_HEIGHT
                or len(snake) != len(set(snake))
            ):
                game_over = True

            # Clear the screen
            screen.fill((0, 0, 0))

            # Draw the grid, snake, and fruit
            draw_grid()
            draw_snake(snake)
            draw_fruit(fruit)
            draw_score(score)

            # Update the display
            pygame.display.flip()

            # Control game speed
            clock.tick(10)

    # Show game over screen
    game_over_screen()

    # Keep the game over screen displayed until the player presses Enter to play again
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                main()

if __name__ == "__main__":
    main()
