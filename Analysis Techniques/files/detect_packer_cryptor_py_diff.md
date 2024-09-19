```diff
diff --git a/detect_packer_cryptor.py b/detect_packer_cryptor.py
index 898d5bf..eb1d114 100644
--- a/detect_packer_cryptor.py
+++ b/detect_packer_cryptor.py
@@ -1,20 +1,25 @@
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
+packer_path = rules_path + 'packer.yar'
+crypto_path = rules_path + 'crypto_signatures.yar'
 
 #Now we will try to find out if yara rules match with the exe
+
 #file, if so that means that yara has detected a packer or a cryptor
 #first we try to detect cryptors
-
+             
 try:
   #the function match will return the list of detected cryptors
   matches = crypto_rules.match(exe_file_path)
@@ -28,10 +33,36 @@ except:
 #detect packers
 
 try:
-  matches = packer_rules.match(exe_file_path)
+  matches = packer_rules.match(packer_path)
   if matches:
     print('packers detected')
     print(matches)
 except:
   print('packer exception, you must read yara docs')
-  
\ No newline at end of file
+  
+#first, let's define the list of packers/cryptors we want to detect
+packers = ['AHTeam', 'Armadillo', 'Stelth', 'yodas', 'ASProtect', 'ACProtect', 'PEnguinCrypt', 
+ 'UPX', 'Safeguard', 'VMProtect', 'Vprotect', 'WinLicense', 'Themida', 'WinZip', 'WWPACK',
+ 'Y0da', 'Pepack', 'Upack', 'TSULoader'
+ 'SVKP', 'Simple', 'StarForce', 'SeauSFX', 'RPCrypt', 'Ramnit', 
+ 'RLPack', 'ProCrypt', 'Petite', 'PEShield', 'Perplex',
+ 'PELock', 'PECompact', 'PEBundle', 'RLPack', 'NsPack', 'Neolite', 
+ 'Mpress', 'MEW', 'MaskPE', 'ImpRec', 'kkrunchy', 'Gentee', 'FSG', 'Epack', 
+ 'DAStub', 'Crunch', 'CCG', 'Boomerang', 'ASPAck', 'Obsidium','Ciphator',
+ 'Phoenix', 'Thoreador', 'QinYingShieldLicense', 'Stones', 'CrypKey', 'VPacker',
+ 'Turbo', 'codeCrypter', 'Trap', 'beria', 'YZPack', 'crypt', 'crypt', 'pack',
+ 'protect', 'tect'
+]
+
+#next, we will try to match peid rules with an exe file
+try:
+  matches = peid_rules.match(crypto_path)
+  if matches:
+    for match in matches:
+      for packer in packers:
+        #this line is simply trying to see if one of the known packers has been detected
+        if packer.lower() in match.lower():
+          print('packer detected')
+          print(packer)
+except:
+  print('error')
\ No newline at end of file
```