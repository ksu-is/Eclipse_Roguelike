from typing import Tuple

import numpy as np

graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool), #True/false condition for if tile can be walked on.
        ("transparent", np.bool), #True/false condition for if tile type blocks field of view.
        ("dark", graphic_dt), #Graphic for tiles outside player field of view.
    ]
)

def new_tile(
    *,
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype=tile_dt)

#foor and wall use attributes from previous variables to define their respective tile types.
floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord("#"), (255, 255, 255), (0, 0, 100)),
)