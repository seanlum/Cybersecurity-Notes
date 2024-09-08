# Recovering files from a DD image

[Mounting a DD file](./Mounting-a-DD-file.md)

# Listing partitions in a DD image
```
─$ sudo apt install sleuthkit

─$ mmls recoverfiles.dd 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000020479   0000018432   Linux (0x83)

```
# List files within a partition
```
└─$ sudo fls -f ext4 -r -o 2048 recoverfiles.dd
d/d 11: lost+found
r/r * 12:       Vanilla.gif
r/r * 13:       SBTCertifications.mp4
r/r * 14:       Flag3.pdf
r/r * 15:       Flag2.docx
r/r * 16:       Flag1.png
V/V 2305:       $OrphanFiles

```

# Recovering photos from a partition 
```
sudo photorec <file.dd>
# Select partition
# Select output folder
# Export files
```