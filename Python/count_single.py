def count_single_file(file):
    single = ("#", "--", "//")
    multiStart = ("'''", '"""', "/*", "%{", ":'", "=begin")
    multiEnd = ("'''", '"""', "*/", "%}", "'", "=end")

    try:
        with open(file, "r") as file:
            lines = file.readlines()
            count = 0
            insideMulti = False

            for line in lines:
                line = line.strip()

                if not line:
                    continue

                if insideMulti:
                    if line.endswith(multiEnd):
                        insideMulti = False
                    continue

                if any(line.startswith(comment) for comment in single):
                    continue

                if line.startswith(multiStart):
                    insideMulti = True
                    continue

                count += 1

        return count
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"ERROR: File '{file}' not found.")

        return exit(1)
