#!/usr/bin/env python3

import os
import sys


def count_lines(path):
    """

    Takes a file as an argument. Opens the file and extracts the lines
    into a list. In the for loop, it strips all lines of whitespace then
    ignores all blank lines. Then, it checks if it is inbetween the start
    and end of a multiline comment. If it is, it continues, ignoring the
    lines within the comment, as well as the beginning and ending of the
    comment itself (such as /* and */). If the line starts with a single
    line comment type, it is ignored as well. It then iterates the count
    for every line that does not meet any of those criteria (aka a line
    of code).

    """

    single_line = ("#", "--", "//")
    multiline_start = ("\"\"\"", "'''", "/*", "%{", ":'", "=begin")
    multiline_end = ("\"\"\"", "'''", "*/", "%}", "'", "=end")

    try:
        with open(path, "r") as f:
            lines = f.readlines()
            count = 0
            inside_multiline = False

            for line in lines:
                line = line.strip()

                if not line:
                    continue

                if inside_multiline:
                    if line.endswith(multiline_end):
                        inside_multiline = False
                    continue

                if any(line.startswith(comment) for comment in single_line):
                    continue

                if line.startswith(multiline_start):
                    inside_multiline = True
                    continue

                count += 1

        return count
    except FileNotFoundError as e:
        print(f"Error Type: {e}")
        print(f"Error: File '{path}' not found!")
        return sys.exit(1)


# Runs count_lines on every file and sums the total
def count_multiple_files(paths):
    try:
        total = 0
        for path in paths:
            total += count_lines(path)
        return total
    except Exception as e:
        print(f"Error Type: {e}")
        print(f"Error: File(s) '{', '.join(paths)}' not found!")
        return sys.exit(1)


# Super long, so I made a function for it
def print_usage():
    print("Usage:")
    print(f"    Single File: {sys.argv[0]} <file_path>")
    print(f"    Multiple Files: {sys.argv[0]} <file_path1> <file_path2>")
    print("NOTE:")
    print("     Currently, inputting multiple files will sum the total")
    print("     of all of the files. Separate counts will be implemented")
    print("     at a later date.")


# Used multiple times, so I made a function for it
def print_count(names, count):
    if len(names) > 1:
        print(f"Lines of code in {', '.join(names)}: {count}")
    else:
        print(f"Lines of code in {''.join(names)}: {count}")


# Do you even __main__ bro?
if __name__ == "__main__":
    paths = sys.argv[1:]
    basenames = [os.path.basename(path) for path in paths]

    if len(sys.argv) < 2:
        print_usage()
        sys.exit(0)
    elif len(sys.argv) == 2:
        count = count_lines(paths[0])
        print_count(basenames, count)
    else:
        count = count_multiple_files(paths)
        print_count(basenames, count)

