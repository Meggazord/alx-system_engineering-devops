#!/usr/bin/env bash
# This script displays the time for 12 hours and 59 minutes

hour=0

while [ $hour -le 12 ]; do
    echo "Hour: $hour"
    
    minute=1
    while [ $minute -le 59 ]; do
        echo $minute
        ((minute++))
    done
    
    ((hour++))
done
