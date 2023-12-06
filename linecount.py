import sys
import os


def count_lines(path):
    prefixes = ("#", "--", "//", "/*", "'''", "\"\"\"")

    try:
        with open(path, "r") as f:
            lines = f.readlines()
            # Exclude blank lines, comments, and docstrings
            count = [line for line in lines if line.strip() and not line.lstrip().startswith(prefixes)]
            return len(count)
    except FileNotFoundError:
        print(f"Error: File {path} not found!")
        return sys.exit(0)


def count_multiple(paths):
    try:
        total = 0
        for path in paths:
            total += count_lines(path)
        return total
    except Exception as e:
        print(f"Error Type: {e}")
        print(f"Error: File(s) {', '.join(paths)} not found!")
        return sys.exit(0)


if __name__ == "__main__":

    file_paths = sys.argv[1:]
    file_names = [os.path.basename(path) for path in file_paths]

    # Check if an argument is provided
    if len(sys.argv) < 2:
        print("Usage: python linecount.py <file_path1> <file_path2>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        count = count_lines(file_paths[0])
        print(f"Lines of Code in {''.join(file_names)}: {count}")
    else:
        count = count_multiple(file_paths)
        print(f"Lines of Code in {', '.join(file_names)}: {count}")

