# Zip Archive Passwords

Within Kali Linux, you can crack passwords for files pretty easily in most cases if you already have the password.

```
└─$ sudo apt install wordlists
└─$ sudo apt install fcrackzip
└─$ dpkg-query -L  wordlists
/.
/usr
/usr/bin
/usr/bin/wordlists
/usr/share
/usr/share/doc
/usr/share/doc/wordlists
/usr/share/doc/wordlists/changelog.gz
/usr/share/doc/wordlists/copyright
/usr/share/wordlists
/usr/share/wordlists/rockyou.txt.gz
└─$ sudo gunzip /usr/share/wordlists/rockyou.txt.gz
└─$ fcrackzip -v -D -p /usr/share/wordlists/rockyou.txt ../noise_samples.zip
found file 'brown.wav', (size cp/uc 3922359/3969044, flags 9, chk 73cf)
found file 'location.wav', (size cp/uc    998/129564, flags 9, chk 73cf)
found file 'wahwah.wav', (size cp/uc 7663461/7938044, flags 9, chk 73cf)
found file 'white.wav', (size cp/uc 12607488/23040082, flags 9, chk 7aba)
possible pw found: garfield ()
checking pw 05546TUNmaneerat
```