from boringmd.line_guidance import LineGuidance


def test_delete() -> None:
    assert LineGuidance().delete is False
    assert LineGuidance(delete=True).delete is True


def test_stop() -> None:
    assert LineGuidance().stop is False
    assert LineGuidance(stop=True).stop is True
