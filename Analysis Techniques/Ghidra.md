# Ghidra

Analyzing binaries with Ghidra can be very simple, or very advanced. It comes with some debugging capabilities, reverse engineering capabilities, decompiling / disassembling capabilities. 

After importing a file, which can be one of many formats (PE, ELF, Macho, etc), you can use the `Code Explorer` which can allow you to explore various regions of a binary. For example an ELF file has a symbol tree with `Imports`, `Exports`, `Functions`, `Labels`, `Classes`, and `Namespaces`

# Ghidra Help

`Start Ghidra` > `Code Browser` > `Help` > `Ghidra Help`

### Topics in the Ghidra Help
- Byte Viewer
- Code Browser
- Debugger
- Decompiler 
- Eclipse Integration
- Function ID
- Graphing
- Memory Map
- Program Annotation
- Symbol Table

# Ghidra Read The Docs
- https://low-level.readthedocs.io/en/latest/reversing/ghidra/
  - https://blag.nullteilerfrei.de/2019/07/29/ghidra-msdn-offline-library-love/
# Ghidra API Documentation
https://ghidra.re/ghidra_docs/api/index.html
- [Ghidra ELF format package](https://ghidra.re/ghidra_docs/api/ghidra/app/util/bin/format/elf/package-summary.html)

# Ghidra Installation Guide
https://ghidra-sre.org/InstallationGuide.html