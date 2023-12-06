# LineCounter

LineCounter is a command line application to count the number of lines of code in a given file.

It skips any line that is either blank or contains a comment or docstring.

Supported Languages:
- Any language that uses any of these commenting styles:
> " # "
> " // "
> " /**/ "
> " ''' ''' " or ' """ """ '
> " -- "

USAGE:
> ./count.sh <file_path>

The application also supports counting multiple files. Doing so sums up the total count of each file.

USAGE:
> ./count.sh <file_path1> <file_path2>

-------------------------------------------------------

# TODO

- Add more language support
- Add flag to count multiple files separately
- Probably refactor at some point
