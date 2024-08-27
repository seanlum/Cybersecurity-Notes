# Portable Executable Format

https://en.wikipedia.org/wiki/Portable_Executable

### PE Format Description on OSDev

https://wiki.osdev.org/PE

### PE Format on Microsoft

https://learn.microsoft.com/en-us/windows/win32/debug/pe-format


### Win32 API

https://learn.microsoft.com/en-us/windows/win32/

# Common PE Formats

### Useful book for Processes, Tools, and Analysis
https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals

- [Windows Internals, Part 1: System architecture, processes, threads, memory management, and more, 7th Edition](https://www.microsoftpressstore.com/store/windows-internals-part-1-system-architecture-processes-9780735684188)
- [Windows Internals, Part 2, 7th Edition](https://www.microsoftpressstore.com/store/windows-internals-part-2-9780135462409)
- [Tools for Windows Internals](https://github.com/zodiacon/WindowsInternals)

Common PE Format Files
1.	Executable Files (.exe)
    - Standard application executables that can be run directly by the Windows operating system.
    - https://en.wikipedia.org/wiki/Comparison_of_executable_file_formats
2.	Dynamic Link Libraries (.dll)
•	Shared libraries that contain code and data that can be used by multiple programs simultaneously.
3.	System Files (.sys)
•	Device drivers and other low-level system files that interact with the Windows kernel.
4.	Control Panel Applets (.cpl)
•	Special types of DLLs used to create Control Panel items.
5.	Screen Savers (.scr)
•	Executable files that run as screen savers.
6.	ActiveX Controls (.ocx)
•	Special types of DLLs used for creating reusable software components in Windows.
7.	COM Files (.com)
•	Although traditionally associated with a different format, some .com files in modern Windows systems are actually PE files.
8.	Boot Files (.efi)
•	Executable files used in the UEFI (Unified Extensible Firmware Interface) environment, often found in boot loaders.

To inspect and analyze PE files, you can use various tools:
- PE Explorer: A tool for inspecting the structure of PE files.
- Dependency Walker: A tool for analyzing the dependencies of PE files.
- Resource Hacker: A tool for viewing and editing resources in executables and DLLs.
- CFF Explorer: A freeware suite for PE editing.
- Hex Editors: For examining the raw binary data of PE files.

# Analysis

### Microsoft BinSkim
https://github.com/microsoft/binskim

### PE Explorer
https://www.heaventools.com/overview.htm

### Dependency Walker
https://www.dependencywalker.com/

### PE Tools
https://github.com/petoolse/petools

# In-Memory Analysis

### PE Sieve

https://github.com/hasherezade/pe-sieve

Scans a given process. Recognizes and dumps a variety of potentially malicious implants (replaced/injected PEs, shellcodes, hooks, in-memory patches).

https://github.com/hasherezade/pe-sieve/wiki

# Reverse Engineering

### Binary Ninja

https://binary.ninja/

Binary Ninja is an interactive decompiler, disassembler, debugger, and binary analysis platform built by reverse engineers, for reverse engineers. Developed with a focus on delivering a high-quality API for automation and a clean and usable GUI, Binary Ninja is in active use by malware analysts, vulnerability researchers, and software developers worldwide. Decompile software built for many common architectures on Windows, macOS, and Linux for a single price, or try out one of our limited (but free!) versions.

### Ghidra

https://ghidra-sre.org/

A software reverse engineering (SRE) suite of tools developed by NSA's Research Directorate in support of the Cybersecurity mission

### IDA

The free binary code analysis tool to kickstart your reverse engineering experience.

https://hex-rays.com/ida-free/


### PE Bear

https://github.com/hasherezade/pe-bear-releases

PE-bear is a freeware reversing tool for PE files. Its objective is to deliver fast and flexible “first view” for malware analysts, stable and capable to handle malformed PE files.

https://institute.sektor7.net/view/courses/red-team-operator-malware-development-essentials/214144-portable-executable/624071-pe-bear-looking-inside