#!/usr/bin/env bash
# This script displays "Best School" 10 times and says Hi on the 9th iteration

count=0

while [ $count -lt 10 ]; do
    if [ $count -eq 9 ]; then
        echo "Best School"
        echo "Hi"
    else
        echo "Best School"
    fi
    ((count++))
done
