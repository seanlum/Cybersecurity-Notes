# Finding SUID Files

```
find <directory_name> -perm /4000

find / -perm -u=s -type f 2>/dev/null
```