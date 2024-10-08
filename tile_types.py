from typing import Tuple

import numpy as np  # type: ignore
import color

# Tile graphics compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bits for RGB.
        ("bg", "3B"),
    ]
)

# Tile struct used for static tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked on.
        ("transparent", np.bool),  # True if doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when tile is not in FOV.
        ("light", graphic_dt),  # Graphics for when the tile is in FOV.
    ]
)


def new_tile(
    *,  # Enforce use of keywords so param order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """
    Helper function for defining individual tile types
    """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), color.white, (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), color.white, (50, 50, 150)),
    light=(ord(" "), color.white, (200, 180, 50)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), color.white, (0, 0, 100)),
    light=(ord(" "), color.white, (130, 110, 50)),
)
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord("#"), (0, 0, 100), (50, 50, 150)),
    light=(ord("#"), color.white, (200, 180, 50)),
)
