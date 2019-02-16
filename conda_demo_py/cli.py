"""Console scripts."""

from argparse import ArgumentParser, FileType
from pprint import pprint

from yaml import load

from .version import __version__


def cdemopy():
    """All CLI entry point functions must take no arguments and return either
    None or an exit code. This example takes any input YAML files and prints
    out Python equivalents."""
    parser = ArgumentParser(description=cdemopy.__doc__)
    parser.add_argument('--version', action='version',
                        version=f'%(prog)s {__version__}')
    parser.add_argument('input_files', nargs='*', type=FileType())
    args = parser.parse_args()
    return implement_cdemopy(args.input_files)
    # No return value -> None -> no error


def implement_cdemopy(input_files):
    print('hello from conda_demo_py')
    for input_file in input_files:
        print()
        print(input_file.name)
        data = load(input_file)
        pprint(data)
    # Every Python function has a default return value of None.
