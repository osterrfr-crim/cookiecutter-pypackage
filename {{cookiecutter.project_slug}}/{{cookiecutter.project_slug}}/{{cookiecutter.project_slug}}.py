#!/usr/bin/env python
# coding: utf-8

"""
{{ cookiecutter.project_short_description}}
"""

# -- Standard library --------------------------------------------------------
import logging.config
import argparse
import os

# -- Project specific --------------------------------------------------------
from .__meta__ import __version__ as __ver__

THIS_DIR = os.path.dirname(__file__)


def main():
    """
    Command line entry point.
    """
    log_conf_fn = os.path.join(THIS_DIR, 'logging.ini')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", "-v", action="version", version=__ver__)
    parser.add_argument("-l",
                        action='store',
                        default=log_conf_fn,
                        dest='logging_conf_fn',
                        help='Set logging configuration filename')
    args = parser.parse_args()
    logging.config.fileConfig(args.logging_conf_fn)


if __name__ == '__main__':
    main()
