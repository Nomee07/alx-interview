#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): The grid where 0 represents water

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for the current land cell
                perimeter += 4

                # Check if the cell above is land, then subtract 2
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Check if the cell to the left is land, then subtract 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
