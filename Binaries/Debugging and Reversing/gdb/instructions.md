# GNU Debugger

## Inspecting Variables

```as
x/s <address>
// displays string

x/s <address>+<offset>
// displays part of string until '\0' is encountered

x/c <address>
// displays first character of address

x/c <address>+<offset>
// displays character at address plus offset
```