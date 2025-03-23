

from models import Maze, Position2D, Player, Direction
from controllers import MazeCreator
from views import MazeRenderer
from utils import KeyboardListener, Event, ArgParser



WIDTH: int = 20
HEIGHT: int = 10
PLAYER_POS: Position2D = Position2D(0, 0)
PLAYER_VISION: int = 5



def handle_events(event: Event, player: Player, maze: Maze) -> bool:
    if event == Event.QUIT: return False
    elif event == Event.NONE: return True
    elif event in Direction.Directions(): player.move(maze, event); return True
    else: raise ValueError(f"Invalid event: {event}")

def handle_state(player: Player, maze: Maze) -> bool:
    
    if player.has_exited(maze):
        print("You have exited the maze!")
        return False
    
    return True

def main(player: Player, maze: Maze) -> None:

    running: bool = True
    event: Event = Event.NONE

    while running:

        print(MazeRenderer.render_maze(maze, player))
        event: Event = KeyboardListener.listen_default()
        running = handle_events(event, player, maze) and handle_state(player, maze)
        print("\033c", end="")  # flush the console

    # weird way to do it, but whatever
    handle_state(player, maze)



if __name__ == '__main__':
    
    player: Player = Player(PLAYER_POS, PLAYER_VISION)
    maze: Maze = MazeCreator.Maze(player.pos, WIDTH, HEIGHT)
    main(player, maze)

