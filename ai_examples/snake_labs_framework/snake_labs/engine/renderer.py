from __future__ import annotations

import pygame

from ..core.entities import Item, Reactor, Robot
from ..core.grid import Grid
from ..core.tiles import FLOOR, PLATFORM, WALL


class Renderer:
    def __init__(self, screen: pygame.Surface, grid: Grid) -> None:
        self.screen = screen
        self.grid = grid
        self.font_title = pygame.font.SysFont("consolas", 28, bold=True)
        self.font_body = pygame.font.SysFont("consolas", 18)

    def draw(self, robot: Robot, reactor: Reactor, items: list[Item], message: str, solved: bool) -> None:
        self._draw_background()
        self._draw_grid()
        self._draw_reactor(reactor)
        for item in items:
            self._draw_item(item)
        self._draw_robot(robot)
        self._draw_ui(message, solved, robot)

    def _draw_background(self) -> None:
        self.screen.fill((17, 21, 31))
        for y in range(0, self.grid.spec.height, 64):
            pygame.draw.line(self.screen, (26, 32, 45), (0, y), (self.grid.spec.width, y), 1)

    def _draw_grid(self) -> None:
        tile = self.grid.spec.tile_size
        for row in range(self.grid.spec.rows):
            for col in range(self.grid.spec.cols):
                rect = pygame.Rect(col * tile, row * tile, tile, tile)
                style = FLOOR if (col + row) % 2 == 0 else PLATFORM
                pygame.draw.rect(self.screen, style.fill, rect)
                pygame.draw.rect(self.screen, style.edge, rect, 1)
        border = pygame.Rect(0, 0, self.grid.spec.width, self.grid.spec.height)
        pygame.draw.rect(self.screen, WALL.edge, border, 4)

    def _draw_robot(self, robot: Robot) -> None:
        x, y = self.grid.cell_to_world(robot.col, robot.row)
        tile = self.grid.spec.tile_size
        center = (x + tile // 2, y + tile // 2)
        body_radius = tile // 2 - 7
        pygame.draw.circle(self.screen, (255, 174, 107), center, body_radius)
        pygame.draw.circle(self.screen, (57, 62, 84), center, body_radius, 3)
        eye_offset = 9
        pygame.draw.circle(self.screen, (236, 247, 255), (center[0] - eye_offset, center[1] - 4), 6)
        pygame.draw.circle(self.screen, (236, 247, 255), (center[0] + eye_offset, center[1] - 4), 6)
        pygame.draw.circle(self.screen, (30, 36, 51), (center[0] - eye_offset, center[1] - 4), 2)
        pygame.draw.circle(self.screen, (30, 36, 51), (center[0] + eye_offset, center[1] - 4), 2)
        if robot.carrying:
            cube_rect = pygame.Rect(center[0] - 9, center[1] + 11, 18, 18)
            pygame.draw.rect(self.screen, (104, 210, 255), cube_rect, border_radius=4)
            pygame.draw.rect(self.screen, (211, 248, 255), cube_rect, 2, border_radius=4)

    def _draw_item(self, item: Item) -> None:
        if item.delivered:
            return
        x, y = self.grid.cell_to_world(item.col, item.row)
        tile = self.grid.spec.tile_size
        rect = pygame.Rect(x + tile // 2 - 12, y + tile // 2 - 12, 24, 24)
        pygame.draw.rect(self.screen, (113, 227, 255), rect, border_radius=5)
        pygame.draw.rect(self.screen, (245, 245, 255), rect, 2, border_radius=5)

    def _draw_reactor(self, reactor: Reactor) -> None:
        x, y = self.grid.cell_to_world(reactor.col, reactor.row)
        tile = self.grid.spec.tile_size
        base = pygame.Rect(x + 6, y + 10, tile - 12, tile - 14)
        pygame.draw.rect(self.screen, (67, 82, 107), base, border_radius=10)
        pygame.draw.rect(self.screen, (147, 164, 190), base, 2, border_radius=10)
        glow_center = (base.centerx, base.centery)
        pygame.draw.circle(self.screen, (249, 177, 79), glow_center, 16)
        pygame.draw.circle(self.screen, (255, 221, 127), glow_center, 8)

    def _draw_ui(self, message: str, solved: bool, robot: Robot) -> None:
        panel = pygame.Rect(0, self.grid.spec.height - 84, self.grid.spec.width, 84)
        pygame.draw.rect(self.screen, (13, 16, 24), panel)
        pygame.draw.line(self.screen, (84, 96, 117), panel.topleft, panel.topright, 2)
        title = "SnakeLabs Prototype" if not solved else "SnakeLabs Prototype - Complete"
        self.screen.blit(self.font_title.render(title, True, (249, 178, 81)), (18, self.grid.spec.height - 76))
        self.screen.blit(self.font_body.render(message, True, (227, 235, 244)), (18, self.grid.spec.height - 44))
        carrying = robot.carrying or "nothing"
        status = f"carrying: {carrying}   turns: {len(robot.path_history)}"
        self.screen.blit(self.font_body.render(status, True, (145, 180, 220)), (self.grid.spec.width - 270, self.grid.spec.height - 44))
