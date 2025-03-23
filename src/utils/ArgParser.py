
from models import Position2D
from enum import Enum, auto
import argparse


class ArgParserArguments(Enum):

    WIDTH = auto()
    HEIGHT = auto()
    PLAYER_POS = auto()
    PLAYER_VISION = auto()
    NONE = auto()


class ArgParser:

    @staticmethod
    def parse_args() -> dict[ArgParserArguments, any]:

        parser: argparse.ArgumentParser = argparse.ArgumentParser(description="DungeonCrawler")
        parser.add_argument("--width", type=int, default=20, help="Width of the maze")
        parser.add_argument("--height", type=int, default=10, help="Height of the maze")
        parser.add_argument("--player_pos", type=Position2D.from_str, default=Position2D(0, 0), help="Player's starting position")
        parser.add_argument("--player_vision", type=int, default=5, help="Player's vision")
        args: argparse.Namespace = parser.parse_args()

        return {
            ArgParserArguments.WIDTH: args.width,
            ArgParserArguments.HEIGHT: args.height,
            ArgParserArguments.PLAYER_POS: args.player_pos,
            ArgParserArguments.PLAYER_VISION: args.player_vision,
        }
    
