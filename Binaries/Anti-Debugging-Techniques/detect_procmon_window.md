# Detect WindowClassName
```
PROCMON_WINDOW_NAME = PROCMONPHJGNP^GO@TR
```
```c
BOOL is_procmon_running()
{
  CHAR ClassName[24]; // [esp+8h] [ebp-18h] BYREF

  qmemcpy(ClassName, &PROCMON_WINDOW_NAME, 0x16u);
  decrypt_string_001(ClassName);
  return FindWindowA(ClassName, 0) != 0;
}
```