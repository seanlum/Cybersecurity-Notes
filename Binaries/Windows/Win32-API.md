# Win32 API
The Win32 API has been around since the early 90s and still has a great amount of code that has not changed much.

## Terms
- `System Cache`
- `Stack`
- `Heap`
- `Page Tables and Hyper Space`
- `System Page-Table Entries`
- `Pagefile-Backed`
- `Private Allocations`
- `Windows kernel object manager`
- `Virtual Address Descriptor`
    - `Mapped allocations`
    - `Private allocations`
## Libraries

```
NTDLL.dll
WIN32K.sys
```

## Functions
```
ReadFile
WriteFile
CreateFileMapping
ReadProcessMemory
WriteProcessMemory
UmapViewOfFile
VirtualAlloc
VirutalProtect
VirtualQuery
VirtualFree
```