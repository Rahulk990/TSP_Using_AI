from random import randint
from typing import Tuple

class City:

    # Random Initialization if not specified
    def __init__(self, x: float = None, y: float = None) -> None:
        self.x = x if (x) else randint(0, 200)
        self.y = y if (y) else randint(0, 200)

    def getCity(self) -> Tuple[float, float]:
        return self.x, self.y
