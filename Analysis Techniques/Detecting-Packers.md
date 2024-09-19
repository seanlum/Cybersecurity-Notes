# Install Yara
https://yara.readthedocs.io/en/latest/gettingstarted.html
```
wget https://github.com/VirusTotal/yara/archive/refs/tags/v4.5.2.tar.gz
```
```
tar -xvf v4.5.2.tar.gz
cd v4.5.2
```
### Install build dependencies
#### Note on libjansson-dev
https://jansson.readthedocs.io/en/1.1/gettingstarted.html
```
sudo apt-get install automake libtool make gcc pkg-config
sudo apt-get install flex bison
sudo apt-get install libssl-dev libjansson-dev libmagic-dev
```
```
./bootstrap.sh
./configure --enable-cuckoo --enable-magic --enable-dotnet
make
sudo make install
```
```
yara
```

# Scan using YaraCollector

This will eventually be updated to include the updates from YaraCollector
#### Install Yara-Python library
```bash
pip install python-yara
```
### Get YaraCollector
```
$ git clone https://github.com/seanlum/YaraCollector.git
```
### Download rules
```bash
mkdir rules
cd rules
wget https://raw.githubusercontent.com/Yara-Rules/rules/master/packers/peid.yar
wget https://raw.githubusercontent.com/Yara-Rules/rules/master/packers/packer.yar
wget https://raw.githubusercontent.com/Yara-Rules/rules/master/crypto/crypto_signatures.yar
cd ..
```
### Generate rules list
```
find rules --type f >> ruleslist.txt
```
```
python3 YaraCollector/scan-files.py --rules-list ruleslist.txt --scan-directory rules >> log.txt
```
### [log output](./files/log.txt)

# Detect malwarea packers and cryptors with Python (Yara and PEFile)

https://isleem.medium.com/detect-malware-packers-and-cryptors-with-python-yara-pefile-65bf3c15be78



### Install dependencies
#### Install PEFile Python library
```bash
pip install pefile
```
#### Install Yara-Python library
```bash
pip install python-yara
```

### Install detection rules
#### Yara-Rules packers rules
```bash
wget https://raw.githubusercontent.com/Yara-Rules/rules/master/packers/peid.yar
wget https://raw.githubusercontent.com/Yara-Rules/rules/master/packers/packer.yar
wget https://raw.githubusercontent.com/Yara-Rules/rules/master/crypto/crypto_signatures.yar
```
### Script for detetecting rules
```
wget https://gist.githubusercontent.com/islem-esi/cef15f99db844fe1cfe596656dfe9bb2/raw/e0cb55a3604ddc1376a7aca5b40fba2949929920/detect_packer_cryptor.py
```

### Edit the rules path

```diff
diff --git a/detect_packer_cryptor.py b/detect_packer_cryptor.py
index 898d5bf..69bbbd1 100644
--- a/detect_packer_cryptor.py
+++ b/detect_packer_cryptor.py
@@ -1,17 +1,20 @@
 import yara
+import os

 #Path to the folder containing downloaded files in the first part
-rules_path = 'path/to/the/folder/containing/downloaded/rules'
+# rules_path = 'path/to/the/folder/containing/downloaded/rules'
+rules_path = os.path.abspath('./') + os.path.sep

 #Read files
 peid_rules = yara.compile(rules_path + 'peid.yar')
 packer_rules = yara.compile(rules_path + 'packer.yar')
-crypto_rules = yara.compile(rules_path + 'crypto.yar')
+crypto_rules = yara.compile(rules_path + 'crypto_signatures.yar')

 #Path to the exe file you want to analyze
-exe_file_path = 'path/to/exe/file'
+exe_file_path = rules_path + 'peid.yar'
```

### Execute the script
```
$ python3 detect_packer_cryptor.py
packers detected
[Borland]
```