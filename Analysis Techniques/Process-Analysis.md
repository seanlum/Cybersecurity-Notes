# Process Analysis

# Process Analysis on Windows

[Tools for Monitoring Performance Counters and Events](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/tools-monitor-performance-counters-and-events)

## Task Manager

```
WIN+X 
Task Manager
```
```
WIN+R
taskmgr
```
```
cmd.exe taskmgr.exe
```
```
WIN Key
Task Manager
```

## Perfmon

https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/perfmon

[Windows Performance Monitor](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc749249(v=ws.11))

[Overview of Performance Monitor](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc749154(v=ws.10))

```
perfmon </res|report|rel|sys>
```



## PowerShell

```
Get-Process [-Name <name>] [-Id <pid>]
Get-Process | Select-Object Name, Id, CPU, WS
Get-Process | Export-Csv -Path "processes.csv
```
[Get-Process Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process?view=powershell-7.4)

```PowerShell

Name                              Category  Module                    Synopsis
----                              --------  ------                    --------
Enter-PSHostProcess               Cmdlet    Microsoft.PowerShell.Core Connects to and enters into an interactive ses...
Exit-PSHostProcess                Cmdlet    Microsoft.PowerShell.Core Closes an interactive session with a local pro...
Wait-Process                      Cmdlet    Microsoft.PowerShell.M... Waits for the processes to be stopped before a...
Get-Process                       Cmdlet    Microsoft.PowerShell.M... Gets the processes that are running on the loc...
Start-Process                     Cmdlet    Microsoft.PowerShell.M... Starts one or more processes on the local comp...
Stop-Process                      Cmdlet    Microsoft.PowerShell.M... Stops one or more running processes.
Debug-Process                     Cmdlet    Microsoft.PowerShell.M... Debugs one or more processes running on the lo...
Get-AppvVirtualProcess            Function  AppvClient                ...
Start-AppvVirtualProcess          Function  AppvClient                ...
```

## Command Prompt

```
tasklist [/PID] [/FI] [/SVC]
taskkill [/IM <process_name>] [/ID <pid>] [/F]
```
- [tasklist documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tasklist)
- [taskkill documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/taskkill)
## WMIC

```
# list processes
wmic process list brief
# Get process notepad.exe
wmic process where "name='notepad.exe'" get processid, name, commandline
# Filtering by process ID
wmic process where "processid=1234" get name, commandline
# Exporting to a file
wmic process list brief > processes.txt
```
[WMIC Documentation](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic)
### ProcExp, ProcExp64

https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer

## ProcMon
https://learn.microsoft.com/en-us/sysinternals/downloads/procmon

## Process Dumping

## Magnet DumpIt
https://www.magnetforensics.com/resources/magnet-dumpit-for-windows/


### SysInternals ProcDump

https://learn.microsoft.com/en-us/sysinternals/downloads/procdump
```
> procdump -ma <PID> <output_path>
```

### Process Monitoring

https://learn.microsoft.com/en-us/sysinternals/downloads/procmon


## Process Imaging

### FTK-Imager
https://www.exterro.com/digital-forensics-software/ftk-imager

## Process Post-Analysis

### Volatility Framework

https://volatilityfoundation.org/

https://volatilityfoundation.org/the-volatility-framework/

#### [Volatility 3 GitHub](https://github.com/volatilityfoundation/volatility3)
#### [Volatility Documentation](https://volatility3.readthedocs.io/en/latest/)

```
python3 vol.py -f /home/user/samples/stuxnet.vmem windows.info
```

### Yara

```
yara -r rules.yar process_dump.dmp
```

### Rekall
https://github.com/google/rekall

```
# list processes
rekall -f process_dump.dmp pslist

# Find malware
 rekall -f process_dump.dmp malfind
```

# Sandboxing

### Cuckoo Sandbox
https://cuckoosandbox.org/

https://cuckoo.sh/docs/

### CAPEv2
https://github.com/kevoreilly/CAPEv2

https://capev2.readthedocs.io/en/latest/

https://capev2.readthedocs.io/en/latest/installation/index.html

# Process Analysis on Linux

### DumpIt for Linux
https://github.com/MagnetForensics/dumpit-linux