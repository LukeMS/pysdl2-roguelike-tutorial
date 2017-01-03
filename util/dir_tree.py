"""tree.py.

Written by Doug Dahms

Original work available at:
    https://gist.github.com/BjornFJohansson/f49aacf7cdc43a75c8f7

With minor modifications by Lucas Siqueira.

Prints the tree structure for the path specified on the command line.
"""

import os
from os import listdir, sep
from os.path import abspath, basename, isdir

from sys import argv

WP = os.path.join(os.path.dirname(__file__), '..', 'first_rl_part_1')


def tree(dir, padding, print_files=False, ignore_paths=None):
    """..."""
    print(padding[:-1] + '+-' + basename(abspath(dir)) + '/')
    padding = padding + ' '
    files = []
    if print_files:
        files = [x for x in listdir(dir)
                 if x not in ignore_paths]
    else:
        files = [x for x in listdir(dir)
                 if isdir(dir + sep + x) and
                 x not in ignore_paths]
    count = 0
    for file in files:
        count += 1
        print(padding + '|')
        path = dir + sep + file
        if isdir(path):
            if count == len(files):
                tree(path, padding + ' ', print_files, ignore_paths)
            else:
                tree(path, padding + '|', print_files, ignore_paths)
        else:
            print(padding + '+-' + file)


def usage():
    """..."""
    return '''Usage: %s [-f] <PATH>
Print tree structure of path specified.
Options:
-f      Print files as well as directories
PATH    Path to process''' % basename(argv[0])


def main(arg_path=None, padding=None, arg_files=None, arg_ignore=None):
    """..."""
    padding = padding or ' '
    if len(argv) == 1 and arg_path is None:
        print(usage())
    elif len(argv) == 2 or (arg_path and arg_ignore is None and
                            arg_files is None):
        # print just directories
        path = argv[1]
        if isdir(path):
            tree(path, ' ')
        else:
            print('ERROR: \'' + path + '\' is not a directory')
    elif (len(argv) == 3 and arg_path) and (argv[1] == '-f' or arg_files):
        # print directories and files
        path = argv[2]
        if isdir(path):
            tree(path, ' ', True)
        else:
            print('ERROR: \'' + path + '\' is not a directory')
    elif arg_path:
        tree(arg_path, padding, arg_files, arg_ignore)
    else:
        print(usage())

if __name__ == '__main__':
    main(arg_path=WP, arg_files=True, arg_ignore=[".git", "__pycache__"])
