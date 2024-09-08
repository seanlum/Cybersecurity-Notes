# GDB - The GNU Source-Level Debugger

### [Current | Debugging with GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/)

### [Supported Languages](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Supported-Languages.html#Supported-Languages)

### Help 

```
help show
help info
help set
help run
help start
```


## Logging
### [Logging Output](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Logging-Output.html#Logging-Output)

### set logging
```
(gdb) help set logging
Set logging options.

List of set logging subcommands:

set logging debugredirect -- Set the logging debug output mode.
set logging enabled -- Enable logging.
set logging file -- Set the current logfile.
set logging overwrite -- Set whether logging overwrites or appends to the log file.
set logging redirect -- Set the logging output mode.

Type "help set logging" followed by set logging subcommand name for full documentation.
Type "apropos word" to search for commands related to "word".
Type "apropos -v word" for full documentation of commands related to "word".
Command name abbreviations are allowed if unambiguous.
```

### show logging
```
(gdb) help show logging
Show logging options.

List of show logging subcommands:

show logging debugredirect -- Show the logging debug output mode.
show logging enabled -- Show whether logging is enabled.
show logging file -- Show the current logfile.
show logging overwrite -- Show whether logging overwrites or appends to the log file.
show logging redirect -- Show the logging output mode.

Type "help show logging" followed by show logging subcommand name for full documentation.
Type "apropos word" to search for commands related to "word".
Type "apropos -v word" for full documentation of commands related to "word".
Command name abbreviations are allowed if unambiguous.
```

## Recording
```
(gdb) help record
record, rec
Start recording.

List of record subcommands:

record btrace, record b -- Start branch trace recording.
record delete, record del, record d -- Delete the rest of execution log and start recording it anew.
record full -- Start full execution recording.
record function-call-history -- Prints the execution history at function granularity.
record goto -- Restore the program to its state at instruction number N.
record instruction-history -- Print disassembled instructions stored in the execution log.
record save -- Save the execution log to a file.
record stop, record s -- Stop the record/replay target.

Type "help record" followed by record subcommand name for full documentation.
Type "apropos word" to search for commands related to "word".
Type "apropos -v word" for full documentation of commands related to "word".
Command name abbreviations are allowed if unambiguous.
```

## Processes 

### [Analysis Techniques\Process Analysis](../Analysis%20Techniques/Process-Analysis.md)

#### [Attach to a running process](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Attach.html#Attach)

```
attach <pid>
```

#### [Kill a process](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Kill-Process.html#Kill-Process)
```
kill <pid>
```

## Run and Start
#### [Starting a program in GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Starting.html)
```
run
r

(gdb) help run
run, r
Start debugged program.
You may specify arguments to give it.
Args may include "*", or "[...]"; they are expanded using the
shell that will start the program (specified by the "$SHELL" environment
variable).  Input and output redirection with ">", "<", or ">>"
are also allowed.

With no arguments, uses arguments last specified (with "run" or
"set args").  To cancel previous arguments and run with no arguments,
use "set args" without arguments.

To start the inferior without using a shell, use "set startup-with-shell off".
```
```
start
starti

(gdb) help start
Start the debugged program stopping at the beginning of the main procedure.
You may specify arguments to give it.
Args may include "*", or "[...]"; they are expanded using the
shell that will start the program (specified by the "$SHELL" environment
variable).  Input and output redirection with ">", "<", or ">>"
are also allowed.

With no arguments, uses arguments last specified (with "run" or
"set args").  To cancel previous arguments and run with no arguments,
use "set args" without arguments.

To start the inferior without using a shell, use "set startup-with-shell off".
```

## Execution Stack

To get the execution stack, you can use `disassemble` and you can also inspect the `$pc` Pointer Counter variable.

```
(gdb) help disassemble
Disassemble a specified section of memory.
Usage: disassemble[/m|/r|/s] START [, END]
Default is the function surrounding the pc of the selected frame.

With a /s modifier, source lines are included (if available).
In this mode, the output is displayed in PC address order, and
file names and contents for all relevant source files are displayed.

With a /m modifier, source lines are included (if available).
This view is "source centric": the output is in source line order,
regardless of any optimization that is present.  Only the main source file
is displayed, not those of, e.g., any inlined functions.
This modifier hasn't proved useful in practice and is deprecated
in favor of /s.

With a /r modifier, raw instructions in hex are included.

With a single argument, the function surrounding that address is dumped.
Two arguments (separated by a comma) are taken as a range of memory to dump,
  in the form of "start,end", or "start,+length".

Note that the address is interpreted as an expression, not as a location
like in the "break" command.
So, for example, if you want to disassemble function bar in file foo.c
you must type "disassemble 'foo.c'::bar" and not "disassemble foo.c:bar".
```

```gdb
Breakpoint 1, 0x00000000004010c0 in _start ()
(gdb) disassemble
Dump of assembler code for function _start:
=> 0x00000000004010c0 <+0>:     endbr64
   0x00000000004010c4 <+4>:     xor    %ebp,%ebp
   0x00000000004010c6 <+6>:     mov    %rdx,%r9
   0x00000000004010c9 <+9>:     pop    %rsi
   0x00000000004010ca <+10>:    mov    %rsp,%rdx
   0x00000000004010cd <+13>:    and    $0xfffffffffffffff0,%rsp
   0x00000000004010d1 <+17>:    push   %rax
   0x00000000004010d2 <+18>:    push   %rsp
   0x00000000004010d3 <+19>:    xor    %r8d,%r8d
   0x00000000004010d6 <+22>:    xor    %ecx,%ecx
   0x00000000004010d8 <+24>:    mov    $0x401243,%rdi
   0x00000000004010df <+31>:    call   *0x2f03(%rip)        # 0x403fe8
   0x00000000004010e5 <+37>:    hlt
End of assembler dump.
(gdb) backtrace 15
#0  0x00000000004010c0 in _start ()
(gdb) x/15i $pc
=> 0x4010c0 <_start>:   endbr64
   0x4010c4 <_start+4>: xor    %ebp,%ebp
   0x4010c6 <_start+6>: mov    %rdx,%r9
   0x4010c9 <_start+9>: pop    %rsi
   0x4010ca <_start+10>:        mov    %rsp,%rdx
   0x4010cd <_start+13>:        and    $0xfffffffffffffff0,%rsp
   0x4010d1 <_start+17>:        push   %rax
   0x4010d2 <_start+18>:        push   %rsp
   0x4010d3 <_start+19>:        xor    %r8d,%r8d
   0x4010d6 <_start+22>:        xor    %ecx,%ecx
   0x4010d8 <_start+24>:        mov    $0x401243,%rdi
   0x4010df <_start+31>:        call   *0x2f03(%rip)        # 0x403fe8
   0x4010e5 <_start+37>:        hlt
   0x4010e6:    cs nopw 0x0(%rax,%rax,1)
   0x4010f0 <_dl_relocate_static_pie>:  endbr64
(gdb)
```

## Navigation

#### step
```
(gdb) help step
step, s
Step program until it reaches a different source line.
Usage: step [N]
Argument N means step N times (or till program stops for another reason).
```

### stepi

```
(gdb) help stepi
stepi, si
Step one instruction exactly.
Usage: stepi [N]
Argument N means step N times (or till program stops for another reason).
```

### nexti
```
(gdb) help nexti
nexti, ni
Step one instruction, but proceed through subroutine calls.
Usage: nexti [N]
Argument N means step N times (or till program stops for another reason).
```

#### next
```
(gdb) help next
next, n
Step program, proceeding through subroutine calls.
Usage: next [N]
Unlike "step", if the current source line calls a subroutine,
this command does not enter the subroutine, but instead steps over
the call, in effect treating it as a single source line.
```

#### continue
```
(gdb) help continue
continue, fg, c
Continue program being debugged, after signal or breakpoint.
Usage: continue [N]
If proceeding from breakpoint, a number N may be used as an argument,
which means to set the ignore count of that breakpoint to N - 1 (so that
the breakpoint won't break until the Nth time it is reached).

If non-stop mode is enabled, continue only the current thread,
otherwise all the threads in the program are continued.  To
continue all stopped threads in non-stop mode, use the -a option.
Specifying -a and an ignore count simultaneously is an error.
```

#### jump
```
(gdb) help jump
jump, j
Continue program being debugged at specified line or address.
Usage: jump LOCATION
Give as argument either LINENUM or *ADDR, where ADDR is an expression
for an address to start at.
```

#### skip
```
(gdb) help skip
Ignore a function while stepping.

Usage: skip [FUNCTION-NAME]
       skip [FILE-SPEC] [FUNCTION-SPEC]
If no arguments are given, ignore the current function.

FILE-SPEC is one of:
       -fi|-file FILE-NAME
       -gfi|-gfile GLOB-FILE-PATTERN
FUNCTION-SPEC is one of:
       -fu|-function FUNCTION-NAME
       -rfu|-rfunction FUNCTION-NAME-REGULAR-EXPRESSION

List of skip subcommands:

skip delete -- Delete skip entries.
skip disable -- Disable skip entries.
skip enable -- Enable skip entries.
skip file -- Ignore a file while stepping.
skip function -- Ignore a function while stepping.

Type "help skip" followed by skip subcommand name for full documentation.
Type "apropos word" to search for commands related to "word".
Type "apropos -v word" for full documentation of commands related to "word".
Command name abbreviations are allowed if unambiguous.
```

#### finish
```
(gdb) help finish
finish, fin
Execute until selected stack frame returns.
Usage: finish
Upon return, the value returned is printed and put in the value history.
```

### If recording is enabled
```
reverse-step
reverse-next
reverse-continue
```

## args
#### [Program Arguments](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Arguments.html#Arguments)
```
show args

(gdb) help show args
Show argument list to give program being debugged when it is started.
Follow this command with any number of args, to be passed to the program.

set args

(gdb) help set args
Set argument list to give program being debugged when it is started.
Follow this command with any number of args, to be passed to the program.
```

## env or environment
#### [Show program environment](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Environment.html#Environment)
```
show paths
(gdb) help show paths
Current search path for finding object files.
$cwd in the path means the current working directory.
This path is equivalent to the $PATH shell variable.  It is a list of
directories, separated by colons.  These directories are searched to find
fully linked executable files and separately compiled object files as needed.
```
```
show environment [varname]
show env [varname]

(gdb) show env SHELL
SHELL = /bin/bash

set environment <pathname> [value]
set env <pathname> [value]

(gdb) help show env
The environment to give the program, or one variable's value.
With an argument VAR, prints the value of environment variable VAR to
give the program being debugged.  With no arguments, prints the entire
environment to be given to the program.
```


## Threads

#### [Threads](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Threads.html#Threads)

```
# Switch threads
thread <thread-id>

# print thread events
set print thread-events [on|off]

# show thread debug information
show debug threads [on|off]

# Info on threads
info threads [-gid] [thread-id-list]

# Thread commands
thread apply [thread-id-list | all [-ascending]] [flag]... command
```

## Memory

### [Examining Memory](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Memory.html#Memory)

```
x/nfu addr 

n, the repeat count
f, the format-string type
u, the unit size (b, h, w, g)

(gdb) help x
Examine memory: x/FMT ADDRESS.
ADDRESS is an expression for the memory address to examine.
FMT is a repeat count followed by a format letter and a size letter.
Format letters are o(octal), x(hex), d(decimal), u(unsigned decimal),
  t(binary), f(float), a(address), i(instruction), c(char), s(string)
  and z(hex, zero padded on the left).
Size letters are b(byte), h(halfword), w(word), g(giant, 8 bytes).
The specified number of objects of the specified size are printed
according to the format.  If a negative number is specified, memory is
examined backward from the address.

Defaults for format and size letters are those previously used.
Default count is 1.  Default address is following last thing printed
with this command or "print".
```

### [Searching Memory](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Searching-Memory.html#Searching-Memory)
```
(gdb) help find
Search memory for a sequence of bytes.
Usage:
find [/SIZE-CHAR] [/MAX-COUNT] START-ADDRESS, END-ADDRESS, EXPR1 [, EXPR2 ...]
find [/SIZE-CHAR] [/MAX-COUNT] START-ADDRESS, +LENGTH, EXPR1 [, EXPR2 ...]
SIZE-CHAR is one of b,h,w,g for 8,16,32,64 bit values respectively,
and if not specified the size is taken from the type of the expression
in the current language.
The two-address form specifies an inclusive range.
Note that this means for example that in the case of C-like languages
a search for an untyped 0x42 will search for "(int) 0x42"
which is typically four bytes, and a search for a string "hello" will
include the trailing '\0'.  The null terminator can be removed from
searching by using casts, e.g.: {char[5]}"hello".

The address of the last match is stored as the value of "$_".
Convenience variable "$numfound" is set to the number of matches.
```
```
# From gdb docs
(gdb) find &hello[0], +sizeof(hello), "hello"
0x804956d <hello.1620+6>
1 pattern found
(gdb) find &hello[0], +sizeof(hello), 'h', 'e', 'l', 'l', 'o'
0x8049567 <hello.1620>
0x804956d <hello.1620+6>
2 patterns found.
(gdb) find &hello[0], +sizeof(hello), {char[5]}"hello"
0x8049567 <hello.1620>
0x804956d <hello.1620+6>
2 patterns found.
(gdb) find /b1 &hello[0], +sizeof(hello), 'h', 0x65, 'l'
0x8049567 <hello.1620>
1 pattern found
(gdb) find &mixed, +sizeof(mixed), (char) 'c', (short) 0x1234, (int) 0x87654321
0x8049560 <mixed.1625>
1 pattern found
(gdb) print $numfound
$1 = 1
(gdb) print $_
$2 = (void *) 0x8049560
```

### [Assigning Memory](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Assignment.html#Assignment)

```
whatis <variable>

set var <variable>=<value>

(gdb) help set var
set variable, set var
Evaluate expression EXP and assign result to variable VAR.
Usage: set variable VAR = EXP
This uses assignment syntax appropriate for the current language
(VAR = EXP or VAR := EXP for example).
VAR may be a debugger "convenience" variable (names starting
with $), a register (a few standard names starting with $), or an actual
variable in the program being debugged.  EXP is any valid expression.
This may usually be abbreviated to simply "set".

set {int}0x83040 = 4
```
## Libraries

```
(gdb) info sharedlibrary
From                To                  Syms Read   Shared Object Library
0x00007ffff7fcb000  0x00007ffff7ff0875  Yes (*)     ./ld-linux-x86-64.so.2
0x00007ffff7e063c0  0x00007ffff7f5f0dd  Yes (*)     ./libc.so.6
(*): Shared library is missing debugging information.
```

## Functions

```
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401070  setvbuf@plt
0x0000000000401080  puts@plt
0x0000000000401090  __stack_chk_fail@plt
0x00000000004010a0  printf@plt
0x00000000004010b0  fgets@plt
0x00000000004010c0  _start
0x00000000004010f0  _dl_relocate_static_pie
0x0000000000401100  deregister_tm_clones
0x0000000000401130  register_tm_clones
0x0000000000401170  __do_global_dtors_aux
0x00000000004011a0  frame_dummy
0x00000000004011a6  setup
0x000000000040120b  hello
0x0000000000401243  main
0x0000000000401314  _fini
0x00007ffff7fcb1e0  _dl_signal_exception
0x00007ffff7fcb240  _dl_signal_error
0x00007ffff7fcb460  _dl_catch_exception
...
--Type <RET> for more, q to quit, c to continue without paging--
```

### Procedure Lookup Table plt functions
```
(gdb) info functions plt
All functions matching regular expression "plt":

Non-debugging symbols:
0x0000000000401070  setvbuf@plt
0x0000000000401080  puts@plt
0x0000000000401090  __stack_chk_fail@plt
0x00000000004010a0  printf@plt
0x00000000004010b0  fgets@plt
```

#### [Memory Region Attributes](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Memory-Region-Attributes.html#Memory-Region-Attributes)

## Signals

### [Signals](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Signals.html#Signals)

### C Source Blocked Signals
#### [Difference between a process signal mask, blocked signal set, and a blocked signal](https://stackoverflow.com/questions/48409070/difference-between-a-process-signal-mask-blocked-signal-set-and-a-blocked-sign)

## Registers

#### [Registers](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Registers.html#Registers)

```
info registers

info all-registers

info registers reggroup

info registers regname
```
[$pc versus $rip](https://stackoverflow.com/questions/61133451/where-to-view-the-program-counter-pc-and-instruction-register-ir-in-gdb)
#### [Assembly Registers](./Assembly-Registers.md)

## Stack

#### [Stack](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Stack.html#Stack)

## Variables

#### [Variables](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Variables.html#Variables)

## Breakpoints

#### [Breakpoints](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Breakpoints.html#Breakpoints)

## Tracepoints

#### [Tracepoints](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Tracepoints.html#Tracepoints)

# [Old | GDB - Manual Table of Contents](https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_toc.html)

