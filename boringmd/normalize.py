from logging import getLogger
from pathlib import Path
from typing import List

from lstr import lstr

from boringmd.transformers import chain


def from_file(path: Path) -> str:
    """
    Converts a Markdown file to plain text.

    Arguments:
        Path: Path to Markdown file.

    Returns:
        Conversion to plain text.
    """
    with open(path, "r") as stream:
        return from_string(stream.read())


def from_string(document: str) -> str:
    """
    Converts a Markdown document to plain text.

    Arguments:
        document: Markdown document.

    Returns:
        Conversion to plain text.
    """

    transformers = chain()
    delete: List[int] = []
    lines = [lstr(line) for line in document.splitlines()]
    logger = getLogger()

    for index in range(len(lines)):
        index_str = "#" + str(index).rjust(len(str(len(lines))), "0")
        logger.debug("Starting chain for %s: %s", index_str, lines[index])

        for transformer in transformers:
            logger.debug("Transforming %s with %s.", index_str, transformer.name)
            line_change = transformer.transform(index, lines[index])

            if line_change.line is None:
                logger.debug("Deleting %s.", index_str)
                delete.append(index)
            else:
                lines[index] = line_change.line

            if line_change.stop:
                break

    for index in reversed(delete):
        del lines[index]

    return "\n".join([str(line) for line in lines]) + "\n"