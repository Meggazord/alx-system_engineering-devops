#!/usr/bin/env bash
# This script displays the content of the current directory in a list format

for file in *; do
    if [[ $file != .* ]]; then
        name_after_dash=$(echo "$file" | cut -d '-' -f 2-)
        echo "$name_after_dash"
    fi
done
