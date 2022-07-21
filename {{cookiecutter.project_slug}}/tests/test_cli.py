from {{ cookiecutter|modname }}.__main__ import main

from click.testing import CliRunner


def test_{{ cookiecutter|modname }}_cli():
    runner = CliRunner()
    result = runner.invoke(main, ())
    assert result.exit_code == 0
