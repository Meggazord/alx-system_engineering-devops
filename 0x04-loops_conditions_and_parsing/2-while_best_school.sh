#!/usr/bin/env bash
# This script is displaying "Best School" 10 times using a while loop

count=0

while [ $count -lt 10 ]; do
    echo "Best School"
    ((count++))
done
