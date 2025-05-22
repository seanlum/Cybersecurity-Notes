# Base16, Base34, and Base64

https://en.wikipedia.org/wiki/Character_encoding

https://datatracker.ietf.org/doc/html/rfc4648

### Python base64

https://docs.python.org/3/library/base64.html

```python
import base64
encoded = base64.b64encode(b'data to be encoded')
encoded
b'ZGF0YSB0byBiZSBlbmNvZGVk'
data = base64.b64decode(encoded)
data
b'data to be encoded'
```

# Hexadecimal Character Encoding

https://en.wikipedia.org/wiki/Hexadecimal

### HxD Hex Editor and Disk Editor 

https://mh-nexus.de/en/hxd/

# PEM, DER, CRT, and CER: X.509 Encodings and Conversions
https://www.ssl.com/guide/pem-der-crt-and-cer-x-509-encodings-and-conversions/

https://en.wikipedia.org/wiki/X.509

https://unix.stackexchange.com/questions/492704/what-encoding-is-used-for-the-keys-when-using-ssh-keygen-t-rsa

```
For ssh keys please check below from dave_thompson_085 comments:

Note ssh-keygen uses (several) PEM formats but never the one(s) in 7468. In the past for RSA it defaulted to OpenSSL's two 'traditional' (aka 'legacy') formats, either unencrypted whcih is 7468-like except containing PKCS1, or password-encrypted which is1421-like with Proc-type and DEK-Info and base64 of encrypted PKCS1, but not 7468-like. Since 7.8 it defaults to OpenSSH's own 'new format' (previously invoked by option -o) which is 7468-like but the contents are entirely different (XDR-style not ASN.1). There are numerous Qs about these already on several Stacks.

OpenSSH public key formats are never PEM (although commercial 'SSH2' sort-of are), just base64 of SSH wire format. And I was recently reminded this Q/A covers the private key formats quite thoroughly
```

# Octal Character Encoding

### SSH Protocol Architecuture

https://www.rfc-editor.org/rfc/rfc4251#section-5

# MIME Formats

https://en.wikipedia.org/wiki/MIME

### EBCDIC 

https://en.wikipedia.org/wiki/EBCDIC

Extended Binary Coded Decimal Interchange Code[1][2] (EBCDIC;[1] /ˈɛbsɪdɪk/) is an eight-bit character encoding used mainly on IBM mainframe and IBM midrange computer operating systems.

# URL Encoding 

### urlencode()

https://www.w3schools.com/tags/ref_urlencode.ASP

https://www.php.net/manual/en/function.urlencode.php

### encodeURI()

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI

### decodeURIComponent()

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent

### decodeURI()

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI

# Character Sets

### Unicode Character Encoding

https://home.unicode.org/

### UTF-8, UTF-16, UTF-32 & BOM

https://unicode.org/faq/utf_bom.html

### ANSI character set

https://en.wikipedia.org/wiki/ANSI_character_set

### ANSEL 

https://en.wikipedia.org/wiki/ANSEL

ANSEL, the American National Standard for Extended Latin Alphabet Coded Character Set for Bibliographic Use, was a character set used in text encoding. It provided a table of coded values for the representation of characters of the extended Latin alphabet in machine-readable form for thirty-five languages written in the Latin alphabet and for fifty-one romanized languages. ANSEL adds 63 graphic characters to ASCII,[1] including 29 combining diacritic characters.

### ASCII

https://en.wikipedia.org/wiki/ASCII

