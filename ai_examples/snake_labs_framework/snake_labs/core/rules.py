from __future__ import annotations

from .entities import Item, Reactor, Robot
from .grid import Grid


def can_move(grid: Grid, col: int, row: int) -> tuple[int, int]:
    return grid.clamp_cell(col, row)


def is_adjacent(left: tuple[int, int], right: tuple[int, int]) -> bool:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) == 1


def can_collect(robot: Robot, item: Item) -> bool:
    return robot.carrying is None and (robot.col, robot.row) == (item.col, item.row)


def can_deliver(robot: Robot, reactor: Reactor) -> bool:
    return robot.carrying is not None and is_adjacent((robot.col, robot.row), (reactor.col, reactor.row))
