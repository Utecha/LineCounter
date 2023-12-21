#!/usr/bin/env python3

import os
import sys

from count_single import count_single_file
from count_multiple import count_multiple_files


def usage(argv):
    print(f"Usage: {argv[0]} <file_path1> <file_path2>")
    print("NOTES:")
    print("\tYou can enter any number of filepaths to count.")
    print("\tBy default, if you enter more than one filepath as")
    print("\tan argument, it will sum up the total of all files.\n")
    print("\tYou can also submit a folder as an argument. The script")
    print("\twill check through the folder, and treat every file it")
    print("\tfinds of the specified file type as the arguments passed")
    print("\tin as file paths.")


def print_count(basenames, count):
    if len(basenames) > 1:
        print(f"Lines of code in '{', '.join(basenames)}': {count}")
    else:
        print(f"Lines of code in '{''.join(basenames)}': {count}")


if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    file_paths = argv[1:]
    basenames = [os.path.basename(file) for file in file_paths]

    if argc < 2:
        usage(argv)
        sys.exit(1)
    elif argc == 2:
        count = count_single_file(file_paths[0])
        print_count(basenames, count)
    else:
        count = count_multiple_files(file_paths)
        print_count(basenames, count)
