# Debugging in Visual Studio Code
Visual Studio Code or VSCode actually supports a variety of debugger modes. Some of the default inclusions are `gdb` and `lldb` which are very common.

## Debugging manual for Visual Studio Code
https://code.visualstudio.com/docs/debugtest/debugging

## Debugging Configurations
https://code.visualstudio.com/docs/debugtest/debugging-configuration

### Writing a Configuration File
- Create an initial file in the `.vscode` directory called `launch.json`
    - By default, VSCode uses JSON files for configuration.
- Debuggers supported: 
    - Edge
    - Node.js
    - Python
    - C/C++

# Sample C/C++ Cross-Platform Debugging Configuration
```json
{
  "version": "0.2.0",
  "configurations": [
    {
        "name": "(gdb) (Windows) Launch",
        "type": "cppdbg",
        "request": "launch",
        "program": "${workspaceFolder}/main.exe",
        "args": [ ],
        "stopAtEntry": true,
        "cwd": "${workspaceFolder}",
        "environment": [],
        "externalConsole": false,
        "MIMode": "gdb",
        "miDebuggerPath": "C:/msys64/usr/bin/gdb.exe",
        "setupCommands": [
            {
                "description": "Enable pretty-printing for gdb",
                "text": "-enable-pretty-printing",
                "ignoreFailures": true
            },
            {
                "description": "Set Disassembly Flavor to Intel",
                "text": "-gdb-set disassembly-flavor intel",
                "ignoreFailures": true
            }
        ]
    },
    {
        "name": "(gdb) (Linux) Launch",
        "type": "cppdbg",
        "request": "launch",
        "program": "${workspaceFolder}/main",
        "args": [ ],
        "stopAtEntry": true,
        "cwd": "${workspaceFolder}",
        "environment": [],
        "externalConsole": false,
        "MIMode": "gdb",
        "miDebuggerPath": "/usr/bin/gdb",
        "setupCommands": [
            {
                "description": "Enable pretty-printing for gdb",
                "text": "-enable-pretty-printing",
                "ignoreFailures": true
            },
            {
                "description": "Set Disassembly Flavor to Intel",
                "text": "-gdb-set disassembly-flavor intel",
                "ignoreFailures": true
            }
        ]
    },
    {
        "name": "(lldb) (macOS) Launch",
        "type": "cppdbg",
        "request": "launch",
        "program": "${workspaceFolder}/main",
        "args": [ ],
        "stopAtEntry": true,
        "cwd": "${workspaceFolder}",
        "environment": [],
        "externalConsole": false,
        "MIMode": "lldb",
        "miDebuggerPath": "/usr/bin/lldb",
        "setupCommands": [
        ]
    }
  ]
}
```

## Sample Configuration for Node.js

```json
{
  "name": "launch program that reads a file from stdin",
  "type": "node",
  "request": "launch",
  "program": "program.js",
  "console": "integratedTerminal",
  "args": ["<", "in.txt"]
}
```