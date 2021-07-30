from pathlib import Path

import rpipes
from rpipes.art import BANNER
from rpipes.border import draw_boundary
from rpipes.utils import play_sound


def print_options(selection: int, options: list) -> None:
    """
    Prints the options provided and highlights the active selection.

    Args:
        selection (int): A zero indexed integer representing the current selection
        options (list): The list of options to print
    """
    print(rpipes.terminal.clear, end="")
    draw_boundary()

    print(
        rpipes.terminal.move_y(
            (rpipes.terminal.height - len(BANNER.split("\n")) - len(options) - 1) // 2
        ),
        end="",
    )

    for line in BANNER.split("\n"):
        print(rpipes.terminal.move_right(2), end="")
        print(line)

    print()

    for idx, option in enumerate(options):
        print(rpipes.terminal.move_right(2), end="")  # Move 2 right to not interfere with border

        if option == "Quit" and idx != selection:
            print(rpipes.terminal.red + "Quit" + rpipes.terminal.normal)

        elif option == "Quit" and idx == selection:
            print(rpipes.terminal.black + rpipes.terminal.on_red + "Quit" + rpipes.terminal.normal)

        elif idx == selection:
            print(
                rpipes.terminal.black + rpipes.terminal.on_green + option + rpipes.terminal.normal
            )

        else:
            print(rpipes.terminal.green + option + rpipes.terminal.normal)

    print(
        rpipes.terminal.move(rpipes.terminal.height - 3, rpipes.terminal.width - 29)
        + f"Use {rpipes.terminal.white_bold}UP{rpipes.terminal.normal} and "
        f"{rpipes.terminal.white_bold}DOWN{rpipes.terminal.normal} to navigate"
    )

    print(
        rpipes.terminal.move(rpipes.terminal.height - 4, rpipes.terminal.width - 23)
        + f"Press {rpipes.terminal.white_bold}ENTER{rpipes.terminal.normal} to select"
    )


def get_selection(options: list) -> int:
    """
    An interactive prompt for the user to select an option from a list of options.

    Args:
        options (list): List of options for the user choose from

    Returns:
        int: A zero indexed integer representing the chosen selection
    """
    selection = 0

    with rpipes.terminal.fullscreen() and rpipes.terminal.hidden_cursor():
        terminal_size = rpipes.terminal.width, rpipes.terminal.height

        print(rpipes.terminal.clear)

        print_options(selection, options)
        while True:
            with rpipes.terminal.cbreak():  # Without rpipes.terminal.cbreak, the terminal cannot take in any input
                key = rpipes.terminal.inkey(timeout=0.1)

                # Resize border if the terminal size gets changed
                if (rpipes.terminal.width, rpipes.terminal.height) != terminal_size:
                    print(rpipes.terminal.clear)

                    # Draw the content first to avoid content overflow
                    print_options(selection, options)
                    draw_boundary()

                    terminal_size = rpipes.terminal.width, rpipes.terminal.height

                if key.name == "KEY_UP":
                    selection = (selection - 1) % len(options)
                    print_options(selection, options)
                    play_sound(Path("music/up-down.wav"))

                elif key.name == "KEY_DOWN":
                    selection = (selection + 1) % len(options)
                    print_options(selection, options)
                    play_sound(Path("music/up-down.wav"))

                elif key.name == "KEY_ENTER":
                    play_sound(Path("music/up-down.wav"))
                    return selection


def load_screen(options: list) -> int:
    """Callback for loading a screen."""
    return get_selection(options)
