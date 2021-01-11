import yaml
from PIL import Image, ImageDraw
from fractal import recursive_half_fractal
from scene import PyramidRender

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile)

print(config)

MIN_SQUARE_SIZE = config['Minimum_size']
ITERATIONS = config['Iterations']
TILE_SIZE = config['Tile_size']
IGNORE_PROPER_FRACTAL = config['Ignore_proper_fractal']

INIT_SQUARE_SIZE = MIN_SQUARE_SIZE * 2 ** ITERATIONS
IMAGE_SIZE = 4 * INIT_SQUARE_SIZE
CENTRE = IMAGE_SIZE // 2

SCALED_IMAGE_SIZE = IMAGE_SIZE * TILE_SIZE
SPACING = [0 for x in range(ITERATIONS)]



if __name__ == '__main__':
    squares = recursive_half_fractal(INIT_SQUARE_SIZE, ITERATIONS, CENTRE, CENTRE, -1, IGNORE_PROPER_FRACTAL, SPACING, [])
    image = Image.new(mode='L', size=(SCALED_IMAGE_SIZE, SCALED_IMAGE_SIZE), color=255)
    draw = ImageDraw.Draw(image)

    for square in squares:
        x0 = square.x
        y0 = square.y
        x1 = x0 + square.size
        y1 = y0 + square.size

        sqaure_corners = [x0, y0, x1, y1]
        square_scaled = [x * TILE_SIZE for x in sqaure_corners]

        draw.rectangle(square_scaled, fill=128)
        #print(square.show())

    del draw
    image.show()

    scene = PyramidRender(squares)
    scene.run()

