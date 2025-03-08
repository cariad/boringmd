from lstr import lstr
from pytest import mark

from boringmd.transformers.hyperlink import HyperlinkTransformer


@mark.parametrize(
    "line, expect",
    [
        ("foo", "foo"),
        ("[foo](bar)", "foo"),
        ("woo [foo](bar)", "woo foo"),
        ("[woo] [foo](bar)", "[woo] foo"),
        ("[foo](bar) (woo)", "foo (woo)"),
    ],
)
def test(
    line: str,
    expect: str,
) -> None:
    line_str = lstr(line)

    HyperlinkTransformer().transform(
        0,
        line_str,
    )

    assert line_str == expect
