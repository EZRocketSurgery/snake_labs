"""
Mini Game 04: Timers and Particles

Concept focus:
- Timed spawning (every N seconds)
- Short-lived particle effects
- List update/removal patterns

Run:
    python game_04_timers_particles.py
"""

import random
import pygame


pygame.init()

WIDTH, HEIGHT = 900, 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game 04 - Timers and Particles")
clock = pygame.time.Clock()


BG = (17, 22, 30)
TEXT = (232, 239, 248)
SPAWN_COLOR = (255, 189, 92)
PARTICLE_COLOR = (120, 198, 255)
CURSOR_COLOR = (160, 242, 183)

title_font = pygame.font.SysFont("consolas", 34)
body_font = pygame.font.SysFont("consolas", 22)


# Targets are simple circles represented by dicts.
targets = []

# Particles are tiny moving squares with life timers.
particles = []

score = 0

# Spawn a new target every 1.0 second.
spawn_interval = 1.0
spawn_timer = 0.0


def spawn_target():
    """Create one target at a random position with random size."""
    radius = random.randint(14, 28)
    x = random.randint(radius + 10, WIDTH - radius - 10)
    y = random.randint(radius + 80, HEIGHT - radius - 10)
    # Store as dict so fields are explicit and readable.
    targets.append({"x": x, "y": y, "r": radius})


def burst_particles(x, y):
    """Create a quick burst for visual feedback when target is clicked."""
    for _ in range(18):
        particles.append(
            {
                "x": float(x),
                "y": float(y),
                "vx": random.uniform(-220, 220),
                "vy": random.uniform(-220, 220),
                "life": random.uniform(0.25, 0.6),
                "size": random.randint(3, 6),
            }
        )


running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos

            # Check targets from end to front; we may remove one on hit.
            for i in range(len(targets) - 1, -1, -1):
                t = targets[i]
                dx = mx - t["x"]
                dy = my - t["y"]

                # Circle hit test using distance squared.
                if dx * dx + dy * dy <= t["r"] * t["r"]:
                    score += 1
                    burst_particles(t["x"], t["y"])
                    targets.pop(i)
                    break

    # Timed spawning concept:
    # Add dt to timer, and spawn each time threshold is crossed.
    spawn_timer += dt
    while spawn_timer >= spawn_interval:
        spawn_target()
        spawn_timer -= spawn_interval

    # Update particles and remove dead ones.
    # Iterate backward so pop(i) is safe.
    for i in range(len(particles) - 1, -1, -1):
        p = particles[i]
        p["x"] += p["vx"] * dt
        p["y"] += p["vy"] * dt
        p["life"] -= dt
        if p["life"] <= 0:
            particles.pop(i)

    # Draw scene.
    screen.fill(BG)

    for t in targets:
        pygame.draw.circle(screen, SPAWN_COLOR, (int(t["x"]), int(t["y"])), t["r"])
        pygame.draw.circle(screen, (136, 95, 44), (int(t["x"]), int(t["y"])), t["r"], 2)

    for p in particles:
        pygame.draw.rect(
            screen,
            PARTICLE_COLOR,
            (int(p["x"]), int(p["y"]), p["size"], p["size"]),
        )

    # Draw a simple custom crosshair at mouse position.
    mx, my = pygame.mouse.get_pos()
    pygame.draw.line(screen, CURSOR_COLOR, (mx - 10, my), (mx + 10, my), 2)
    pygame.draw.line(screen, CURSOR_COLOR, (mx, my - 10), (mx, my + 10), 2)

    screen.blit(title_font.render("Timers and Particles", True, TEXT), (20, 16))
    screen.blit(body_font.render("Click circles before screen fills up", True, TEXT), (20, 58))
    screen.blit(body_font.render(f"Score: {score}", True, TEXT), (20, 90))
    screen.blit(body_font.render(f"Targets: {len(targets)}", True, TEXT), (20, 122))
    screen.blit(body_font.render(f"Particles: {len(particles)}", True, TEXT), (20, 154))

    pygame.display.flip()

pygame.quit()
