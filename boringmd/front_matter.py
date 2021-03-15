from dataclasses import dataclass
from re import RegexFlag, match
from typing import Optional


@dataclass
class Delimiter:
    plain: str
    pattern: str


FRONT_MATTER_DELIMITERS = [
    Delimiter(plain="---", pattern=r"---"),
    Delimiter(plain="+++", pattern=r"\+\+\+"),
]


def document_delimiter(md: str) -> Optional[Delimiter]:
    """
    Gets the Markdown document's front matter delimiter.

    Arguments:
        md: Markdown document.

    Returns:
        Delimiter, if any.
    """
    return line_delimiter(md.splitlines()[0]) if md else None


def front_matter(md: str) -> Optional[str]:
    """
    Extracts the Markdown document front matter as a string.

    Arguments:
        md: Markdown document.

    Returns:
        Front matter, if any.
    """
    delimiter = document_delimiter(md)
    if not delimiter:
        return None

    found = match(
        fr"{delimiter.pattern}\s(.+)\s{delimiter.pattern}",
        md,
        RegexFlag.DOTALL + RegexFlag.MULTILINE,
    )

    return found.group(1) if found else None


def line_delimiter(line: str) -> Optional[Delimiter]:
    """
    Returns the front matter delimiter if this line is one.

    Arguments:
        line: Line to check.

    Returns:
        Delimiter.
    """
    if not line:
        return None
    for delimiter in FRONT_MATTER_DELIMITERS:
        if line == delimiter.plain:
            return delimiter
    return None
