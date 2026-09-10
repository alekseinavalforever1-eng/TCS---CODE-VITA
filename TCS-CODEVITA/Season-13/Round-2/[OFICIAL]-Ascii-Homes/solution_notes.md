# Ascii Homes Solution

## Problem Description

The problem requires generating ASCII art for houses with specific dimensions and orientations (Up, Down, Left, Right, Horizontal). The houses must be aligned at the bottom baseline.

## Approach

### 1. Parsing Input

The input string (e.g., `6x3U 4x2U`) is split by spaces. Each part is parsed to extract:

- **Length (`L`)**: The width of the house.
- **Height (`H`)**: The height of the walls.
- **Direction (`D`)**: The orientation (`U`, `D`, `L`, `R`, `H`).

### 2. House Representation

A `House` class encapsulates the logic for a single house.

- **Dimensions**: We calculate the total width and height of the house based on its orientation.
  - `H` (Horizontal): Standard house.
  - `U` (Up): Tilted upwards.
  - `D` (Down): Tilted downwards.
  - `L` (Left): Tilted left.
  - `R` (Right): Tilted right.

### 3. Rendering

We create a 2D character grid (canvas) for each house.

- **Drawing Primitives**: Helper methods draw the roof (`/\`), inverted roof (`\/`), walls (`@` `&`), and base (`#`).
- **Orientation Logic**:
  - **H**: Standard roof on top of walls.
  - **U**: Roof, Base, Walls, Inverted Roof (based on visual interpretation of "Tilt Up").
  - **D**: Base, Walls, Inverted Roof.
  - **L**: Roof, Base, Walls, Base.
  - **R**: Roof, Walls, Roof, Walls.

### 4. Alignment and Output

- We determine the maximum height among all houses to establish a common canvas height.
- Each house is rendered into its own grid.
- We print the houses line by line, from top to bottom.
- Since houses must be bottom-aligned, we calculate the vertical offset for shorter houses.
- We concatenate the rows of each house (with padding for empty space) to form the final output lines.

## Compilation and Execution

### Java

```bash
cd A
javac Main.java
java Main
```

Input:

```text
6x3U 4x2U 8x4L 2x2H
```

## Files

- `Main.java`: The source code.
- `test_input.txt`: Sample input from the problem description.
