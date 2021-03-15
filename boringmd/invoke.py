from argparse import ArgumentParser
from logging import basicConfig, getLogger, root
from typing import List, Optional

from boringmd.normalize import text_from_file
from boringmd.front_matter import front_matter_from_file

def invoke(args: Optional[List[str]] = None) -> int:
    """
    Entrypoint for `boringmd` via a command line interface.

    Arguments:
        arg: Optional arguments. Will read from the command line if omitted.

    Returns:
        Shell exit code.
    """

    basicConfig(format="%(message)s")
    logger = getLogger("boringmd")

    arg_parser = ArgumentParser(
        "boringmd",
        usage="boringmd exciting.md > boring.txt",
        description="Converts Markdown to boring plain text.",
        epilog="Made with ❤️ by Cariad Eccleston: https://cariad.io",
    )

    arg_parser.add_argument(
        "markdown",
        help="Path to Markdown file",
        metavar="PATH",
    )

    arg_parser.add_argument(
        "--front-matter",
        action="store_true",
        help="print front matter only",
    )

    arg_parser.add_argument(
        "--log-level",
        default="INFO",
        help="log level",
        metavar="LEVEL",
    )

    parsed_args = arg_parser.parse_args(args)
    root.setLevel(parsed_args.log_level.upper())

    try:
        if parsed_args.front_matter:
            print(front_matter_from_file(parsed_args.markdown))
        else:
            print(text_from_file(parsed_args.markdown))
        return 0
    except FileNotFoundError as ex:
        logger.error('"%s" not found.', ex.filename)
        return 2
    except Exception as ex:
        logger.exception(ex)
        return 1
