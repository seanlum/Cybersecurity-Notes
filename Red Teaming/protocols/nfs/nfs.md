# Network File System

https://wiki.archlinux.org/title/NFS

https://nfs.sourceforge.net/

```
/usr/bin/showmount -e <target_ip_address>
```

## Attacking NFS Shares
- https://rootrecipe.medium.com/attacking-nfs-shares-b907d5d8d74
- https://pentestmonkey.net/blog/nfs-hardlink

## squashfs vulnerabilities
- [What does all the no squash option do in nfs exports](https://serverfault.com/questions/1089557/what-does-the-no-all-squash-option-do-in-nfs-exports)
### The bad config option
```
no_root_squash
```