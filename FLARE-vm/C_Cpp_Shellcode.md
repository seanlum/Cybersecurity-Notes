# blobrunner
BlobRunner is a simple tool to quickly debug shellcode extracted during malware analysis.

BlobRunner allocates memory for the target file and jumps to the base (or offset) of the allocated memory. This allows an analyst to quickly debug into extracted artifacts with minimal overhead and effort.

https://github.com/OALabs/BlobRunner