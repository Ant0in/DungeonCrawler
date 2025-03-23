
import random


class Position2D:

    def __init__(self, x: int, y: int) -> None:
        
        self._x: int = x
        self._y: int = y

    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y
    
    @property
    def coords(self) -> tuple[int, int]:
        return self.x, self.y
    
    def set_coords(self, x: int, y: int) -> None:
        self._x = x
        self._y = y
    
    def __eq__(self, other: 'Position2D') -> bool:
        return self.coords == other.coords
    
    def __hash__(self) -> int:
        return hash(self.coords)
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def manhattan_distance(self, other: 'Position2D') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def random_position(max_x: int, max_y: int, excluded: set | None) -> 'Position2D':

        if excluded is None: excluded = set()
        assert len(excluded) < max_x * max_y, "Too many excluded positions"

        while True:
            pos = Position2D(random.randint(0, max_x), random.randint(0, max_y))
            if pos not in excluded: return pos

