from __future__ import annotations

from pathlib import Path

import pygame

from .core.entities import Item, Reactor, Robot
from .core.grid import Grid, GridSpec
from .core.simulation import LabState
from .engine.input import InputMapper
from .engine.renderer import Renderer
from .utils.file_loader import load_json
from .utils.logger import get_logger


WINDOW_TITLE = "snake_labs"


def load_level(level_name: str = "sandbox") -> LabState:
    """Load a level JSON file and convert it into a runtime LabState."""
    level_path = Path(__file__).parent / "levels" / f"{level_name}.json"
    data = load_json(level_path)
    grid = Grid(GridSpec(data["cols"], data["rows"], data["tile_size"]))
    robot = Robot(**data["robot"], name="lab_robot")
    reactor = Reactor(**data["reactor"], name="reactor_core")
    items = [Item(name="crate", **item) for item in data.get("items", [])]
    return LabState(grid=grid, robot=robot, reactor=reactor, items=items, message=f'Loaded level: {data["name"]}')


def main() -> None:
    """Run the game loop: input -> simulation -> render."""
    logger = get_logger()
    pygame.init()

    state = load_level("sandbox")
    screen = pygame.display.set_mode((state.grid.spec.width, state.grid.spec.height))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()
    renderer = Renderer(screen, state.grid)
    input_mapper = InputMapper()

    running = True
    while running:
        # Keep the game speed stable and predictable for learning.
        clock.tick(60)

        # 1) Read events, 2) map to commands, 3) update simulation.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
            command = input_mapper.command_for_key(event)
            if command:
                state.step(command)

        # Render uses state only; it does not change gameplay logic.
        renderer.draw(state.robot, state.reactor, state.items, state.message, state.solved)
        pygame.display.flip()

    logger.info("Closing snake_labs cleanly.")
    pygame.quit()


if __name__ == "__main__":
    main()
