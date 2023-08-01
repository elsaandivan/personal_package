"""Console script for elsa."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("elsa")
    click.echo("=" * len("elsa"))
    click.echo("Skeleton project created by Cookiecutter PyPackage")


if __name__ == "__main__":
    main()  # pragma: no cover
