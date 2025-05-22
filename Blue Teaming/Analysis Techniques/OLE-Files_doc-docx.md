# OLE Files

The Didier Stevens suite comes with oledump.py which is a way to get file streams out of a .DOC file or a file which uses the OLE file format.

### First, examine the file
```
python oledump.py <filename>
```

### Then, extract a file
```
# -v will print as ascii
# without -v will be hexdump
python oledump.py <filename> -s <stream_number_int> [-v]
```