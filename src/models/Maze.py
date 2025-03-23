
from .Tile import Tile, Direction
from .Position2D import Position2D


MazeMatrix = list[list[Tile]]


class Maze:

    def __init__(self, width: int, height: int, exit_pos: Position2D) -> None:
        
        self._width: int = width
        self._height: int = height
        self._exit_pos: Position2D = exit_pos
        self._matrix: MazeMatrix = [[Tile.OpenTile(Position2D(i, j)) for i in range(width)] for j in range(height)]

        assert self.is_position_valid(exit_pos), f"Exit position {exit_pos} is out of bounds"

    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @property
    def exit_pos(self) -> Position2D:
        return self._exit_pos

    @property
    def matrix(self) -> MazeMatrix:
        return self._matrix
    
    def get_tile(self, pos: Position2D) -> Tile:

        if not self.is_position_valid(pos):
            raise IndexError(f"Position {pos} is out of bounds")
        
        return self.matrix[pos.y][pos.x]
    
    def set_tile(self, pos: Position2D, tile: Tile) -> None:
        
        if not self.is_position_valid(pos):
            raise IndexError(f"Position {pos} is out of bounds")

        self.matrix[pos.y][pos.x] = tile

    def is_position_valid(self, pos: Position2D) -> bool:
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height
    
    def get_accessible_neighbors(self, tile: Tile) -> list[Tile]:

        nb: list[Tile] = list()

        for direction in tile.Directions():
            nb_pos: Position2D = tile.get_neighbor_pos(direction)

            if self.is_position_valid(nb_pos):
                nb_tile: Tile = self.get_tile(nb_pos)
                if tile.is_accessible(nb_tile):
                    nb.append(nb_tile)

        return nb

    def add_walls(self, tile1: Tile, tile2: Tile) -> None:
        direction: Direction = tile1.get_direction(tile2)
        tile1.set_wall(direction, True)
        tile2.set_wall(direction.Opposite(), True)

    def remove_walls(self, tile1: Tile, tile2: Tile) -> None:
        direction: Direction = tile1.get_direction(tile2)
        tile1.set_wall(direction, False)
        tile2.set_wall(direction.Opposite(), False)

    def all_tiles(self) -> list[Tile]:
        return [tile for row in self.matrix for tile in row]
    
    def all_tiles_from_row(self, row: int) -> list[Tile]:

        if not 0 <= row < self.height:
            raise IndexError(f"Row {row} is out of bounds")
        
        return self.matrix[row]

    def all_tiles_from_column(self, column: int) -> list[Tile]:

        if not 0 <= column < self.width:
            raise IndexError(f"Column {column} is out of bounds")
        
        return [row[column] for row in self.matrix]