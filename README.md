# Fractal Pyramids

I made this for fun to see what a [T-square (fractal)](https://en.wikipedia.org/wiki/T-square_(fractal)) would look like as bases of pyramids. By default, the square branch relation is 1/2. The `factor` configuration allows you to adjust this manually, but it may yield unexpected results.

## Use

1. Install all packages in `requirement.txt`
1. Activate the virtual environment by running the following:
    ```bash
    source env/bin/activate
    ```
1. Run the following:
    ```bash
    python draw.py
    ```

You should get a window with the fractal pattern and a second window with a 3D scene of the fractal pyramids.

## Configuration

There is a `config.yml` file that comes with some options:

| Option | Type | Description |
| - | - | - |
| minimum_size | +int | The minimum length for half length/width of the pyramid base. Thus, a value of `1` will make it so the smallest pyramid base is `2` in length/width.
tile_size | +int | The size of the tile. This purely scales the whole pyramid up.
iterations | +int | Number of times the fractal pattern should occur. This indirectly decides the maximium pyramid base as it is just `minimum_size * factor ^ iterations`.
ignore_proper_fractal | bool | While developing, I did not account for the fractal pattern properly and always did the fractal pattern in all 4 corners. If this is `true`, it will always draw all 4 corners.
factor | +int | This is the growth factor of the pyramids. It's best to keep this at 2 as anything else seems to lead to weird behaviour (either limitations of the drawing or I did something wrong).
spacing | [+int, +int] | This provides a spacing per each set of iteration using the following formula: `spacing[0] * x + spacing[1]` where x is the current iteration.