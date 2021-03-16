from mock import Mock, patch

from boringmd.invoke import invoke


def test() -> None:
    assert invoke(["./tests/documents/smoke.md"]) == 0


@patch("boringmd.invoke.text_from_file", side_effect=Exception())
def test__exception(text_from_file: Mock) -> None:
    assert invoke(["foo"]) == 1


def test__file_not_found() -> None:
    assert invoke(["foo"]) == 2


def test__front_matter() -> None:
    assert invoke(["--front-matter", "./tests/documents/smoke.md"]) == 0


def test__no_path() -> None:
    assert invoke([]) == 3


def test__version() -> None:
    assert invoke(["--version"]) == 0
