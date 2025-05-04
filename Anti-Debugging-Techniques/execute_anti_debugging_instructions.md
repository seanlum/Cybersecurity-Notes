# Check if NtGlobalFlags are enabled

## Links
https://unprotect.it/technique/ntglobalflag/

https://mandiant.github.io/capa/rules/execute%20anti-debugging%20instructions/

## Explanation
```
FLG_HEAP_ENABLE_TAIL_CHECK (0x10)
FLG_HEAP_ENABLE_FREE_CHECK (0x20)
FLG_HEAP_VALIDATE_PARAMETERS (0x40)

112 = 0x7
112 = 0x4 | 0x2 | 0x1
```
## Example Code
```c
BOOL if_debug_flags_enabled()
{
  return NtCurrentPeb()->NtGlobalFlag == 112;
}
```
## YARA
```
rule DebuggerCheck__GlobalFlags  {
    meta:
	description = "Rule to detect NtGlobalFlags debugger check"
        author = "Thibault Seret"
        date = "2020-09-26"
    strings:
        $s1 = "NtGlobalFlags"
    condition:
        any of them
}
```