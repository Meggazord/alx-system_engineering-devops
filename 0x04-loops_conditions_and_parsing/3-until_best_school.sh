#!/usr/bin/env bash
# This script is displaying "Best School" 10 times using an until loop

count=0

until [ $count -ge 10 ]; do
    echo "Best School"
    ((count++))
done
