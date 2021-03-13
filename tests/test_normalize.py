from pathlib import Path

from boringmd import from_file

def test() -> None:
    for path in Path(__file__).parent.joinpath("documents").iterdir():
        if path.is_file() and path.name.endswith(".md"):
            with open(path.with_suffix(".txt"), "r") as expect_stream:
                assert from_file(path) == expect_stream.read()
