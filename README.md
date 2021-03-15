# boringmd

`boringmd` is a Python package and command line tool for converting Markdown documents to plain text.

`boringmd` does _not_ render Markdown in any particularly beautiful way. It's a lightweight package for simply extracting plain text content.

## Examples

Each example below shows a snippet of Markdown and how it will be transformed to plain text.

### Emphasis

```markdown
This is *emphasis*, and so is _this_.
```

```text
This is emphasis, and so is this.
```

### Fenced code

````markdown
Code sample:

```markdown
# Shopping list

1. Ducks
2. Grapes
3. Basketballs
```
````

```text
Code sample:

# Shopping list

1. Ducks
2. Grapes
3. Basketballs
```

### Front matter

```markdown
---
foo: bar
---
I love gummy cakes.
```

```text
I love gummy cakes.
```

### Headings

```markdown
# Abraham Lincoln

## Life

### Favourite cakes

Abraham Lincoln might have enjoyed gummy cakes.

```

```text
Abraham Lincoln

Life

Favourite cakes

Abraham Lincoln might have enjoyed gummy cakes.
```

### HTML

```markdown
I want a line break<br />here.
```

```text
I want a line break here.
```

### Indented code

```markdown
Code sample:

    # Shopping list

    1. Ducks
    2. Grapes
    3. Basketballs
```

```text
Code sample:

    # Shopping list

    1. Ducks
    2. Grapes
    3. Basketballs
```

### Inline code

```markdown
Use `git` to clone and `pytest` to test.
```

```text
Use git to clone and pytest to test.
```

### Line

```markdown
This paragraph is separated from the next.

---

This paragraph is separated from the previous.
```

```text
This paragraph is separated from the next.

This paragraph is separated from the previous.
```

### Strength

```markdown
This is **strong**.
```

```text
This is strong.
```

## Usage

### Installation

`boringmd` requires Python 3.8 or later.

```bash
pip install boringmd
```

### Command line

On the command line, `boringmd` prints the conversion to stdout:

```bash
boringmd input.md
```

To write the conversion to a file, redirect it:

```bash
boringmd input.md > output.txt
```

### Package

```python
from boringmd import from_string
print(from_string("**foo** and _bar_"))

from pathlib import Path
from boringmd import from_file
print(from_file(Path("input.md")))
```

## Related packages

`boringmd` uses [cariad/lstr](https://github.com/cariad/lstr) to manipulate strings.

## Thank you! 🎉

My name is **Cariad**, and I'm an [independent freelance DevOps engineer](https://cariad.io).

I'd love to spend more time working on projects like this, but--as a freelancer--my income is sporadic and I need to chase gigs that pay the rent.

If this project has value to you, please consider [☕️ sponsoring](https://github.com/sponsors/cariad) me. Sponsorships grant me time to work on _your_ wants rather than _someone else's_.

Thank you! ❤️
