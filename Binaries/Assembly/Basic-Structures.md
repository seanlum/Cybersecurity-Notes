# Basic Assembly Structures

### Function with a Return
```c
int f()
{
    return 20;
}
```
```asm
f:
    mov     eax, 123
    ret
```

### Hello, world!

```c

#include <stdio.h>

int main()
{
    printf("hello, world!\n");
    return 0;
}
```
```
> cl hello_world.cpp /Fa1.asm
```

```as
CONST SEGMENT 
$SG3830 DB 'hello, world', 0AH, 00H
CONST ENDS
PUBLIC _main
EXTRN  _printf:PROC
_TEXT  SEGMENT
_main  PROC
    push    ebp
    mov     ebp, esp
    push    OFFSET $SG3830
    call    _printf
    add     exp, 4
    xor     eax, eax
    pop     ebp
    ret     0
_main ENDP
_TEXT ENDS
```