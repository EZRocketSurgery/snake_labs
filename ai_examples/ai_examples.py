"""
Very small "idle game" example for learning Pygame.

How to run:
	python ai_examples.py

What to observe while it runs:
1. Manual clicks give coins instantly.
2. Passive income (coins per second) is added over time.
3. Upgrades increase how fast coins are generated.
4. The UI is redrawn every frame from the current game state.

This file is intentionally full of comments so you can read it like a tutorial.
"""

import pygame


# -----------------------------
# Basic Pygame setup
# -----------------------------
# You must initialize Pygame before creating windows, fonts, clocks, etc.
pygame.init()

# Screen dimensions and title.
WIDTH, HEIGHT = 900, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Idle Coins - Pygame Learning Example")

# Clock controls how fast the game loop runs.
# We target 60 FPS, but game logic uses delta-time so speed stays stable.
clock = pygame.time.Clock()


# -----------------------------
# Colors and fonts
# -----------------------------
# RGB format: (red, green, blue), each 0-255.
BG = (22, 27, 36)
PANEL = (36, 44, 58)
BUTTON = (74, 163, 223)
BUTTON_HOVER = (98, 185, 245)
TEXT = (235, 240, 250)
ACCENT = (245, 196, 90)
SUCCESS = (110, 204, 137)

# Default system font for portability.
title_font = pygame.font.SysFont("consolas", 42)
main_font = pygame.font.SysFont("consolas", 28)
small_font = pygame.font.SysFont("consolas", 20)


# -----------------------------
# Game state variables
# -----------------------------
# These variables represent the entire "state" of our idle game.
coins = 0.0
coins_per_click = 1.0
coins_per_second = 0.0

# Upgrade levels start at 0 and increase as player buys them.
click_upgrade_level = 0
idle_upgrade_level = 0

# Costs start small and increase after each purchase.
click_upgrade_cost = 15.0
idle_upgrade_cost = 25.0

# For a tiny visual reward, we track click flashes.
click_flash_timer = 0.0


# -----------------------------
# UI geometry (rectangles)
# -----------------------------
# Pygame often uses pygame.Rect for button hit-testing and drawing.
coin_button_rect = pygame.Rect(100, 160, 280, 280)
click_upgrade_rect = pygame.Rect(470, 190, 330, 95)
idle_upgrade_rect = pygame.Rect(470, 315, 330, 95)


# -----------------------------
# Helper functions
# -----------------------------
def draw_text(text, font, color, x, y):
	"""Render text and draw it at (x, y)."""
	surface = font.render(text, True, color)
	screen.blit(surface, (x, y))


def format_number(value):
	"""
	Keep numbers readable.
	- Small values show 1 decimal.
	- Bigger values use integer formatting with commas.
	"""
	if value < 1000:
		return f"{value:.1f}"
	return f"{value:,.0f}"


def draw_button(rect, label, can_afford):
	"""
	Draw a simple button.
	- Button changes color when mouse is over it.
	- Label color indicates whether player can afford it.
	"""
	mouse_pos = pygame.mouse.get_pos()
	hovered = rect.collidepoint(mouse_pos)

	color = BUTTON_HOVER if hovered else BUTTON
	pygame.draw.rect(screen, color, rect, border_radius=12)
	pygame.draw.rect(screen, (12, 16, 24), rect, 2, border_radius=12)

	label_color = TEXT if can_afford else (180, 180, 180)
	draw_text(label, small_font, label_color, rect.x + 14, rect.y + 12)


# -----------------------------
# Main game loop
# -----------------------------
# This loop runs until user closes the window.
running = True
while running:
	# Delta-time (seconds since previous frame).
	# This makes idle income frame-rate independent.
	dt = clock.tick(60) / 1000.0

	# 1) INPUT: read events from OS (mouse, keyboard, close button, etc).
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			mouse_pos = event.pos

			# Clicking the big coin gives manual income.
			if coin_button_rect.collidepoint(mouse_pos):
				coins += coins_per_click
				click_flash_timer = 0.12

			# Clicking upgrade buttons attempts a purchase.
			if click_upgrade_rect.collidepoint(mouse_pos) and coins >= click_upgrade_cost:
				coins -= click_upgrade_cost
				click_upgrade_level += 1

				# Increase click power with each level.
				coins_per_click += 0.75

				# Cost scales up after every buy.
				click_upgrade_cost *= 1.55

			if idle_upgrade_rect.collidepoint(mouse_pos) and coins >= idle_upgrade_cost:
				coins -= idle_upgrade_cost
				idle_upgrade_level += 1

				# Increase passive generation each level.
				coins_per_second += 0.8

				# Cost scales too, usually a bit steeper.
				idle_upgrade_cost *= 1.7

	# 2) UPDATE: advance game state.
	# Passive income happens continuously using delta-time.
	coins += coins_per_second * dt

	# Reduce click flash timer to animate feedback.
	if click_flash_timer > 0:
		click_flash_timer -= dt
		if click_flash_timer < 0:
			click_flash_timer = 0

	# 3) DRAW: clear screen and redraw everything every frame.
	screen.fill(BG)

	# Top title and stats panel.
	draw_text("Idle Coins", title_font, ACCENT, 32, 26)
	pygame.draw.rect(screen, PANEL, (28, 88, WIDTH - 56, 58), border_radius=10)
	draw_text(f"Coins: {format_number(coins)}", main_font, TEXT, 42, 102)
	draw_text(f"Per click: {coins_per_click:.2f}", small_font, TEXT, 365, 106)
	draw_text(f"Per second: {coins_per_second:.2f}", small_font, SUCCESS, 590, 106)

	# Big coin button.
	coin_color = (255, 214, 102) if click_flash_timer > 0 else (240, 190, 74)
	pygame.draw.ellipse(screen, coin_color, coin_button_rect)
	pygame.draw.ellipse(screen, (180, 136, 44), coin_button_rect, 4)
	draw_text("CLICK", main_font, (75, 52, 10), coin_button_rect.x + 88, coin_button_rect.y + 114)

	# Upgrade buttons with affordability logic.
	click_label = (
		f"Upgrade Click (Lv {click_upgrade_level}) - Cost {format_number(click_upgrade_cost)}"
	)
	idle_label = (
		f"Upgrade Idle  (Lv {idle_upgrade_level}) - Cost {format_number(idle_upgrade_cost)}"
	)

	draw_button(click_upgrade_rect, click_label, coins >= click_upgrade_cost)
	draw_button(idle_upgrade_rect, idle_label, coins >= idle_upgrade_cost)

	# Helpful learning note at the bottom.
	draw_text(
		"Tip: game state lives in variables; draw reads that state each frame.",
		small_font,
		(170, 188, 210),
		30,
		HEIGHT - 34,
	)

	# Push everything drawn this frame to the actual window.
	pygame.display.flip()


# Shutdown cleanly when loop exits.
pygame.quit()