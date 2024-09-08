# Install error 0x80004005 on Kali Linux

### Install command

```
wsl --install kali-linux
```

https://answers.microsoft.com/en-us/windows/forum/all/wslregisterdistribution-failed-with-error/dd28f58e-869a-4a33-8b7f-95695371cb0d

### Make sure WSL is properly installed

```cmd
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /al
```

### Set the Registry Key

- 3 is for Manual
- 2 is for Automatic

```powershell
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LxssManager" -Name "Start"
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LxssManager" -Name "Start" -Value 2
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LxssManager" -Name "Start"
```

### Ensure the service is started
```cmd
net start LxssManager
```

### Make sure WSL is set to version 2

```
wsl --set-default-version 2
```


### Make sure WSL is up to date 

```
wsl --update
```

### Install Kali Linux

```
wsl --install --distribution kali-linux
```