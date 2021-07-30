from pathlib import Path
from typing import List

import rpipes
from rpipes.border import draw_boundary
from rpipes.utils import play_sound


def display_tutorial(lines: List[str]) -> None:
    """Wraps and prints tutorial text"""
    print(rpipes.terminal.clear, end="")
    print(
        rpipes.terminal.move(rpipes.terminal.height - 3, rpipes.terminal.width - 20)
        + f"Press {rpipes.terminal.white_bold}B{rpipes.terminal.normal} to go back"
    )
    draw_boundary()
    print(rpipes.terminal.move_xy(2, 2), end="")

    lines = [
        line.format(
            title=rpipes.terminal.white_underline + rpipes.terminal.bold,
            bold=rpipes.terminal.bold,
            normal=rpipes.terminal.normal,
            breakline=rpipes.terminal.white_underline + rpipes.terminal.normal,
        )
        for line in lines
    ]

    for line in lines:
        if line.startswith(rpipes.terminal.white_underline):
            print(rpipes.terminal.move_down(1) + rpipes.terminal.move_x(2), end="")

        for wrapped_line in rpipes.terminal.wrap(line, width=rpipes.terminal.width - 4):
            print(wrapped_line, end="")
            print(rpipes.terminal.move_down(1) + rpipes.terminal.move_x(2), end="", flush=True)


def load_screen(file: Path) -> None:
    """Callback for loading screen"""
    tutorial_text = file.read_text(encoding="utf8").splitlines()
    terminal_size = 0, 0
    with rpipes.terminal.hidden_cursor():
        with rpipes.terminal.cbreak():
            while True:
                if terminal_size != (rpipes.terminal.width, rpipes.terminal.height):
                    display_tutorial(tutorial_text)
                    terminal_size = (rpipes.terminal.width, rpipes.terminal.height)

                if rpipes.terminal.inkey(timeout=0.1) == "b":
                    play_sound(Path("music/up-down.wav"))
                    return
