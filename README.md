# LineCounter - Python Edition

#### NOTE: This is the main branch of this repo. Other branches include Lua and Rust variants of this program. I may add others later.

This was just a fun little project I decided to work on as an exercise to both learn more about programming in various languages, but also to have a fun little way of tracking how many lines of code I am ultimately writing for various projects. It works to track how efficient you are becoming as a programmer. Meaning, you are able to accomplish the same tasks in less lines of code, though hopefully while maintaining readability, of course!

- [License](#license)
- [Supported Languages](#supported-languages)
- [Install](#install)
- [Usage](#usage)

## License
LineCounter is released under the [MIT License](https://github.com/Utecha/LineCounter/blob/python/LICENSE)

## Supported Languages

- Python (a given, considering this was the first language I wrote the program in)
- Lua (also a given, if you check the branches)
- Rust (same as lua)
- C 
- C++
- C#
- Objective-C
- Java
- JavaScript/Typescript
- Shell (Bash/Zsh/Fish)
- MATLAB
- PHP
- Ruby
- Swift
- Kotlin
- Go
- SQL
- Dart
- R
- Zig
- Probably a bunch of others I can't think of off the top of my head

If your language does not appear on that list, it still may be supported. Any language with these single/multi-line comment types are supported:

#### Single Line
- "#" (in quotes cause markdown)
- //
- "--" (in quotes cause markdown)

#### Multi-Line
- """ """ or ''' ''' (Python docstrings)
- /* */
- :' '
- %{ %}
- =begin =end

That covers most languages, however if I am missing any commenting styles used by your language, you can request it be added.

## Install
To install, open a terminal and enter this:
> git clone -b python https://github.com/Utecha/LineCounter.git

If you want the Lua or Rust variants of the program, replace 'python' with 'lua' or 'rust'

## Usage

On POSIX compliant systems (Linux/MacOS), you have a couple of options at your disposal.

On Windows, you're basically stuck with option 1 unless you use Windows Subsystem for Linux.

##### Option 1
SINGLE FILE:
> python linecount.py <file_path>

MULTIPLE FILES:
> python linecount.py <file_path1> <file_path2>

NOTE: Debian/Ubuntu based systems and some other Linux distros should use 'python3' rather than 'python', by default.

##### Option 2
By default, the script should be executable. However, if it isn't, enter this in your terminal (assuming you're in the same directory as the script):
> chmod +x linecount.py

Then, you may run the program as such:

SINGLE FILE:
> ./linecount.py <file_path>

MULTIPLE FILES:
> ./linecount.py <file_path1> <file_path2>

##### Option 3
In your .bashrc or .zshrc file, add:
> export PATH="$PATH:Path/To/LineCounter"
> alias count="linecount.py"

Save and exit, then in your terminal, source the .bashrc or .zshrc file, and now you can run the program like this:

SINGLE FILE:
> count <file_path>

MULTIPLE FILES:
> count <file_path1> <file_path2>
