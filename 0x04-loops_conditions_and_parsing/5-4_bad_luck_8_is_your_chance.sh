#!/usr/bin/env bash
# This script displays different messages based on the loop iteration

count=0

while [ $count -lt 10 ]; do
    if [ $count -eq 4 ]; then
        echo "bad luck"
    elif [ $count -eq 8 ]; then
        echo "good luck"
    else
        echo "Best School"
    fi
    ((count++))
done
