# Disassembling a Binary

## objdump
### Supported formats 
```
C:\msys64\mingw64\bin\objdump.exe: supported targets: pe-x86-64 pei-x86-64 pe-bigobj-x86-64 elf64-x86-64 pe-i386 pei-i386 elf32-i386 elf32-iamcu pdb elf64-little elf64-big elf32-little elf32-big srec symbolsrec verilog tekhex binary ihex plugin
C:\msys64\mingw64\bin\objdump.exe: supported architectures: i386 i386:x86-64 i386:x64-32 i8086 i386:intel i386:x86-64:intel i386:x64-32:intel iamcu iamcu:intel
```
### Reading .rodata
- `-sj .rodata` infers including source, and using a section.
    - Equivalent to `--source --section=".rodata"`
```
$ objdump -sj .rodata compilation_example.o
```
```
$ objdump -Sj .text compilation_example.exe
```
### Disassembling a file in Intel format
```
$ objdump -M intel -d <file>
```
### Disassembling all data in a file
```
$ objdump [ -D | --disassemble-all ] <file>
```
### Listing Headers
```
$ objdump -x <file>
```

## readelf

### Reading Sections
```
$ readelf --wide --segments <file>
```

## libbfd
https://ftp.gnu.org/old-gnu/Manuals/bfd-2.9.1/html_mono/bfd.html

### libbfd reference manual
http://www.skyfree.org/linux/references/bfd.pdf