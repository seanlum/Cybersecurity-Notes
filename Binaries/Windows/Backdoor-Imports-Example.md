## Example of Imports of a Backdoor
```c#
DeleteFileA
ExitProcess
ExpandEnvironmentStringsA
FreeLibrary
GetCommandLineA
GetLastError
GetModuleFileNameA
GetModuleHandleA
GetProcAddress
GetSystemDirectoryA
CloseHandle
GetTempPathA
GetTickCount
GetVersionExA
LoadLibraryA
CopyFileA
OpenProcess
ReleaseMutex
RtlUnwind
CreateFileA
Sleep
TerminateProcess
TerminateThread
WriteFileCreateMutexA
CreateThread 

// ADVAPI32.DLL
GetUserNameA
RegDeleteValueA
RegCreateKeyExA
RegCloseKey
RegQueryValueA
RegSetValueExA

// CRTDLL.DLL
__GetMainArgs
atoi
exit
free
malloc
memset
printf
raise
rand
signal
sprintf
srand
strcat
strchr
strcmp
strncpy
strstr
strtok

// SHELL32.DLL
ShellExecuteA

// USER32.DLL
CharUpperBuffA

// WININET.DLL
InternetCloseHandle
InternetGetConnectedState
InternetOpenA
InternetOpenUrlA
InternetReadFile

// WS2_32.DLL
WSACleanup
listen
ioctlsocket
inet_addr
htons
getsockname
socket
gethostbyname
gethostbyaddr
connect
closesocket
bind
accept
__WSAFDIsSet
WSAStartup
send
select
recv
```

# Stages
```
Setup code loads resource into C:\WINNT\system32\ZoneLockup.exe
Function uses CopyFileA after resource to ZoneLockup.exe
ZoneLockup.exe is loaded with ShellExecuteA
ExitProcess
GetCommandLineA
```
```
WININET.InternetGetConnectedState
set timeout to 30000 ms
Sleep if connection stat is not desired value
Otherwise call gethostbyname 
Establish socket with WinSock2 with connect over proprietary port
```
```
Generate random string for initialization
Join server with IRC
Binary executes codes with the backdoor
```