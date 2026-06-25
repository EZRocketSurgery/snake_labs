"""
Mini Game 02: Collision Collector

Concept focus:
- Rect collision (AABB with pygame.Rect)
- Spawning collectibles
- Score and timer
- Using helper functions for game logic

Run:
    python game_02_collision_collect.py
"""

import random
import pygame


pygame.init()

WIDTH, HEIGHT = 900, 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game 02 - Collision Collector")
clock = pygame.time.Clock()


BG = (25, 28, 40)
PLAYER_COLOR = (120, 220, 170)
COIN_COLOR = (245, 202, 87)
TEXT = (235, 240, 248)
DANGER = (246, 123, 119)

title_font = pygame.font.SysFont("consolas", 34)
body_font = pygame.font.SysFont("consolas", 22)


player = pygame.Rect(430, 260, 48, 48)
player_speed = 320

coin = pygame.Rect(0, 0, 28, 28)

score = 0
time_left = 25.0


def place_coin_away_from_player(min_distance=120):
    """Place coin randomly, but not too close to player for better gameplay."""
    while True:
        coin.x = random.randint(20, WIDTH - coin.width - 20)
        coin.y = random.randint(80, HEIGHT - coin.height - 20)

        dx = coin.centerx - player.centerx
        dy = coin.centery - player.centery
        if (dx * dx + dy * dy) ** 0.5 >= min_distance:
            break


place_coin_away_from_player()


running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if time_left > 0:
        # Countdown only while game is active.
        time_left -= dt
        if time_left < 0:
            time_left = 0

        # Input controls player movement directly.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.x -= int(player_speed * dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.x += int(player_speed * dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.y -= int(player_speed * dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.y += int(player_speed * dt)

        # Keep player fully on screen.
        player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

        # Core collision concept:
        # colliderect returns True if rectangles overlap.
        if player.colliderect(coin):
            score += 1
            place_coin_away_from_player()

    # Drawing section.
    screen.fill(BG)
    pygame.draw.rect(screen, PLAYER_COLOR, player, border_radius=8)
    pygame.draw.rect(screen, (15, 18, 24), player, 2, border_radius=8)
    pygame.draw.ellipse(screen, COIN_COLOR, coin)
    pygame.draw.ellipse(screen, (140, 105, 35), coin, 2)

    screen.blit(title_font.render("Collision Collector", True, TEXT), (20, 14))
    screen.blit(body_font.render("Move: WASD or Arrows", True, TEXT), (20, 58))
    screen.blit(body_font.render(f"Score: {score}", True, TEXT), (20, 92))

    timer_color = DANGER if time_left < 7 else TEXT
    screen.blit(body_font.render(f"Time: {time_left:0.1f}", True, timer_color), (20, 126))

    if time_left <= 0:
        screen.blit(body_font.render("Time up! Close window to restart.", True, DANGER), (20, 164))

    pygame.display.flip()

pygame.quit()
