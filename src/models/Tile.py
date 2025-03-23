
from .Position2D import Position2D
from enum import Enum



class Direction(Enum):

    LEFT = 0,
    RIGHT = 1,
    TOP = 2,
    DOWN = 3,
    NONE = 4,

    def Opposite(self) -> 'Direction':

        match self:
            case Direction.LEFT:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.LEFT
            case Direction.TOP:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.TOP
            case _:
                return Direction.NONE

    @staticmethod
    def Directions() -> list['Direction']:
        return [Direction.LEFT, Direction.RIGHT, Direction.TOP, Direction.DOWN]


class Tile:

    def __init__(self, pos: Position2D, 
                 wleft: bool, wright: bool,
                 wtop: bool, wdown: bool) -> None:
        
        self._pos: Position2D = pos
        self._walls: dict[Direction, bool] = {
            Direction.LEFT: wleft,
            Direction.RIGHT: wright,
            Direction.TOP: wtop,
            Direction.DOWN: wdown
        }


    @classmethod
    def OpenTile(cls, pos: Position2D) -> 'Tile':
        return cls(pos, False, False, False, False)
    
    @classmethod
    def ClosedTile(cls, pos: Position2D) -> 'Tile':
        return cls(pos, True, True, True, True)


    @property
    def pos(self) -> Position2D:
        return self._pos


    @property
    def walls(self) -> dict[Direction, bool]:
        return self._walls
    
    @property
    def wall_left(self) -> bool:
        return self.walls[Direction.LEFT]
    
    @property
    def wall_right(self) -> bool:
        return self.walls[Direction.RIGHT]
    
    @property
    def wall_top(self) -> bool:
        return self.walls[Direction.TOP]
    
    @property
    def wall_down(self) -> bool:
        return self.walls[Direction.DOWN]
    
    def set_wall(self, direction: Direction, value: bool) -> None:

        if direction not in self.walls:
            raise ValueError(f"Invalid direction: {direction}")

        self.walls[direction] = value


    def get_neighbor_pos(self, direction: Direction) -> Position2D:

        match direction:
            case Direction.LEFT:
                return Position2D(self.pos.x - 1, self.pos.y)
            case Direction.RIGHT:
                return Position2D(self.pos.x + 1, self.pos.y)
            case Direction.TOP:
                return Position2D(self.pos.x, self.pos.y - 1)
            case Direction.DOWN:
                return Position2D(self.pos.x, self.pos.y + 1)
            case _:
                raise ValueError(f"Invalid direction: {direction}")
            
    def is_accessible(self, tile: 'Tile') -> bool:

        # we need to check if the tile is a neighbor of the current tile
        # and if the wall between them is open

        if tile.pos == self.get_neighbor_pos(Direction.LEFT):
            return not self.wall_left and not tile.wall_right
        elif tile.pos == self.get_neighbor_pos(Direction.RIGHT):
            return not self.wall_right and not tile.wall_left
        elif tile.pos == self.get_neighbor_pos(Direction.TOP):
            return not self.wall_top and not tile.wall_down
        elif tile.pos == self.get_neighbor_pos(Direction.DOWN):
            return not self.wall_down and not tile.wall_top
        else:
            return False

    def get_direction(self, neighbor: 'Tile') -> Direction:

        if neighbor.pos == self.get_neighbor_pos(Direction.LEFT):
            return Direction.LEFT
        elif neighbor.pos == self.get_neighbor_pos(Direction.RIGHT):
            return Direction.RIGHT
        elif neighbor.pos == self.get_neighbor_pos(Direction.TOP):
            return Direction.TOP
        elif neighbor.pos == self.get_neighbor_pos(Direction.DOWN):
            return Direction.DOWN
        else:
            raise ValueError(f"Tile {neighbor} is not a neighbor of {self}")

    def __repr__(self):
        # hash with pos and address
        return f"Tile @ {self.pos} @ {id(self)}"
    
    def __hash__(self):
        return hash(f'{self}')
    
    def __eq__(self, other: 'Tile') -> bool:
        return hash(self) == hash(other)
    
    def __ne__(self, other: 'Tile') -> bool:
        return not self.__eq__(other)

