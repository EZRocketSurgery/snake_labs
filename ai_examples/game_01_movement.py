"""
Mini Game 01: Movement Lab

Concept focus:
- Keyboard input
- Velocity and acceleration
- Delta-time (frame-rate independent movement)
- Simple world boundaries

Run:
    python game_01_movement.py
"""

import pygame


pygame.init()

WIDTH, HEIGHT = 900, 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game 01 - Movement Lab")
clock = pygame.time.Clock()


# Basic colors used for drawing.
BG = (19, 24, 34)
GRID = (40, 48, 63)
PLAYER = (100, 190, 255)
TEXT = (230, 236, 245)
ACCENT = (245, 195, 95)


# Default font from system for portability.
title_font = pygame.font.SysFont("consolas", 34)
body_font = pygame.font.SysFont("consolas", 22)


# Player is represented by a rectangle.
player = pygame.Rect(420, 250, 55, 55)

# Velocity is separate from position to show motion mechanics clearly.
vx = 0.0
vy = 0.0

# Tunable movement parameters.
accel = 1200.0     # How quickly the player speeds up while key is held.
friction = 800.0  # How quickly velocity decays when no key is held.
max_speed = 380.0


def draw_grid(spacing=40):
    """Draw a simple background grid so movement is easy to observe."""
    for x in range(0, WIDTH, spacing):
        pygame.draw.line(screen, GRID, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, spacing):
        pygame.draw.line(screen, GRID, (0, y), (WIDTH, y), 1)


def approach_zero(value, amount):
    """
    Move a value toward zero by a fixed amount.
    Useful for friction-like behavior.
    """
    if value > 0:
        return max(0.0, value - amount)
    if value < 0:
        return min(0.0, value + amount)
    return 0.0


running = True
while running:
    # dt = seconds since last frame; movement uses dt so it behaves similarly at 30/60/144 FPS.
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Poll keyboard each frame.
    keys = pygame.key.get_pressed()

    # Horizontal input creates acceleration.
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        vx -= accel * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        vx += accel * dt

    # Vertical input creates acceleration.
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        vy -= accel * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        vy += accel * dt

    # If no key is held for an axis, apply friction toward zero.
    if not (keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_d] or keys[pygame.K_RIGHT]):
        vx = approach_zero(vx, friction * dt)
    if not (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_s] or keys[pygame.K_DOWN]):
        vy = approach_zero(vy, friction * dt)

    # Clamp top speed so velocity stays manageable.
    vx = max(-max_speed, min(max_speed, vx))
    vy = max(-max_speed, min(max_speed, vy))

    # Update position using current velocity.
    player.x += int(vx * dt)
    player.y += int(vy * dt)

    # Keep player in bounds. If collision with wall happens, stop movement in that direction.
    if player.left < 0:
        player.left = 0
        vx = 0.0
    if player.right > WIDTH:
        player.right = WIDTH
        vx = 0.0
    if player.top < 0:
        player.top = 0
        vy = 0.0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        vy = 0.0

    # Draw everything.
    screen.fill(BG)
    draw_grid()

    pygame.draw.rect(screen, PLAYER, player, border_radius=10)
    pygame.draw.rect(screen, (10, 14, 20), player, 2, border_radius=10)

    screen.blit(title_font.render("Movement Lab", True, ACCENT), (20, 16))
    screen.blit(body_font.render("Move: WASD or Arrow Keys", True, TEXT), (20, 64))
    screen.blit(body_font.render(f"vx: {vx:7.2f}", True, TEXT), (20, HEIGHT - 70))
    screen.blit(body_font.render(f"vy: {vy:7.2f}", True, TEXT), (20, HEIGHT - 42))

    pygame.display.flip()

pygame.quit()
