import rpipes
from rpipes.constants import WBorder


def draw_boundary() -> None:
    """Prints a border around the app."""
    # Upper edge
    print(rpipes.terminal.move_xy(0, 0), WBorder.HORIZONTAL * (rpipes.terminal.width - 1))

    # Left and Right edges
    for row in range(rpipes.terminal.height - 2):
        print(
            WBorder.VERTICAL,
            rpipes.terminal.move_right(rpipes.terminal.width - 4),
            WBorder.VERTICAL,
        )

    # Bottom edge
    print(
        rpipes.terminal.move_xy(0, rpipes.terminal.height - 2),
        WBorder.HORIZONTAL * (rpipes.terminal.width - 1),
    )

    # Top left corner
    print(rpipes.terminal.move_xy(0, 0) + WBorder.DOWN_AND_RIGHT)

    # Top right corner
    print(rpipes.terminal.move_xy(rpipes.terminal.width - 1, 0) + WBorder.DOWN_AND_LEFT)

    # Bottom left corner
    print(rpipes.terminal.move_xy(0, rpipes.terminal.height - 2) + WBorder.UP_AND_RIGHT)

    # Bottom right corner
    print(
        rpipes.terminal.move_xy(rpipes.terminal.width - 1, rpipes.terminal.height - 2)
        + WBorder.UP_AND_LEFT
    )
