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

### Edit the file
- edit the include paths
- add the second scanner portion
- 
### [The diff of the file](./files/detect_packer_cryptor_py_diff.md)

### Execute the script
```
$ python3 ./detect_packer_cryptor.py
packers detected
[emotet_packer, silent_banker, zbot, Borland, rpx_1_xx, dotfuscator, AutoIt_2]
```

### Detecting with PEFile
```
wget https://gist.githubusercontent.com/islem-esi/334d223b3088e0bec5adc75f010c83c2/raw/f95fdbfece61ab42900c7d7f8b62e4264e5fabc1/detect_with_pefile.py
```
```python
#don't forget this
import pefile

#first, let's get the list of sections names used by packers/cryptors
packers_sections = {
        #The packer/protector/tools section names/keywords
        '.aspack': 'Aspack packer',
        '.adata': 'Aspack packer/Armadillo packer',
        'ASPack': 'Aspack packer',
        '.ASPack': 'ASPAck Protector',
        '.boom': 'The Boomerang List Builder (config+exe xored with a single byte key 0x77)',
        '.ccg': 'CCG Packer (Chinese Packer)',
        '.charmve': 'Added by the PIN tool',
        'BitArts': 'Crunch 2.0 Packer',
        'DAStub': 'DAStub Dragon Armor protector',
        '!EPack': 'Epack packer',
        'FSG!': 'FSG packer (not a section name, but a good identifier)',
        '.gentee': 'Gentee installer',
        'kkrunchy': 'kkrunchy Packer',
        '.mackt': 'ImpRec-created section',
        '.MaskPE': 'MaskPE Packer',
        'MEW': 'MEW packer',
        '.MPRESS1': 'Mpress Packer',
        '.MPRESS2': 'Mpress Packer',
        '.neolite': 'Neolite Packer',
        '.neolit': 'Neolite Packer',
        '.nsp1': 'NsPack packer',
        '.nsp0': 'NsPack packer',
        '.nsp2': 'NsPack packer',
        'nsp1': 'NsPack packer',
        'nsp0': 'NsPack packer',
        'nsp2': 'NsPack packer',
        '.packed': 'RLPack Packer (first section)',
        'pebundle': 'PEBundle Packer',
        'PEBundle': 'PEBundle Packer',
        'PEC2TO': 'PECompact packer',
        'PECompact2': 'PECompact packer (not a section name, but a good identifier)',
        'PEC2': 'PECompact packer',
        'pec1': 'PECompact packer',
        'pec2': 'PECompact packer',
        'PEC2MO': 'PECompact packer',
        'PELOCKnt': 'PELock Protector',
        '.perplex': 'Perplex PE-Protector',
        'PESHiELD': 'PEShield Packer',
        '.petite': 'Petite Packer',
        'petite': 'Petite Packer',
        '.pinclie': 'Added by the PIN tool',
        'ProCrypt': 'ProCrypt Packer',
        '.RLPack': 'RLPack Packer (second section)',
        '.rmnet': 'Ramnit virus marker',
        'RCryptor': 'RPCrypt Packer',
        '.RPCrypt': 'RPCrypt Packer',
        '.seau': 'SeauSFX Packer',
        '.sforce3': 'StarForce Protection',
        '.spack': 'Simple Pack (by bagie)',
        '.svkp': 'SVKP packer',
        'Themida': 'Themida Packer',
        '.Themida': 'Themida Packer',
        'Themida ': 'Themida Packer',
        '.taz': 'Some version os PESpin',
        '.tsuarch': 'TSULoader',
        '.tsustub': 'TSULoader',
        '.packed': 'Unknown Packer',
        'PEPACK!!': 'Pepack',
        '.Upack': 'Upack packer',
        '.ByDwing': 'Upack Packer',
        'UPX0': 'UPX packer',
        'UPX1': 'UPX packer',
        'UPX2': 'UPX packer',
        'UPX!': 'UPX packer',
        '.UPX0': 'UPX Packer',
        '.UPX1': 'UPX Packer',
        '.UPX2': 'UPX Packer',
        '.vmp0': 'VMProtect packer',
        '.vmp1': 'VMProtect packer',
        '.vmp2': 'VMProtect packer',
        'VProtect': 'Vprotect Packer',
        '.winapi': 'Added by API Override tool',
        'WinLicen': 'WinLicense (Themida) Protector',
        '_winzip_': 'WinZip Self-Extractor',
        '.WWPACK': 'WWPACK Packer',
        '.yP': 'Y0da Protector',
        '.y0da': 'Y0da Protector',
    }

#lower case the names to make it easier for search
packers_sections_lower =  {x.lower(): x for x in packers_sections.keys()}

#the following function takes the names of sections of an exe file as an argument and
#tries to match them with the names associated to packers
def detect_packing(sections_of_pe):
    return [packers_sections_lower[x.lower()] for x in sections_of_pe if x.lower() in packers_sections_lower.keys()]

#finally let's parse the exe file with pefile and get sections names
try:
  #parse the files
    exe = pefile.PE(exe_file_path, fast_load=True)
    matches = detect_packing([
        section.Name.decode(errors='replace',).rstrip('\x00') for section in exe.sections
    ])
    if matches:
        print('packers matched')
        print(matches)
except:
    print('manuel exception')
```