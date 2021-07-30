import rpipes
from rpipes.border import draw_boundary
from rpipes.constants import TROPHY


def display_game_over() -> None:
    """Displayed when game successfully finished"""
    print(rpipes.terminal.clear, end="")
    print(
        rpipes.terminal.move(rpipes.terminal.height - 3, rpipes.terminal.width - 20)
        + f"Press {rpipes.terminal.white_bold}B{rpipes.terminal.normal} to go back"
    )
    print(rpipes.terminal.yellow, end="")
    print(
        rpipes.terminal.move_xy(rpipes.terminal.width // 2 - 8, rpipes.terminal.height // 2 - 8),
        end="",
    )

    trophy_lines = TROPHY.splitlines()
    for row, line in enumerate(trophy_lines):
        print(
            rpipes.terminal.move_xy(
                rpipes.terminal.width // 2 - len(trophy_lines[0]) // 2,
                row + rpipes.terminal.height // 2 - len(trophy_lines) // 2,
            )
            + line,
            end="",
        )
    print(rpipes.terminal.normal, end="")

    draw_boundary()


def load_screen() -> None:
    """Callback for loading screen"""
    with rpipes.terminal.hidden_cursor():
        with rpipes.terminal.cbreak():
            while rpipes.terminal.inkey() != "b":
                display_game_over()
