# macOS

### Listing Connections
```
# All connections
$ netstat -a

# IPv4
$ netstat -f inet

# IPv6
$ netstat -f inet6

# UNIX Sockets
$ netstat -f unix

# TCP connections
$ netstat -p tcp

# UDP connections
$ netstat -p udp
```

### Listing connections with lsof
```
# all TCP/IP connections
$ lsof -i

# IPv4 connections
$ lsof -i 4

# IPv6 connections
$ lsof -i 6

# Listing just the command, pid, and connection info
$ lsof -i -nP | awk 'NR==1 {print $1, $2, $9} NR>1 {print $1, $2, $9}'
```

### Displaying the routing table
```
$ netstat -r 
```

## Objective-See Netiquette
#### [Netiquette GUI Program (Included with LuLu)](https://objective-see.org/products/netiquette.html)
#### [https://github.com/objective-see/Netiquette/tree/master](https://github.com/objective-see/Netiquette/tree/master)

## Displaying Network Connections with Python

```
# Does not require root
$ python3 connections-lsof-ps.py

# Requires root 
$ python3 connections-psutil.py
```