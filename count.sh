#!/bin/sh

if [ -z "$1" ]; then
	echo "Usage: $0 <file_path>"
	exit 1
fi

SCRIPT_DIR="$(dirname "$0")"
source "/usr/lib/python3.11/venv/scripts/common/activate"
python "${SCRIPT_DIR}/linecount.py" "$@"
