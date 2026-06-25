from __future__ import annotations

from dataclasses import dataclass, field

from .entities import Item, Reactor, Robot
from .grid import Grid
from .rules import can_collect, can_deliver, can_move


@dataclass(slots=True)
class LabState:
    """Mutable game state for one puzzle run.

    Keep this class focused on gameplay rules, not rendering details.
    """

    grid: Grid
    robot: Robot
    reactor: Reactor
    items: list[Item] = field(default_factory=list)
    turn_count: int = 0
    solved: bool = False
    message: str = "Booting lab..."

    def step(self, command: str | None) -> None:
        """Apply one player command to the state."""
        if self.solved:
            return

        self.turn_count += 1
        if command in {"up", "down", "left", "right"}:
            self._move_robot(command)
        elif command == "collect":
            self._collect_item()
        elif command == "deliver":
            self._deliver_item()
        elif command == "wait":
            self.message = "Waiting for the next instruction."

        # Keep a short movement history for debugging and UI feedback.
        self.robot.remember()
        if all(item.delivered for item in self.items):
            self.solved = True
            self.message = "Puzzle solved. Reactor stabilized."

    def _move_robot(self, command: str) -> None:
        delta = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0),
        }[command]
        next_col, next_row = can_move(self.grid, self.robot.col + delta[0], self.robot.row + delta[1])
        self.robot.col = next_col
        self.robot.row = next_row
        self.message = f"Robot moved {command}."

    def _collect_item(self) -> None:
        for item in self.items:
            if item.delivered:
                continue
            if can_collect(self.robot, item):
                self.robot.carrying = item.kind
                item.delivered = True
                self.message = f"Collected {item.kind}."
                return
        self.message = "No item to collect here."

    def _deliver_item(self) -> None:
        if not self.robot.carrying:
            self.message = "Robot is not carrying anything."
            return
        if can_deliver(self.robot, self.reactor):
            self.reactor.power += 1
            self.robot.carrying = None
            self.message = "Delivered item to the reactor."
            return
        self.message = "Move next to the reactor to deliver."
