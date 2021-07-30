from pathlib import Path

import rpipes
from rpipes.border import draw_boundary
from rpipes.utils import play_sound


def print_authors(authors: dict[str, str]) -> None:
    """Prints a list of authors with links from a dictionary of authors and links."""
    print(rpipes.terminal.move_y(rpipes.terminal.height // 2 - len(authors) // 2), end="")

    for author in authors:
        print(rpipes.terminal.move_right(2), end="")
        print(
            rpipes.terminal.link(
                authors[author],
                rpipes.terminal.white_bold
                + author
                + rpipes.terminal.normal
                + " - "
                + authors[author],
            )
        )  # Not all terminals support links so it also prints the url next to the author

    print(
        rpipes.terminal.move(rpipes.terminal.height - 3, rpipes.terminal.width - 20)
        + f"Press {rpipes.terminal.white_bold}B{rpipes.terminal.normal} to go back"
    )
    draw_boundary()


def show_credits(authors: dict[str, str]) -> None:
    """
    Displays a list of authors who contributed to this project.

    Args:
        authors (dict): A dictionary containing the author and their github page url
    """
    with rpipes.terminal.fullscreen() and rpipes.terminal.hidden_cursor():
        print(rpipes.terminal.clear)
        print_authors(authors)

        terminal_size = rpipes.terminal.width, rpipes.terminal.height

        while True:
            with rpipes.terminal.cbreak():
                key = rpipes.terminal.inkey(timeout=0.1)

                # Resize border if the terminal size gets changed
                if (rpipes.terminal.width, rpipes.terminal.height) != terminal_size:
                    print(rpipes.terminal.clear)
                    print_authors(authors)
                    draw_boundary()
                    terminal_size = rpipes.terminal.width, rpipes.terminal.height

                if key == "b":
                    play_sound(Path("music/up-down.wav"))
                    break


def load_screen(authors: dict[str, str]) -> None:
    """Callback for loading a screen."""
    show_credits(authors)
