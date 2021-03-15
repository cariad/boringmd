from typing import Optional

from pytest import mark

from boringmd.front_matter import front_matter, line_delimiter


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
def test_front_matter(md: str, expect: Optional[str]) -> None:
    assert front_matter(md) == expect


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
