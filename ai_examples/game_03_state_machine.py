"""
Mini Game 03: State Machine Runner

Concept focus:
- Managing game states (menu, play, game over)
- Organizing logic by state
- Restart flow

Run:
    python game_03_state_machine.py
"""

import random
import pygame


pygame.init()

WIDTH, HEIGHT = 900, 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game 03 - State Machine Runner")
clock = pygame.time.Clock()


BG = (20, 24, 33)
TEXT = (236, 241, 250)
ACCENT = (245, 191, 89)
PLAYER_COLOR = (121, 190, 255)
ENEMY_COLOR = (243, 110, 110)

title_font = pygame.font.SysFont("consolas", 40)
body_font = pygame.font.SysFont("consolas", 24)


# Define explicit state constants for clarity.
STATE_MENU = "menu"
STATE_PLAY = "play"
STATE_GAME_OVER = "game_over"


# Mutable game data.
state = STATE_MENU
score_time = 0.0

player = pygame.Rect(80, 430, 52, 52)
player_speed = 340

enemy = pygame.Rect(780, 430, 60, 60)
enemy_speed = 310


def reset_round():
    """Reset positions and timer when entering play state."""
    global score_time
    player.x = 80
    player.y = 430
    enemy.x = random.randint(560, 820)
    enemy.y = 430
    score_time = 0.0


running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # State transitions are handled in one place for readability.
            if state == STATE_MENU and event.key == pygame.K_SPACE:
                reset_round()
                state = STATE_PLAY
            elif state == STATE_GAME_OVER and event.key == pygame.K_r:
                state = STATE_MENU

    # -------- UPDATE --------
    if state == STATE_PLAY:
        score_time += dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.y -= int(player_speed * dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.y += int(player_speed * dt)

        # Clamp player inside play area.
        player.clamp_ip(pygame.Rect(0, 80, WIDTH, HEIGHT - 80))

        # Enemy moves left constantly; once off screen, respawn right.
        enemy.x -= int(enemy_speed * dt)
        if enemy.right < 0:
            enemy.x = WIDTH + random.randint(40, 220)
            enemy.y = random.randint(80, HEIGHT - 60)

        # Collision means player loses.
        if player.colliderect(enemy):
            state = STATE_GAME_OVER

    # -------- DRAW --------
    screen.fill(BG)

    pygame.draw.line(screen, (44, 52, 69), (0, 80), (WIDTH, 80), 2)
    screen.blit(title_font.render("State Machine Runner", True, ACCENT), (20, 20))

    if state == STATE_MENU:
        screen.blit(body_font.render("Press SPACE to start", True, TEXT), (20, 100))
        screen.blit(body_font.render("Move with W/S or Up/Down", True, TEXT), (20, 132))
        screen.blit(body_font.render("Survive as long as possible", True, TEXT), (20, 164))

    elif state == STATE_PLAY:
        pygame.draw.rect(screen, PLAYER_COLOR, player, border_radius=10)
        pygame.draw.rect(screen, ENEMY_COLOR, enemy, border_radius=10)
        screen.blit(body_font.render(f"Time Survived: {score_time:0.2f}s", True, TEXT), (20, 100))

    elif state == STATE_GAME_OVER:
        pygame.draw.rect(screen, PLAYER_COLOR, player, border_radius=10)
        pygame.draw.rect(screen, ENEMY_COLOR, enemy, border_radius=10)
        screen.blit(body_font.render(f"Game Over - Survived: {score_time:0.2f}s", True, ENEMY_COLOR), (20, 100))
        screen.blit(body_font.render("Press R to return to menu", True, TEXT), (20, 132))

    pygame.display.flip()

pygame.quit()
