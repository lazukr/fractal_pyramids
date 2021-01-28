import yaml
import math
from PIL import Image, ImageDraw
from fractal import recursive_half_fractal
from scene import PyramidRender

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile)

MIN_SQUARE_SIZE = config['minimum_size']
ITERATIONS = config['iterations']
TILE_SIZE = config['tile_size']
IGNORE_PROPER_FRACTAL = config['ignore_proper_fractal']
FACTOR = config['factor']
SPACING = config['spacing']
SHOW_BLUEPRINT = config['show_blueprint']

INIT_SQUARE_SIZE = MIN_SQUARE_SIZE * FACTOR ** ITERATIONS
IMAGE_SIZE = 4 * INIT_SQUARE_SIZE + SPACING[0] * INIT_SQUARE_SIZE
CENTRE = IMAGE_SIZE / 2

SCALED_IMAGE_SIZE = IMAGE_SIZE * TILE_SIZE
SPACING = [SPACING[0] * x + SPACING[1] for x in range(ITERATIONS)]

if __name__ == '__main__':
    squares = recursive_half_fractal(INIT_SQUARE_SIZE, FACTOR, ITERATIONS, CENTRE, CENTRE, -1, IGNORE_PROPER_FRACTAL, SPACING, [])

    if (SHOW_BLUEPRINT):
        image_size = math.ceil(SCALED_IMAGE_SIZE);
        image = Image.new(mode='L', size=(image_size, image_size), color=255)
        draw = ImageDraw.Draw(image)
        for square in squares:
            x0 = square.x
            y0 = square.y
            x1 = x0 + square.size
            y1 = y0 + square.size
            sqaure_corners = [x0, y0, x1, y1]
            square_scaled = [x * TILE_SIZE for x in sqaure_corners]
            draw.rectangle(square_scaled, fill=128)
            
        del draw
        image.show()

    scene = PyramidRender(squares)
    scene.run()


