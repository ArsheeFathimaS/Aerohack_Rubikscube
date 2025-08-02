# Rubik's Cube Solver

A Python implementation of the two-phase algorithm for solving the Rubik's Cube, featuring both a graphical interface and a terminal solver.

## Features

- Graphical interface for interactive cube solving
- Terminal-based solver for quick solutions
- Efficient implementation that solves cubes in less than 20 moves on average
- Support for random cube generation

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd RubiksCube-TwophaseSolver
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

### Graphical Interface

Run the GUI solver:
```bash
python client_gui.py
```

The GUI features:
- Interactive cube face coloring
- Color picker for easy input
- Random scramble generation
- One-click solving
- Solution display

Buttons:
- "Solve" - Find solution for current cube state
- "Clean" - Reset to solved cube
- "Empty" - Clear all colors except centers
- "Random" - Generate random scramble

### Terminal Solver

Run the terminal solver:
```bash
python test_solver.py
```

To solve a different cube, edit the `cubestring` in `test_solver.py`. The cube string format is a 54-character string representing the cube faces in the order: Up, Right, Front, Down, Left, Back (URFDLB).

Example cube string:
```python
cubestring = "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL"
```

## Cube String Format

The cube string consists of 54 characters representing the colors of the cube faces:
- U = Up (Yellow)
- R = Right (Green)
- F = Front (Red)
- D = Down (White)
- L = Left (Blue)
- B = Back (Orange)

Each face is represented by 9 characters, read from left to right, top to bottom.

## Solution Format

Solutions are displayed in standard cube notation:
- U, R, F, D, L, B = clockwise face turns
- U2, R2, F2, D2, L2, B2 = 180-degree turns
- U', R', F', D', L', B' = counterclockwise turns

Example solution:
```
L' U B R2 F' L F' U2 L U' B' U2 B L2 F U2 R2 L2 B2
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.