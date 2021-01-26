from typing import List
from utils import Square

TOP_LEFT = 0
TOP_RIGHT = 1
BOTTOM_LEFT = 10
BOTTOM_RIGHT = 11

def recursive_half_fractal(size: int, factor: int, iterations: int, x: int, y: int, parent_direction: int, ignore_parent_directon: bool, spacing: List[int], accumulated_list: List[Square]) -> List[Square]:
    square = Square(size, x, y)
    accumulated_list.append(square)

    if iterations <= 1 or size <= factor:
        return accumulated_list
    else:
        iterations -= 1
        size = size // factor

        left = x - size
        right = x + size
        top = y - size
        bottom = y + size

        half_next_size = size // factor + spacing[iterations]
        # top left
        if (parent_direction != TOP_LEFT or ignore_parent_directon):
            accumulated_list + recursive_half_fractal(size, factor, iterations, left - half_next_size, top - half_next_size, BOTTOM_RIGHT, ignore_parent_directon, spacing, accumulated_list)
        # top right
        if (parent_direction != TOP_RIGHT or ignore_parent_directon):
            accumulated_list + recursive_half_fractal(size, factor, iterations, right + half_next_size, top - half_next_size, BOTTOM_LEFT, ignore_parent_directon, spacing, accumulated_list)
        # bottom left
        if (parent_direction != BOTTOM_LEFT or ignore_parent_directon):
            accumulated_list + recursive_half_fractal(size, factor, iterations, left - half_next_size, bottom + half_next_size, TOP_RIGHT, ignore_parent_directon, spacing, accumulated_list)
        # bottom right
        if (parent_direction != BOTTOM_RIGHT or ignore_parent_directon):
            accumulated_list + recursive_half_fractal(size, factor, iterations, right + half_next_size, bottom + half_next_size, TOP_LEFT, ignore_parent_directon, spacing, accumulated_list)
        
        return accumulated_list
