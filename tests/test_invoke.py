from mock import Mock, patch

from boringmd.invoke import invoke


def test() -> None:
    assert invoke(["./tests/documents/smoke.md"]) == 0


@patch("boringmd.invoke.text_from_file", side_effect=Exception())
def test__exception(text_from_file: Mock) -> None:
    assert invoke(["foo"]) == 1


def test__file_not_found() -> None:
    assert invoke(["foo"]) == 2
