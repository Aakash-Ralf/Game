import pygame
import requests

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLUE = (0, 122, 204)

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Game")

font = pygame.font.Font(None, 36)
score = 0
SERVER_URL = "http://127.0.0.1:5000/update_score"

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw button
    button_rect = pygame.Rect(150, 120, 100, 50)
    pygame.draw.rect(screen, BLUE, button_rect)

    text = font.render("Click!", True, WHITE)
    screen.blit(text, (175, 135))

    # Display Score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (150, 50))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                score += 1
                # Send score to server
                requests.post(SERVER_URL, json={"score": score})

    pygame.display.flip()

pygame.quit()

