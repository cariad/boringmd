
from boringmd import text_from_string

# Regression test for https://github.com/cariad/boringmd/issues/5.
def test_5() -> None:
    result = text_from_string("**foo** [bar](http://test.com)")
    assert result == "foo bar"
