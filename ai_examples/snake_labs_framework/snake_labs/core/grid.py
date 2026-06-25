from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GridSpec:
    cols: int
    rows: int
    tile_size: int

    @property
    def width(self) -> int:
        return self.cols * self.tile_size

    @property
    def height(self) -> int:
        return self.rows * self.tile_size


@dataclass(slots=True)
class Grid:
    spec: GridSpec

    def clamp_cell(self, col: int, row: int) -> tuple[int, int]:
        col = max(0, min(self.spec.cols - 1, col))
        row = max(0, min(self.spec.rows - 1, row))
        return col, row

    def world_to_cell(self, x: float, y: float) -> tuple[int, int]:
        return self.clamp_cell(int(x) // self.spec.tile_size, int(y) // self.spec.tile_size)

    def cell_to_world(self, col: int, row: int) -> tuple[int, int]:
        col, row = self.clamp_cell(col, row)
        return col * self.spec.tile_size, row * self.spec.tile_size
