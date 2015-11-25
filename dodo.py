"""
Automation tools for this project."
"""
import os
import glob

from pyflakes.scripts.pyflakes import checkPath


DOIT_CONFIG = {
    # output from actions should be sent to the terminal/console
    'verbosity': 2,
    # does not stop execution on first task failure
    'continue': True,
    # doit itself should not produce any output (use only actions output)
    'reporter': 'zero',
    # use multi-processing / parallel execution
    'num_process': 2,
    }


def check_path(filename):
    """execute pyflakes checker"""
    return not bool(checkPath(filename))


def task_pyflakes():
    """generate task for each file to be checked"""
    for filename in glob.glob('*.py'):
        path = os.path.abspath(filename)
        yield {
            'name': path,  # name required to identify tasks
            'file_dep': [path],  # file dependency
            'actions': [(check_path, (filename,))],
            }
