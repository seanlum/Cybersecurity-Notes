# Analyzing False Positives

For example, a repository like DependencyChecker from OWASP contains a file called evil.zip which uses the documented Zip-Slip vulnerability to place a folder within temp, but the test file expects the extracted folder to be within /tmp. Now this may behave differently on different OSes as well. But lets break it down.

## Cloning the repository

```
PS C:\Users\seanj> cd D:\Code
PS D:\Code> git clone https://github.com/jeremylong/DependencyCheck.git
Cloning into 'DependencyCheck'...
remote: Enumerating objects: 228122, done.
remote: Counting objects: 100% (6774/6774), done.
remote: Compressing objects: 100% (1669/1669), done.
remote: Total 228122 (delta 4884), reused 6573 (delta 4742), pack-reused 221348 (from 1)
Receiving objects: 100% (228122/228122), 274.15 MiB | 27.72 MiB/s, done.
Resolving deltas: 100% (163507/163507), done.
Updating files: 100% (1342/1342), done.
PS D:\Code> wsl
```
## Inspecting the directory with `WinDirStat`

- Open WinDirStat
- Select the folder you want to scan
- Scan the folder
- Go through the file tree and view information about files.
- Note that `evil.zip` is in `DependencyChecker\core\src\test\resources\`

![](./files/WinDirStat-evil-zip.png)

## Noting the suspicious filename
```
seanlum@Mitobox:/mnt/d/Code/DependencyCheck$ find . -name evil.zip
./core/src/test/resources/evil.zip
```
## Testing evil.zip

![](./files/Zip-Slip-exploit-screenshot.png)

## Oh no, what is BehavesLike.ZipSlip.xz

https://security.snyk.io/research/zip-slip-vulnerability

### [13 Second Clip showing what Zip-Slip does](https://youtube.com/clip/UgkxQLMmzpNBVOCParJHthk5FX6cV_PU1Tvz?si=mZUhRInmm_OzNVXB)

### [Code that can prepare a zip-slip](https://github.com/ptoomey3/evilarc/blob/master/evilarc.py)

## Analyzing evil.zip with `unzip -l`

```sh
seanlum@Mitobox:/mnt/d/Code/DependencyCheck/core/src/test/resources$ unzip -l evil.zip
Archive:  evil.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
       20  2018-04-15 22:04   ../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../tmp/evil.txt
---------                     -------
       20                     1 file
```
## Extracting the payload with `unzip -d`
```
seanlum@Mitobox:$ unzip evil.zip '../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../tmp/evil.txt' -d ~/evil.txt
Archive:  evil.zip
warning:  skipped "../" path component(s) in ../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../tmp/evil.txt
 extracting: /home/seanlum/evil.txt/tmp/evil.txt
```

## Examining the extraction folder with `tree`
```
seanlum@Mitobox:$ ls ~/evil.txt
tmp
seanlum@Mitobox:$ tree ~/evil.txt/
/home/seanlum/evil.txt/
└── tmp
    └── evil.txt

1 directory, 1 file
```
## Determining File Type with `file`
```
seanlum@Mitobox:$ file ~/evil.txt/tmp/evil.txt
/home/seanlum/evil.txt/tmp/evil.txt: ASCII text
```
## Examining the contents of the payload with `cat`
```
seanlum@Mitobox:$ cat ~/evil.txt/tmp/evil.txt
this is an evil one
```
## Code that executes `evil.zip`

After checking some code about where commits came from in the repository, I found this Git commit on the repository

### https://github.com/jeremylong/DependencyCheck/commit/cfa994ddc46d333366054a0c41c5d99ae5e0d64f

```diff
@@ -0,0 +1,65 @@
/*
 * This file is part of dependency-check-core.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Copyright (c) 2018 Jeremy Long. All Rights Reserved.
 */
package org.owasp.dependencycheck.utils;
import java.io.File;
import java.io.FilenameFilter;
import org.apache.commons.io.filefilter.NameFileFilter;
import org.junit.Test;
import org.owasp.dependencycheck.BaseTest;
import org.owasp.dependencycheck.Engine;
/**
 *
 * @author Jeremy Long
 */
public class ExtractionUtilTest extends BaseTest {
    /**
     * Test of extractFiles method, of class ExtractionUtil.
     */
    @Test(expected = org.owasp.dependencycheck.utils.ExtractionException.class)
    public void testExtractFiles_File_File() throws Exception {
        File destination = getSettings().getTempDirectory();
        File archive = BaseTest.getResourceAsFile(this, "evil.zip");
        ExtractionUtil.extractFiles(archive, destination);
    }
    /**
     * Test of extractFiles method, of class ExtractionUtil.
     */
    @Test(expected = org.owasp.dependencycheck.utils.ExtractionException.class)
    public void testExtractFiles_3args() throws Exception {
        File destination = getSettings().getTempDirectory();
        File archive = BaseTest.getResourceAsFile(this, "evil.zip");
        Engine engine = null;
        ExtractionUtil.extractFiles(archive, destination, engine);
    }
    /**
     * Test of extractFilesUsingFilter method, of class ExtractionUtil.
     */
    @Test(expected = org.owasp.dependencycheck.utils.ExtractionException.class)
    public void testExtractFilesUsingFilter() throws Exception {
        File destination = getSettings().getTempDirectory();
        File archive = BaseTest.getResourceAsFile(this, "evil.zip");
        ExtractionUtil.extractFiles(archive, destination);
        FilenameFilter filter = new NameFileFilter("evil.txt");
        ExtractionUtil.extractFilesUsingFilter(archive, destination, filter);
    }
}
```
## What does this mean?

Well, this test is meant to run on Linux, and the code will extract to `/tmp` and we can see that the test case is checking for `getSettings().getTempDirectory()` which will evaluate to `/tmp` on most Linux distributions.

### Possible Bugs

If the evil.zip file does not have code to work on Microsoft Windows

![](./files/7zip-evil-zip-slip-no-work-on-windows.png)

As we can see, in Windows, even in 7zip, there is no code to execute differently on Windows. This test will only work on systems where the temporary directory is in the path `/tmp`, on any other system the test will fail.

## Security Implications

### Linux
#### if `/tmp` exists, the test will pass
#### `/tmp` should be cleared of `evil.txt`

### Windows

On Windows, the files don't extract anywhere.

## Actual payload of the file
```
this is an evil one
```

# The test result is a false positive
Considering the payload just delivers a .txt file within an expected directory, this could be viewed as a false positive. However, if you don't want exploits running in your system, that's a file traversal issue. Some antivirus on Linux may flag this.