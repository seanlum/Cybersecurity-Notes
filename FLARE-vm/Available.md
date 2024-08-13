# 7z-build-nsis

7-zip build script with nsis script decompiling using ms visual studio

This build can unpack nsis script, eg. [NSIS].nsi or [LICENSE].txt from nsis installer. This feature is disable in official versions since 15.05, after which official versions are only able to unpack files from installer.

Notice: Only executables depending on 7z.dll can unpack nsis packages, 7zcl, 7za, 7zr would not unpack nsis package, like official ones.

https://github.com/myfreeer/7z-build-nsis