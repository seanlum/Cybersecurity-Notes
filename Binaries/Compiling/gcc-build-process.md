# GCC Build Process

## Source Code
#### [main.c](./gcc-build-scripts/main.c)

First the source code must be written
```c
#include <stdio.h>

#define FORMAT_STRING "%s"
#define MESSAGE       "Hello, world!"

int
main(int argc, char *argv[]) {
    printf(FORMAT_STRING, MESSAGE);
    return 0;
}
```

## Preprocessing
#### [main-preprocessor.c](./gcc-build-scripts/main-preprocessor.c)
Then the headers must be loaded into the source file. All `#defines` and `#includes` must be built into the file
```
gcc -E -P main.c > main-preprocessor.c
```

## Compilation
#### [main-preprocessor.s](./gcc-build-scripts/main-preprocessor.s)
```
gcc -S -masm=intel main-preprocessor.c
```

## Creating the Object File
#### [main-preprocessor.s](./gcc-build-scripts/main-preprocessor.s)
#### [main-object-disassemble.txt](./gcc-build-scripts/main-object-disassemble.txt)
#### [main-object-ida-dump.txt](./gcc-build-scripts/main-object-ida-dump.txt)
```
gcc -c main-preprocessor.s -o main.o
```

## Linking the Object File
#### [main-ida-dump.txt](./gcc-build-scripts/main-ida-dump.txt)
#### [main-disassemble.txt](./gcc-build-scripts/main-disassemble.txt)
```
gcc main.o -o main
```
