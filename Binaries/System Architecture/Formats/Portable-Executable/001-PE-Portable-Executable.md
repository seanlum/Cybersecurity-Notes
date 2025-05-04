# Windows PE Format

## [PE Format Documentation](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format)

## [pypyi pefile](https://pypi.org/project/pefile/)

```
> python -m pefile <exe_file>
```

###  [PEFile Format](https://drive.google.com/file/d/0B3_wGJkuWLytbnIxY1J5WUs4MEk/view?pli=1&resourcekey=0-n5zZ2UW39xVTH8ZSu6C2aQ)

### General Concepts

| Name | Description |
|------|-------------|
| attribute certificate | A certificate for signing. Includes software manufacturer, digest and it uses PKI |
| date/time stamp | If the timestamp is 0 or 0xFFFFFFFF, it does not represent a real or meaningful date/time stamp |
| file pointer | location in the file which is for being processed by the linker or the loader |
| linker | A reference to the linker that is provided with Microsoft Visual Studio |
| object file | the image file | 
| reserved, must be 0 | for generators and consumers |
| Relative Virtual Address (RVA) | place on disk which references a section for linking |
| Section | Basic unit of code in a PE or COFF file |
| Virtual Address | Same as the RVA but without the base subtracted | 

## [PE Anatomy](https://upload.wikimedia.org/wikipedia/commons/1/1b/Portable_Executable_32_bit_Structure_in_SVG_fixed.svg)

# Finding the Entry Point

```hex
If you see:

    ImageBase = 0x400000
    BaseOfCode = 0x1000
    .text VirtualAddress = 0x1000
    .data VirtualAddress = 0x3000
    AddressOfEntryPoint = 0x1200

Then in memory:

    .text section gets mapped at 0x400000 + 0x1000 = 0x401000
    .data section gets mapped at 0x400000 + 0x3000 = 0x403000

CPU starts execution at 0x400000 + 0x1200 = 0x401200
```

```as
> python -m pefile <exe_file>
...

[IMAGE_OPTIONAL_HEADER64]
0xF8       0x0   Magic:                         0x20B
0xFA       0x2   MajorLinkerVersion:            0xE
0xFB       0x3   MinorLinkerVersion:            0x2A
0xFC       0x4   SizeOfCode:                    0x15C00
0x100      0x8   SizeOfInitializedData:         0xD000
0x104      0xC   SizeOfUninitializedData:       0x0
// Where the program starts, the .text section
0x108      0x10  AddressOfEntryPoint:           0x11460
// This is where the image loading starts
// ImageBase + BaseOfCode
0x10C      0x14  BaseOfCode:                    0x1000
0x110      0x18  ImageBase:                     0x140000000

0x118      0x20  SectionAlignment:              0x1000
0x11C      0x24  FileAlignment:                 0x200
0x120      0x28  MajorOperatingSystemVersion:   0x6
0x122      0x2A  MinorOperatingSystemVersion:   0x0
0x124      0x2C  MajorImageVersion:             0x0
0x126      0x2E  MinorImageVersion:             0x0
0x128      0x30  MajorSubsystemVersion:         0x6
0x12A      0x32  MinorSubsystemVersion:         0x0
0x12C      0x34  Reserved1:                     0x0
0x130      0x38  SizeOfImage:                   0x27000
0x134      0x3C  SizeOfHeaders:                 0x400
0x138      0x40  CheckSum:                      0x0
0x13C      0x44  Subsystem:                     0x3
0x13E      0x46  DllCharacteristics:            0xC160
0x140      0x48  SizeOfStackReserve:            0x180000
0x148      0x50  SizeOfStackCommit:             0x1000
0x150      0x58  SizeOfHeapReserve:             0x100000
0x158      0x60  SizeOfHeapCommit:              0x1000
0x160      0x68  LoaderFlags:                   0x0
0x164      0x6C  NumberOfRvaAndSizes:           0x10
DllCharacteristics: IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE, IMAGE_DLLCHARACTERISTICS_GUARD_CF, IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA, IMAGE_DLLCHARACTERISTICS_NX_COMPAT, IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE
...
```
#### CFFExplorer
```
Open File...
File: <EXE_Name>
    Nt Headers
        Optional Header
            > AddressOfEntryPoint       
            > BaseOfCode                0x00001000
            > ImageBase                 0x0000000140000000
```