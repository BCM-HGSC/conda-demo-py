"""Console scripts."""

from argparse import ArgumentParser

from .version import __version__


def cdemopy():
    """All CLI entry point functions must take no arguments and return either
    None or an exit code."""
    parser = ArgumentParser(description=cdemopy.__doc__)
    parser.add_argument('--version', action='version',
                        version=f'%(prog)s {__version__}')
    args = parser.parse_args()
    print('hello from conda_demo_py')
    # No return value -> None -> no error
