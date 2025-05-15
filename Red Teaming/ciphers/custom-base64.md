# Custom Base64 Cipher
```py
import string
import base64
s = ""
custom = "9ZABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyz012345678+/"
Base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
ciphertext = 'TEgobxZobxZgGFPkb2O='
for ch in ciphertext:
if (ch in Base64):
s = s + Base64[string.find(custom,str(ch))]
elif (ch == '='):
s += '='
result = base64.decodestring(s)
```