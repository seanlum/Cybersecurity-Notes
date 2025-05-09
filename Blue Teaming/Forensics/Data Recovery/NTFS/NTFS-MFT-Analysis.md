# $MFT Files

## What is an $MFT file
An $MFT is known as a Master File Table. These files belong to NTFS file partitions and can be used for recovery.

## Listing Files within an $MFT File
- `MFTECmd` by Eric Zimmerman can be used to extract information about MFT files, and the information may be placed within JSON, CSV, or body  files.
- `Timeline Explorer` by Eric Zimmerman can be used to view information which  was exported by MFTECmd
- Hex editors may also be used to view individual files which were stored in the $MFT file. 
- `SleuthKit` can also be used to get information about MFT files.
    - `istat` can get information about files within disk images
    - `ffind` can be used to find directories by entry number
    - `ifind` can be used to find files by directory number

## Getting Information About Files in $MFT files.
```
> MFTECmd.exe -f <path\to\$MFT_file> --csv <path\to\csv_file>
```

## Open the file CSV with `Timeline Viewer`
```
Open Timeline Viewer
Open File...
Browse for File...

Go to row
Get file Entry number
OFFSET = hex((Entry_number) * (sector_size))
```

## Viewing the File Entry Data
```
Open the $MFT file with 010 Editor
<CTRL+G> then enter <OFFSET>
```