"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Practical Cli Game."""


if __name__ == "__main__":
    main(prog_name="practical-cli-game")  # pragma: no cover
