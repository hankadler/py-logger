#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Built-in logger with added functions.

@author   Hank Adler
@version  0.1.0
@license  MIT
"""


import inspect
import getpass
import logging
import os
import platform
import sys

import header


def get(name, filename=None):
    """Returns logger object with specified name.

    If filename is specified a LOG file is created with an application
    information header.

    Parameters:
        name (str): Logger object name.
        filename (str): LOG pathname.

    Returns:
        logging.Logger object with custom configuration.
    """
    if filename is not None:
        _create(filename)

    logger = logging.getLogger(name)

    return logger


def _create(filename):
    """Creates a LOG file with basic application information header.

    Parameters:
        filename (str): LOG pathname.
    """
    filename = filename.rstrip('.py')
    if not filename.endswith('.log'):
        filename = filename + '.log'

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s  %(levelname)-8s  %(message)s',
        datefmt='%Y-%m-%d  %I:%M-%p',
        filename=filename,
        filemode='a',
    )

    if len(logging.getLogger('').handlers) == 1:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.INFO)
        logging.getLogger('').addHandler(stream_handler)

    app = os.path.realpath(inspect.stack()[-1].filename).replace('\\', '/')
    version = header.getVersion(app)
    system = platform.platform()
    user = getpass.getuser()
    dir = os.getcwd().replace('\\', '/')

    with open(filename, 'w') as fh:
        fh.write('APPLICATION:  %s\n' % app)
        fh.write('    VERSION:  %s\n' % version)
        fh.write('     SYSTEM:  %s\n' % system)
        fh.write('       USER:  %s\n' % user)
        fh.write('  DIRECTORY:  %s\n\n' % dir)


if __name__ == '__main__':
    pass
