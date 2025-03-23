
from .Position2D import Position2D
from .Maze import Maze
from .Tile import Direction


class Player:

    def __init__(self, pos: Position2D, view_radius: int) -> None:
        self._pos: Position2D = pos
        self._view_radius: int = view_radius

    @property
    def pos(self) -> Position2D:
        return self._pos
    
    @property
    def view_radius(self) -> int:
        return self._view_radius
    
    def set_pos(self, new_pos: Position2D) -> None:
        self._pos = new_pos

    def set_view_radius(self, new_radius: int) -> None:
        self._view_radius = new_radius

    def is_visible(self, pos: Position2D) -> bool:
        return self.pos.manhattan_distance(pos) <= self.view_radius
    
    def move(self, maze: Maze, direction: Direction) -> bool:
        
        new_pos: Position2D = maze.get_tile(self.pos).get_neighbor_pos(direction)
        current_tile = maze.get_tile(self.pos)

        if not maze.is_position_valid(new_pos):
            return False
        
        destination_tile = maze.get_tile(new_pos)
        if current_tile.is_accessible(destination_tile):
            self.set_pos(new_pos)
            return True
        
        else:
            return False

    def has_exited(self, maze: Maze) -> bool:
        return self.pos == maze.exit_pos

    def __str__(self) -> str:
        return f"Player at {self.pos} with view radius {self.view_radius}"
    
    