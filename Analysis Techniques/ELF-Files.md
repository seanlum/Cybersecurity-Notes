# ELF Specification
[TIS Committee [May 1995] Tool Interface Standard (TIS) Executable and Linking Format (ELF) Specification - Version 1.2](https://refspecs.linuxfoundation.org/elf/elf.pdf)

```
iii

Preface
This Executable and Linking Format Specification, Version 1.2, is the result of the work of the Tool Interface Standards (TIS) Committee--an association of members of the microcomputer industry formed to work toward standardization of the software interfaces visible to development tools for 32-bit Intel Architecture operating environments. Such interfaces include object module formats, executable file formats, and debug record information and formats.

The goal of the committee is to help streamline the software development process throughout the microcomputer industry, currently concentrating on 32-bit operating environments. To that end, the committee has developed specifications--some for file formats that are portable across leading industry operating systems, and others describing formats for 32-bit Windows * operating systems. Originally distributed collectively as the TIS Portable Formats Specifications Version 1.1, these specifications are now separated and distributed individually.
```

## Google Dork for ELF information
https://www.google.com/search?q=site%3Arefspecs.linuxbase.org+inurl%3Aelf

## [elf(5) man page](https://man7.org/linux/man-pages/man5/elf.5.html)

## [LLVM ELF Doxygen](https://llvm.org/docs/doxygen/namespacellvm_1_1ELF.html) 

## ELF and ABI Standards
https://refspecs.linuxfoundation.org/

## ELF.h - Linux Source
### [linux/include/uapi/linux/elf.h](https://github.com/torvalds/linux/blob/master/include/uapi/linux/elf.h)

#### Section Headers
```c
typedef struct elf32_shdr {
  Elf32_Word	sh_name;
  Elf32_Word	sh_type;
  Elf32_Word	sh_flags;
  Elf32_Addr	sh_addr;
  Elf32_Off	sh_offset;
  Elf32_Word	sh_size;
  Elf32_Word	sh_link;
  Elf32_Word	sh_info;
  Elf32_Word	sh_addralign;
  Elf32_Word	sh_entsize;
} Elf32_Shdr;

typedef struct elf64_shdr {
  Elf64_Word sh_name;		/* Section name, index in string tbl */
  Elf64_Word sh_type;		/* Type of section */
  Elf64_Xword sh_flags;		/* Miscellaneous section attributes */
  Elf64_Addr sh_addr;		/* Section virtual addr at execution */
  Elf64_Off sh_offset;		/* Section file offset */
  Elf64_Xword sh_size;		/* Size of section in bytes */
  Elf64_Word sh_link;		/* Index of another section */
  Elf64_Word sh_info;		/* Additional section information */
  Elf64_Xword sh_addralign;	/* Section alignment */
  Elf64_Xword sh_entsize;	/* Entry size if section holds table */
} Elf64_Shdr;
```

## LSB ELF Format 
- [ELF Sections](https://refspecs.linuxbase.org/LSB_4.1.0/LSB-Core-generic/LSB-Core-generic/sections.html)
- [Executable and Linking Format (ELF)](https://refspecs.linuxbase.org/LSB_4.1.0/LSB-Core-generic/LSB-Core-generic/elf-generic.html)
- [System V Application Binary Interface | AMD64 Specification](https://refspecs.linuxbase.org/elf/x86_64-abi-0.99.pdf)
### Sections of ELF files
- [Linkers part 8 - ELF Segments](https://www.airs.com/blog/archives/45)
- [ELF Special Sections](https://refspecs.linuxbase.org/LSB_3.1.1/LSB-Core-generic/LSB-Core-generic/specialsections.html)

# Debugging ELF Files
- [Binaries/Debuggers-gdb.md](../Binaries/Debuggers-gdb.md)

# Reverse-Engineering ELF Files
- [IDA Documentation](https://hex-rays.com/documentation/)
- [Analysis Techniques/Ghidra.md](./Ghidra.md)


# Dumping Sections of ELF Files

## Listing sections of ELF files with objdump
```
$ objdump -h kangaroo.elf64

kangaroo.elf64:     file format elf64-x86-64

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .interp       0000001c  0000000000000318  0000000000000318  00000318  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  1 .note.gnu.property 00000020  0000000000000338  0000000000000338  00000338  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  2 .note.gnu.build-id 00000024  0000000000000358  0000000000000358  00000358  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  3 .note.ABI-tag 00000020  000000000000037c  000000000000037c  0000037c  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .gnu.hash     00000024  00000000000003a0  00000000000003a0  000003a0  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  5 .dynsym       00000090  00000000000003c8  00000000000003c8  000003c8  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  6 .dynstr       00000088  0000000000000458  0000000000000458  00000458  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  7 .gnu.version  0000000c  00000000000004e0  00000000000004e0  000004e0  2**1
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  8 .gnu.version_r 00000030  00000000000004f0  00000000000004f0  000004f0  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  9 .rela.dyn     000000d8  0000000000000520  0000000000000520  00000520  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 10 .init         0000001b  0000000000001000  0000000000001000  00001000  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 11 .plt          00000010  0000000000001020  0000000000001020  00001020  2**4
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 12 .plt.got      00000008  0000000000001030  0000000000001030  00001030  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 13 .text         0000010f  0000000000001040  0000000000001040  00001040  2**4
...
```

## Dumping sections of ELF files with objdump
```
$ objdump -s -j .text kangaroo.elf64

kangaroo.elf64:     file format elf64-x86-64

Contents of section .text:
 1040 f30f1efa 31ed4989 d15e4889 e24883e4  ....1.I..^H..H..
 1050 f0505445 31c031c9 488d3dd1 000000ff  .PTE1.1.H.=.....
 1060 15732f00 00f4662e 0f1f8400 00000000  .s/...f.........
```

## Dumping symbols with objdump

```
$ objdump -t kangaroo.elf64

kangaroo.elf64:     file format elf64-x86-64

SYMBOL TABLE:
0000000000000000 l    df *ABS*  0000000000000000              Scrt1.o
000000000000037c l     O .note.ABI-tag  0000000000000020              __abi_tag
0000000000000000 l    df *ABS*  0000000000000000              crtstuff.c
0000000000001070 l     F .text  0000000000000000              
...
```