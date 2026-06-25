from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Entity:
    col: int
    row: int
    name: str = "entity"


@dataclass(slots=True)
class Item(Entity):
    kind: str = "cube"
    delivered: bool = False


@dataclass(slots=True)
class Reactor(Entity):
    power: int = 0


@dataclass(slots=True)
class Robot(Entity):
    program: list[str] = field(default_factory=list)
    carrying: str | None = None
    path_history: list[tuple[int, int]] = field(default_factory=list)

    def remember(self) -> None:
        self.path_history.append((self.col, self.row))
        if len(self.path_history) > 24:
            self.path_history.pop(0)
