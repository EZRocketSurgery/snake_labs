from __future__ import annotations

import pygame


class InputMapper:
    def command_for_key(self, event: pygame.event.Event) -> str | None:
        if event.type != pygame.KEYDOWN:
            return None

        if event.key in (pygame.K_w, pygame.K_UP):
            return "up"
        if event.key in (pygame.K_s, pygame.K_DOWN):
            return "down"
        if event.key in (pygame.K_a, pygame.K_LEFT):
            return "left"
        if event.key in (pygame.K_d, pygame.K_RIGHT):
            return "right"
        if event.key == pygame.K_e:
            return "collect"
        if event.key == pygame.K_q:
            return "deliver"
        if event.key == pygame.K_SPACE:
            return "wait"
        return None
