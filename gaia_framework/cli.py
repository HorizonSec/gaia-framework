"""
CLI entry point for GAIA Framework.
"""

import click
from gaia_framework import __version__


@click.group()
@click.version_option(version=__version__)
def main():
    """GAIA Framework - Security module orchestration."""
    pass


if __name__ == "__main__":
    main()
