SnakeLabs Framework (Teaching Version)
=====================================

This folder is designed to teach how a small pygame project is structured.
The goal is not advanced architecture. The goal is to read one file at a time and understand how each part works.

Quick Start
-----------

1. Open a terminal in this folder:

	`ai_examples/snake_labs_framework`

2. Run:

	`python main.py`

3. Play with controls:

	- `WASD` or arrow keys: move
	- `E`: collect item on current tile
	- `Q`: deliver item when next to reactor
	- `Space`: wait one turn

How To Read This Code
---------------------

Read in this order:

1. `main.py`
	- The tiniest launcher possible.
	- It only calls `snake_labs.cli.main()`.

2. `snake_labs/cli.py`
	- The full game loop lives here.
	- You can see setup, input, simulation step, and rendering in one place.

3. `snake_labs/core/simulation.py`
	- The game rules are applied here.
	- This file answers: "What happens when the player presses a key?"

4. `snake_labs/core/rules.py`
	- Small pure functions for movement/collection/delivery checks.

5. `snake_labs/engine/renderer.py`
	- Draws everything on the screen.
	- No gameplay decisions happen here.

6. `snake_labs/levels/sandbox.json`
	- Data-only level file.
	- Change coordinates to experiment without editing Python logic.

Mental Model
------------

Each frame follows this sequence:

1. Read keyboard input.
2. Convert key into a command string.
3. Apply command to `LabState`.
4. Draw the new state.
5. Repeat.

If you keep this loop in mind, the rest of the project becomes much easier to understand.

Beginner Exercises
------------------

1. In `sandbox.json`, move the reactor to a new tile.
2. In `simulation.py`, change the win message.
3. In `input.py`, map another key to `wait`.
4. Add a second level JSON and load it by name in `cli.py`.
