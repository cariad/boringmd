from lstr import lstr

from boringmd.line_change import LineChange


def test__line() -> None:
    assert LineChange(line=None).line is None
    assert LineChange(line=lstr("foo")).line == lstr("foo")


def test__stop() -> None:
    assert LineChange(line=None).stop is False
    assert LineChange(line=None, stop=True).stop is True
