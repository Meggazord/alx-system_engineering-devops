#!/usr/bin/env bash
# Display listening ports with PID and program name

echo "Active Internet connections (only servers)"
echo "Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name"

# Display TCP listening ports
netstat -tln | awk '$6 == "LISTEN" {print "tcp", $1, $4, $7}' | while read proto local foreign state; do
    pid=$(lsof -i -n -P | grep "$local" | awk '{print $2}')
    program=$(ps -p $pid -o comm=)
    echo "tcp        0      0 $local $foreign $state      $pid/$program"
done

# Display UDP listening ports
netstat -uln | awk '$6 == "UNCONN" {print "udp", $1, $4, $7}' | while read proto local foreign state; do
    pid=$(lsof -i -n -P | grep "$local" | awk '{print $2}')
    program=$(ps -p $pid -o comm=)
    echo "udp        0      0 $local $foreign             $pid/$program"
done

echo "Active UNIX domain sockets (only servers)"
echo "Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path"

# Display UNIX domain sockets
netstat -lx | grep ^unix | awk '{print $1, $6, $7, $8, $9, $10}' | while read proto refcnt flags type state inode; do
    pid=$(lsof -U -n | grep "$inode" | awk '{print $2}')
    program=$(ps -p $pid -o comm=)
    echo "unix  $refcnt      $flags     $type      $state        $inode   $pid/$program"
done
