

from models import Maze, Position2D, Tile, Direction
import random



class MazeCreator:

    @staticmethod
    def Maze(start_position: Position2D, width: int, height: int) -> Maze:
        maze: Maze = Maze(width, height, Position2D.random_position(width - 1, height - 1, {start_position}))
        MazeCreator._enclose_maze(maze)
        MazeCreator._maze_DFS(maze, maze.get_tile(start_position), None)
        return maze

    @staticmethod
    def _enclose_maze(maze: Maze) -> None:

        for tile in maze.all_tiles_from_row(0):
            tile.set_wall(Direction.TOP, True)

        for tile in maze.all_tiles_from_row(maze.height - 1):
            tile.set_wall(Direction.DOWN, True)

        for tile in maze.all_tiles_from_column(0):
            tile.set_wall(Direction.LEFT, True)

        for tile in maze.all_tiles_from_column(maze.width - 1):
            tile.set_wall(Direction.RIGHT, True)

    @staticmethod
    def _maze_DFS(maze: Maze, current_tile: Tile, visited: set | None = None) -> None:

        # we explore recursively and add walls around tiles (except the ones we are going to)
        # recursively, so that it creates a maze

        if visited is None: visited = set()

        visited.add(current_tile)
        accessible_neighbors: list[Tile] = MazeCreator._get_accessible_neighbors(maze, current_tile)
        random.shuffle(accessible_neighbors)

        for neighbor in accessible_neighbors:
            maze.add_walls(current_tile, neighbor)
            if neighbor not in visited:
                MazeCreator._maze_DFS(maze, neighbor, visited)
                maze.remove_walls(current_tile, neighbor)

    @staticmethod
    def _get_accessible_neighbors(maze: Maze, tile: Tile) -> list[Tile]:

        neighbors: list[Tile] = []

        # for each direction, we get the neighbor position

        for direction in Direction.Directions():

            nb_pos: Position2D = tile.get_neighbor_pos(direction)

            # if the position is valid, we check if the tile is accessible
            if maze.is_position_valid(nb_pos):
                neighbor: Tile = maze.get_tile(nb_pos)
                if tile.is_accessible(neighbor):
                    neighbors.append(neighbor)

        return neighbors





class MazeRoomPlacer:

    # this will try to place a number of rooms in the maze
    # we will use backtracking to try to place the rooms randomly
    # we want to open n walls in rooms when they are placed, to create a door
    # we will also try to place the rooms in a way that they don't overlap

    ...