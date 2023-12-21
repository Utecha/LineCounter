from count_single import count_single_file


# Runs the countSingleFile function on every file and sums the total.
def count_multiple_files(file_paths):
    try:
        total = 0

        for file in file_paths:
            total += count_single_file(file)

        return total
    except Exception as e:
        print(f"Error: {e}")
        print(f"ERROR: File(s) '{', '.join(file_paths)}' not found!")

        return exit(1)
