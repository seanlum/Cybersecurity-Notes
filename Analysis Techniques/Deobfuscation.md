# Deobfuscation

## Java Deobfuscation

https://github.com/GenericException/SkidSuite/

https://github.com/Col-E/Recaf



## Tools

## de4dot-cex C Code Deobfuscator

- Supports x86 (native) mode
- Supports normal mode
- Decrypts and inlines constants
- Decrypts resources
- Fixes control flow
- Fixes proxy calls
- Deobfuscated assemblies are runnable

https://github.com/ViRb3/de4dot-cex

## Flare-FLOSS

The FLARE Obfuscated String Solver (FLOSS, formerly FireEye Labs Obfuscated String Solver) uses advanced static analysis techniques to automatically extract and deobfuscate all strings from malware binaries. You can use it just like strings.exe to enhance the basic static analysis of unknown binaries.

Obfuscated Strings
Rather than heavily protecting backdoors with hardcore packers, many malware authors evade heuristic detections by obfuscating only key portions of an executable. Often, these portions are strings and resources used to configure domains, files, and other artifacts of an infection. These key features will not show up as plaintext in the output of the strings.exe utility that we commonly use during basic static analysis.

https://github.com/mandiant/flare-floss

## JS-Deobfuscator

A simple but powerful deobfuscator to remove common JavaScript obfuscation techniques. Open an issue if there is a feature you think should be implemented.

Online version at deobfuscate.io

Install via `npm install js-deobfuscator`

Looking for a deobfuscator specific to Obfuscator.io/javascript-obfuscator? Try this repo

If you would like to discuss/learn about JavaScript obfuscation and deobfuscation you can join the Discord server

https://github.com/ben-sb/javascript-deobfuscator

## obfuscator-io-deobfuscator

### `JavaScript` | `Deobfuscator`

A deobfuscator for scripts obfuscated by Obfuscator.io

#### CLI

Install via `npm install -g obfuscator-io-deobfuscator`

Usage: obfuscator-io-deobfuscator <input> -o [output]

https://github.com/ben-sb/obfuscator-io-deobfuscator

## NETReactorSlayer

### `.NET Eziriz Obfuscator`

NETReactorSlayer is an open source (GPLv3) deobfuscator and unpacker for Eziriz .NET Reactor.

https://github.com/SychicBoy/NETReactorSlayer

https://www.eziriz.com/reactor_download.htm

## PDF Stream Dumper

### `PDF` | `Malware Analysis` | `Reverse Engineering` | `Shellcode` | `Deobfuscator`

### Full feature list
- supported filters: FlateDecode, RunLengthDecode, ASCIIHEXDecode, ASCII85Decode, LZWDecode, JBIG2, CCITTFaxDecode, DecodePredictors
- Integrated shellcode tools:
  - sclog gui (Shellcode Analysis tool I wrote at iDefense)
  - scdbg libemu based Shellcode analysis tool
  - Shellcode_2_Exe functionality
  - Export unescaped bytes to file
- supports filter chaining (ie multiple filters applied to same stream)
- supports unescaping encoded pdf headers
- scriptable interface to process multiple files and generate reports
- view all pdf objects
- view deflated streams
- view stream details such as file offsets, header, etc
- save raw and deflated data
- search streams for strings
- scan for functions which contain pdf exploits (dumb scan)
- format javascript using js beautifier (see credits in readme)
- view streams as hex dumps
- zlib compress/decompress arbitrary files
- replace/update pdf streams with your own data
- basic javascript interface so you can run parts of embedded scripts +  support for using MS Script Debugger
- PdfDecryptor w/source - uses iTextSharp and requires .Net Framework 2.0
- Basic Javascript de-obsfuscator
- can hide: header only streams, duplicate streams, selected streams
- js ui also has access to a toolbox class to
  - simplify fragmented strings
  - read/write files
  - do hexdumps
  - do unicode safe unescapes
  - disassembler engine
  - replicate some common Adobe API (new)