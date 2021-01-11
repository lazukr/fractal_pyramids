# Fractal Pyramids

I made this for fun to see what a [T-square (fractal)](https://en.wikipedia.org/wiki/T-square_(fractal)) would look like as bases of pyramids. **This strictly uses square branches related by 1/2.**

## Use

1. Install all packages in `requirement.txt`
1. Run:
    ```bash
    python draw.py
    ```

You should get a window with the fractal pattern and a second window with a 3D scene of the fractal pyramids.

## Configuration

There is a `config.yml` file that comes with some options:

| Option | Type | Description |
| - | - | - |
| Minimum_size | +Integer | The minimum length for half length/width of the pyramid base. Thus, a value of `1` will make it so the smallest pyramid base is `2` in length/width.
Tile_size | +Integer | The size of the tile. This purely scales the whole pyramid up.
Iterations | +Integer | Number of times the fractal pattern should occur. This indirectly decides the maximium pyramid base as it is just `Minimum_size * 2 ^ Iterations`.
Ignore_proper_fractal | Boolean | While developing, I did not account for the fractal pattern properly and always did the fractal pattern in all 4 corners. If this is `true`, it will always draw all 4 corners.