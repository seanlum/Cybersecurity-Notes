# Win32 API
The Win32 API has been around since the early 90s and still has a great amount of code that has not changed much.

## Virtual Address Space (Memory Management)
https://learn.microsoft.com/en-us/windows/win32/memory/virtual-address-space?redirectedfrom=MSDN

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
KERNEL32.DLL
GDI32.DLL
ADVAPI32
```

## Functions
```cpp
ReadFile()
WriteFile()
CreateFileMapping()
ReadProcessMemory()
WriteProcessMemory()
UnmapViewOfFile()
VirtualAlloc()
VirutalProtect()
VirtualQuery()
VirtualFree()

CcCopyRead()
CcCopyWrite()

MmAllocateMappingAddress()

HeapAlloc()
HeapFree()

GetMessage()

// Synchronization Objects
WaitForSingleObject()
WaitForMultipleObjects()

// Process Initialization Sequence
CreateProcess()
LdrpInitialize()
BaseProcessStart()

// Exceptions
RaiseException()
KiUserExceptionDispatcher()
RtlDispatchException()

// Generic Table API
RtlNumberGenericTableElements()
RtlDeleteElementGenericTable()
RtlGetElementGenericTable()
RtlEnumerateGenericTable()
RtlEnumerateGenericTableLikeADirectory()
RtlEnumerateGenericTableWithoutSplaying()
RtlInitializeGenericTable()
RtlIsGenericTableEmpty()
RtlInsertElementGenericTable()
RtlLookupElementGenericTable()
RtlNumberGenericTableElements()
RtlLocateNodeGenericTable()
RtlInsertElementGenericTable()
RtlLocateNodeGenericTable()
RtlRealInsertElementWorker()
```



# Order of Operations for Processes
- Process calls Win32 API `CreateProcess`
    - API creates process object and allocates new memory address for the process
- `CreateProcess` maps `NTDLL.DLL` and the program executable to the newly created address space
- `CreateProcess` creates the process's first thread and allocates stack space for it
- The process first thread is resumed and starts running `LdrpInitialize()` within NTDLL.dll
- `LdrpInitialize` recursively traverses the primary executable import tables and maps into memory every executable that is required for running the primary executable
- `LdrpRunInitializeRoutines` -> calling mount points for `DLL_PROCESS_ATTACH`
- DLLs are initialized, `LdrpInitialize` calls the thread's real initialization routine, which is the `BaseProcessStart` function from `KERNEL32.DLL`

# Header Files
### Microsoft Platform SDK
```c
// WinNT.H
_IMAGE_NT_HEADERS
_IMAGE_FILE_HEADER
_IMAGE_OPTIONAL_HEADER

Export Table - IMAGE_EXPORT_DIRECTORY
Import Table - IMAGE_IMPORT_DESCRIPTOR
Resource Table - IMAGE_RESOURCE_DIRECTORY
Base Relocation Table - IMAGE_BASE_RELOCATION
Debugging Information - IMAGE_DEBUG_DIRECTORY
Thread Local Storage Table - IMAGE_TLS_DIRECTORY
Load Configuration Table - IMAGE_LOAD_CONFIG_DIRECTORY
Bound Import Table - IMAGE_BOUUND_IMPORT_DESCRIPTION
Import Address Table (IAT) - A list of 32-bit pointers
Delay Import Descriptor - ImgDelayDescr

Thread Information Block (TIB)
```