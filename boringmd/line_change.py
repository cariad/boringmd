from typing import Optional

from lstr import lstr


class LineChange:
    """
    Describes a change determined to be made for a line.

    Arguments:
        line: The transformed line. `None` to delete the line.
        stop: The line should not be transformed any further.
    """

    def __init__(self, line: Optional[lstr], stop: bool = False) -> None:
        self.stop = stop
        self.line = line
