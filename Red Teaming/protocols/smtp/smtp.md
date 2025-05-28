# SMTP - Simple Mail Transfer Protocol 
- [How SMTP Works](https://computer.howstuffworks.com/e-mail-messaging/email.htm#pt3)
- [SMTP protocol explained](https://www.afternerd.com/blog/smtp/)

## SMTP with Metasploit

```
msf6> search smtp_version
msf6> use <option>
msf6> set RHOSTS <ip_addr>
msf6> run
msf6> search smtp_enum
msf6> use <option>
msf6> set RHOSTS <ip_addr>
msf6> set THREADS 12
msf6> set USER_FILE <path_to_usernames>
```