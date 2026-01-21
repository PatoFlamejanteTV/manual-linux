#!/bin/bash

# Get the absolute path to the directory where the script lives (tools/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

# Target the 'site' folder which is a sibling to 'tools'
TARGET_DIR="$SCRIPT_DIR/../site"

if [ -d "$TARGET_DIR" ]; then
    # -type f: find files only
    # -size -1000c: size less than 1000 bytes
    find "$TARGET_DIR" -type f -size -500c
else
    echo "Error: Could not find 'site' directory at $TARGET_DIR"
    #exit 1
fi
