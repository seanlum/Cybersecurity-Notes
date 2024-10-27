# Windows User Space Emulator

https://github.com/momo5502/emulator

This project is a work in progress as of 10-27-2024

A high-performance Windows process emulator that operates at the syscall level, providing full control over process execution through comprehensive hooking capabilities.

Built in C++ and powered by the Unicorn Engine.

- Syscall-Level Emulation: Instead of reimplementing Windows APIs, the emulator operates at the syscall level, allowing it to leverage existing system DLLs
- Advanced Memory Management: Supports Windows-specific memory types including reserved, committed, built on top of Unicorn's memory management
- Complete PE Loading: Handles executable and DLL loading with proper memory mapping, relocations, and TLS
- Exception Handling: Implements Windows structured exception handling (SEH) with proper exception dispatcher and unwinding support
- Threading Support: Provides a scheduled (round-robin) threading model
- State Management: Supports both full state serialization and fast in-memory snapshots
- Debugging Interface: Implements GDB serial protocol for integration with common debugging tools (IDA Pro, GDB, LLDB, VS Code, ...)

Perfect for security research, malware analysis, and DRM research where fine-grained control over process execution is required.