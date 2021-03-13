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
    c = chain()
    delete: List[int] = []
    lines = [lstr(line) for line in document.splitlines()]
    logger = getLogger()
    for index in range(len(lines)):
        for transformer in c:
            logger.debug("Normalising: %s", lines[index])
            if result := transformer.transform(index, lines[index]):
                if result.stop:
                    break
                elif result.delete:
                    delete.append(index)
                elif result.line:
                    lines[index] = result.line

    for index in reversed(delete):
        del lines[index]

    return "\n".join([str(line) for line in lines]) + "\n"
