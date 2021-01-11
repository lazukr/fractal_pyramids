from typing import List
from utils import Square
from PIL import Image, ImageDraw

def recursive_half_fractal(size: int, iterations: int, x: int, y: int, parent_direction: int, ignore_parent_directon: bool, spacing: List[int], accumulated_list: List[Square]) -> List[Square]:
    square = Square(size, x, y)
    accumulated_list.append(square)

    if iterations <= 1 or size <= 2:
        return accumulated_list
    else:
        iterations -= 1
        size = size // 2

        left = x - size
        right = x + size
        top = y - size
        bottom = y + size

        half_next_size = size // 2 + spacing[iterations]
        # top left
        if (parent_direction != 0 or ignore_parent_directon == True):
            accumulated_list + recursive_half_fractal(size, iterations, left - half_next_size, top - half_next_size, 11, ignore_parent_directon, spacing, accumulated_list)
        # top right
        if (parent_direction != 1 or ignore_parent_directon == True):
            accumulated_list + recursive_half_fractal(size, iterations, right + half_next_size, top - half_next_size, 10, ignore_parent_directon, spacing, accumulated_list)
        # bottom left
        if (parent_direction != 10 or ignore_parent_directon == True):
            accumulated_list + recursive_half_fractal(size, iterations, left - half_next_size, bottom + half_next_size, 1, ignore_parent_directon, spacing, accumulated_list)
        # bottom right
        if (parent_direction != 11 or ignore_parent_directon == True):
            accumulated_list + recursive_half_fractal(size, iterations, right + half_next_size, bottom + half_next_size, 0, ignore_parent_directon, spacing, accumulated_list)
        
        return accumulated_list
