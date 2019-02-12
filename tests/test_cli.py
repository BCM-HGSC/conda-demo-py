from conda_demo import cli


def test_cli_template():
    assert cli.main() is None
