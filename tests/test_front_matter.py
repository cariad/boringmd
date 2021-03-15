from pathlib import Path
from typing import Optional

from pytest import mark

from boringmd.front_matter import (
    front_matter_from_file,
    front_matter_from_string,
    line_delimiter,
)


def test_front_matter_from_file() -> None:
    for path in Path(__file__).parent.joinpath("documents").iterdir():
        if path.is_file() and path.name.endswith(".md"):
            try:
                with open(path.with_suffix(".yml"), "r") as expect_stream:
                    assert front_matter_from_file(path) == expect_stream.read().rstrip()
            except FileNotFoundError:
                assert front_matter_from_file(path) is None


@mark.parametrize(
    "md, expect",
    [
        ("", None),
        (" ", None),
        ("foo", None),
        ("---\nfoo: bar\n---", "foo: bar"),
        ("+++\nfoo: bar\n+++", "foo: bar"),
        ("---\nfoo: bar\n", None),
    ],
)
def test_front_matter_from_string(md: str, expect: Optional[str]) -> None:
    assert front_matter_from_string(md) == expect


@mark.parametrize(
    "line, plain, pattern",
    [
        ("---", "---", "---"),
        ("+++", "+++", r"\+\+\+"),
    ],
)
def test_line_delimiter__true(line: str, plain: str, pattern: str) -> None:
    delimiter = line_delimiter(line)
    assert delimiter
    assert delimiter.plain == plain
    assert delimiter.pattern == pattern


@mark.parametrize(
    "line",
    [
        (""),
        (" ---"),
        ("--- "),
        ("foo"),
    ],
)
def test_line_delimiter__false(line: str) -> None:
    assert not line_delimiter(line)
