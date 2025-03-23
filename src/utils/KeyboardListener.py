from models import Direction
from enum import Enum, auto
import keyboard


class Event(Enum):
    QUIT = auto()
    NONE = auto()


class KeyboardListener:

    DEFAULT_CONFIG: dict[int, Direction | Event] = {
        72: Direction.TOP,
        80: Direction.DOWN,
        75: Direction.LEFT,
        77: Direction.RIGHT,
        1: Event.QUIT,
    }

    @staticmethod
    def listen(config: dict[int, Direction | Event]) -> Direction | Event:
        key_event: keyboard.KeyboardEvent = keyboard.read_event(suppress=True)
        if key_event.event_type == keyboard.KEY_DOWN:
            scan_code: int = key_event.scan_code
            return config.get(scan_code, Event.NONE)
        return Event.NONE
    
    @staticmethod
    def listen_default() -> Direction | Event:
        return KeyboardListener.listen(KeyboardListener.DEFAULT_CONFIG)

