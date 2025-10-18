"""
Unit tests for CLI module.
"""

import pytest
from click.testing import CliRunner
from gaia_framework.cli import main


def test_cli_help():
    """Test that CLI help command works."""
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert 'GAIA Framework' in result.output


def test_cli_version():
    """Test that CLI version command works."""
    runner = CliRunner()
    result = runner.invoke(main, ['--version'])
    assert result.exit_code == 0
