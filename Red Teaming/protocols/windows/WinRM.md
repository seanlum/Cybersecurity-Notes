# Windows Remote Management

- WinRM uses SOAP over web-based connections. It supports HTTP and HTTPs with basic auth, hashes, and kerberos

# pywinrm

### making a command on CMD with pywinrm
```
ghwinrm.py -c -U user%password -t <target_ip> <command>
```

### making a command with PowerShell on pywinrm
```
ghwinrm.py -p -U user%password -t <target_ip> <command>
```