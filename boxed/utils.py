import threading
from pathlib import Path

import playsound

import boxed
from boxed.border import draw_boundary


def get_int_input(prompt: str, x: int, y: int) -> int:
    """Ask for integer input with `prompt` positioned at `x`, `y`."""
    print(boxed.terminal.clear, end="")
    draw_boundary()
    previous_input = ""
    while True:
        print(boxed.terminal.move_xy(x, y) + " " * len(prompt + previous_input), end="")
        previous_input = input(boxed.terminal.move_xy(x, y) + prompt)
        try:
            return int(previous_input)

        except ValueError:
            print(boxed.terminal.move_xy(x, y + 1) + "Invalid input!")


def play_sound(file_path: Path) -> None:
    """Run sound file behind `file_path` asynchronously."""
    threading.Thread(target=playsound.playsound, args=(str(file_path),), daemon=True).start()
