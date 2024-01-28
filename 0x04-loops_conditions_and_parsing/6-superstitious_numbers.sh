#!/usr/bin/env bash
# This script displays numbers and associated messages for certain iterations

count=1

while [ $count -le 20 ]; do
    case $count in
        4)
            echo "bad luck from China"
            ;;
        9)
            echo "bad luck from Japan"
            ;;
        17)
            echo "bad luck from Italy"
            ;;
        *)
            echo $count
            ;;
    esac
    ((count++))
done
