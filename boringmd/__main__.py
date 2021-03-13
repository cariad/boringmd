from boringmd.cli import Cli


def cli_entry() -> None:
    exit(Cli().invoke())


if __name__ == "__main__":
    cli_entry()
