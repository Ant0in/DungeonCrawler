

from models import Maze, Player, Position2D, Tile



class MazeRenderer:

    @staticmethod
    def render_maze(maze: Maze, player: Player) -> None:
        
        width: int = maze.width
        height: int = maze.height
        output: str = ""
        
        for y in range(height):

            top_line: str = "+"
            mid_line: str = ""
            
            for x in range(width):

                tile: Tile = maze.get_tile(Position2D(x, y))
                visible: bool = player.is_visible(tile.pos)
                
                if visible:
                    # walls
                    top_wall = "---+" if tile.wall_top else "   +"
                    left_wall = "|" if tile.wall_left else " "
                    
                    match tile.pos.coords:
                        case player.pos.coords: char = "P"
                        case maze.exit_pos.coords: char = "E"
                        case _: char = " "
                    
                    top_line += top_wall
                    mid_line += f"{left_wall} {char} "

                else:
                    # not visible
                    top_line += "    "
                    mid_line += "    "
            
            # we need to check if the last tile of each row is visible
            last_tile: Tile = maze.get_tile(Position2D(width - 1, y))
            if player.is_visible(last_tile.pos): mid_line += "|"
            else: mid_line += " "
            output += top_line + "\n" + mid_line + "\n"
        
        # we need to add the bottom line of the maze
        # we need to check which tiles are visible

        for x in range(width):
            tile = maze.get_tile(Position2D(x, height - 1))
            visible = player.is_visible(tile.pos)
            bottom_line = "+---" if tile.wall_down else "+   "
            if visible:
                output += bottom_line
            else:
                output += "    "
        
        return output
    

