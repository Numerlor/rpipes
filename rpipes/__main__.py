import time
from pathlib import Path

import blessed

import rpipes
from rpipes.screens import credits, game, main_menu, tutorial, victory
from rpipes.utils import get_int_input

rpipes.terminal = blessed.Terminal()
try:
    import msvcrt

    # Add a small sleep to blessed's windows terminal kbhit to prevent high CPU usage from the tight loop
    def _kbhit_patch(self, timeout=None):  # noqa: ANN
        end = time.time() + (timeout or 0)
        while True:
            if msvcrt.kbhit():
                return True

            if timeout is not None and end < time.time():
                break
            time.sleep(0.01)

        return False

    blessed.win_terminal.Terminal.kbhit = _kbhit_patch

except ModuleNotFoundError:
    pass


menu_options = ["Play", "How to play", "Credits", "Quit"]

authors = {
    "Aaris-Kazi": "https://github.com/Aaris-Kazi",
    "Abhishek10351": "https://github.com/Abhishek10351",
    "DrokoDomi": "https://github.com/DrokoDomi",
    "Numerlor": "https://github.com/Numerlor",
    "ShanTen": "https://github.com/ShanTen",
    "SystematicError": "https://github.com/SystematicError",
}

try:
    while True:
        action = main_menu.load_screen(menu_options)

        if action == 0:  # Level selector
            cell_size = 0
            while cell_size <= 0:
                cell_size = get_int_input(
                    "Enter cell size (min 1): ", 10, rpipes.terminal.height // 2
                )
            width = 0
            while width < 3:
                width = get_int_input("Enter grid width (min 3): ", 10, rpipes.terminal.height // 2)
            height = 0
            while height < 3:
                height = get_int_input(
                    "Enter grid height (min 3): ", 10, rpipes.terminal.height // 2
                )
            recursive_elements = float("inf")
            while recursive_elements > width * height // 2:
                recursive_elements = max(
                    get_int_input(
                        f"Enter difficulty (number of recursive cells on main puzzle (max {width * height // 2})): ",
                        10,
                        rpipes.terminal.height // 2,
                    ),
                    0,
                )

            if game.load_screen(
                cell_size, width, height, recursive_elements
            ):  # Returns true when game is won
                victory.load_screen()

        elif action == 1:  # Tutorial
            tutorial.load_screen(Path("tutorial.txt"))

        elif action == 2:  # Credits
            credits.load_screen(authors)

        elif action == 3:  # Quit Menu
            raise KeyboardInterrupt()


except KeyboardInterrupt:
    print(rpipes.terminal.clear)
