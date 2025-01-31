import pygame
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load assets
background = pygame.image.load("2.webp")  # Use a real image file
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 36)

def draw_loading_bar(progress):
    """ Draws a simple loading bar on the screen. """
    bar_width = 400
    bar_height = 30
    bar_x = (WIDTH - bar_width) // 2
    bar_y = HEIGHT - 100
    pygame.draw.rect(screen, BLACK, (bar_x, bar_y, bar_width, bar_height))  # Border
    pygame.draw.rect(screen, GREEN, (bar_x, bar_y, bar_width * progress, bar_height))  # Fill

def loading_screen():
    """ Displays a loading screen while simulating asset loading. """
    running = True
    progress = 0

    while running:
        screen.blit(background, (0, 0))  # Display background
        text = font.render("Loading...", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2))

        draw_loading_bar(progress)  # Show loading progress

        pygame.display.flip()
        time.sleep(0.5)  # Simulate loading time
        progress += 0.2

        if progress >= 1:
            running = False  # Exit when loading completes

# Run loading screen
loading_screen()

# Quit Pygame (remove this if transitioning to the main game)
pygame.quit()