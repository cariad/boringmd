# boringmd

`boringmd` is a Python package and command line tool for extracting plain text and front matter from Markdown.

## Installation

`boringmd` requires Python 3.8 or later.

```bash
pip install boringmd
```

## Command line

Pass the filename of a Markdown document to extract its plain text content:

```bash
boringmd input.md
```

To extract the front matter only, include the `--front-matter` flag:

```bash
boringmd input.md --front-matter
```

`boringmd` prints to stdout. To write the extraction to a file, redirect it:

```bash
boringmd input.md > output.txt
```

## Package

```python
from boringmd import front_matter_from_string, text_from_string
markdown = "---\nfoo: bar\n---\n**foo** and _bar_"
print(text_from_string(markdown))
# foo and bar
print(front_matter_from_string(markdown))
# foo: bar

from pathlib import Path
from boringmd import front_matter_from_file, text_from_file
print(text_from_file(Path("input.md")))
print(front_matter_from_file(Path("input.md")))
```

## Related packages

`boringmd` uses [cariad/lstr](https://github.com/cariad/lstr) to manipulate strings.

## Thank you! 🎉

My name is **Cariad**, and I'm an [independent freelance DevOps engineer](https://cariad.io).

I'd love to spend more time working on projects like this, but--as a freelancer--my income is sporadic and I need to chase gigs that pay the rent.

If this project has value to you, please consider [☕️ sponsoring](https://github.com/sponsors/cariad) me. Sponsorships grant me time to work on _your_ wants rather than _someone else's_.

Thank you! ❤️
