from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TileStyle:
    name: str
    fill: tuple[int, int, int]
    edge: tuple[int, int, int]


FLOOR = TileStyle("floor", (35, 43, 56), (64, 75, 92))
WALL = TileStyle("wall", (23, 27, 36), (79, 90, 108))
PLATFORM = TileStyle("platform", (56, 64, 80), (120, 131, 150))
