#!/usr/bin/env bash
# Check if an IP address is reachable using ping

if [ $# -ne 1 ]; then
    echo "Usage: $0 {IP_ADDRESS}"
    exit 1
fi

ip_address=$1

ping -c 5 $ip_address
