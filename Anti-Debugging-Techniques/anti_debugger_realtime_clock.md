## Checking the Realtime Clock For A Debugger
```c
BOOL anti_debugger_check_realtime_clock()
{
  unsigned __int64 v0; // rax
  int v1; // ebx
  unsigned __int64 v2; // rax

  do
  {
    v0 = __rdtsc();
    v1 = v0;
    v2 = __rdtsc();
  }
  while ( (_DWORD)v2 - v1 == 1 );
  return (unsigned int)(v2 - v1) >= 0x200;
}
```