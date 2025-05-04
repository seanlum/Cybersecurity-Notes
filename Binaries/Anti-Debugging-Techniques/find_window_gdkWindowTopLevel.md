# Anti-Debugger Detect Windows: gdkWindowTopLevel

https://github.com/cuckoosandbox/community/blob/master/modules/signatures/windows/antidbg_windows.py
```
return FindWindowA('gdkWindowToplevel', 0) != 0;
```