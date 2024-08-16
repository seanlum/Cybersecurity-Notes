# Hashing

Often entire files, or segments of files, shellcode, and various other bits of data can be analyzed with a hashing program to produce a fingerprint which may later be used to identify a segment or complete object of data/code.

Files and memory may be hashed, resulting in IoC or some form of cryptographic identity. There are checksum algorithms, hashing algorithms, and hashing programs which can be used. YARA uses cryptographic hashes to identify many IoC, for example.

There are quite a few hashing algorithms, but most of todays algorithms primarily involve:

### Note
```
08-16-2024 - @seanlum - encrypting IoC with salt or making a SSL HMAC message digests can result in unique hashes which may only be useful to people who have access to the PKI certificates or the salt which was used to generate the unique hash. This may be useful for internal IoC management, this way internal threat intelligence may be shared among a trust without the hashes being used by a foreign actor with direct relation of content. [HMAC uses a random key](https://github.com/dotnet/runtime/blob/5535e31a712343a63f5d7d796cd874e563e5ac14/src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/HMACSHA256.cs#L35C9-L47C10)

=================================================================================================
08-16-2024 - @seanlum - Idea... UDP streams can be broadcasted in segments, but can be hashed in order when the frames arrive, same with TCP segments. This means that it is memory, and in a stream, streams are digestable in segments

Theory. Network Socket -> Readable Stream -> Buffered Stream -> Data Stream -> Digest Input Stream -> hash. For stream in segment of sequence 1 through N, update digest for stream segment; complete on download completion. You could even identify the stream per MTU segment.

If I were to try a PoC, I might attempt to do it with Java because the networking infrastructure is already well defined.

Link Notes for network streaming:
https://github.com/wireshark/wireshark

https://stackoverflow.com/questions/26152931/how-could-i-sniff-network-traffic-in-java

https://docs.oracle.com/javase/tutorial/networking/sockets/readingWriting.html
https://docs.oracle.com/javase/8/docs/api/java/io/BufferedInputStream.html
https://docs.oracle.com/javase/8/docs/api/java/io/InputStreamReader.html
https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html
https://docs.oracle.com/javase/8/docs/api/java/io/DataInputStream.html
https://docs.oracle.com/javase/8/docs/api/java/security/DigestInputStream.html
https://docs.oracle.com/javase%2F8%2Fdocs%2Fapi%2F%2F/java/net/DatagramSocket.html
https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/io/InputStream.html
https://docs.oracle.com/javase/8/docs/api/java/security/MessageDigest.html

```

## Tools for Hashing
### Linux
- [md5sum - coreutils](https://linux.die.net/man/1/md5sum)
- [sha256sum - coreutils](https://linux.die.net/man/1/sha256sum)
- [SHA2 Utilities - coreutils](https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html)
### Windows
- [Get-FileHash - PowerShell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.2)
- [Certutil Verify MD5, SHA256 Checksum Windows 11](https://www.windowsdigitals.com/verify-md5-sha256-checksum-windows-11/)
- [certutil -hashfile](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil#-hashfile)

```PowerShell
# Example of MD5
> Get-FileHash c:\example.txt -Algorithm MD5
```

## Python
https://docs.python.org/3/library/hashlib.html

- [Hashlib Usage](https://docs.python.org/3/library/hashlib.html#usage)
- [Base64 -- base64 — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)

## JavaScript Node JS

### https://www.npmjs.com/package/node-forge

- [SHA1 Digest in Node Forge](https://www.npmjs.com/package/node-forge#sha1)
- [SHA256 Digest in Node Forge on NPMjs.com](https://www.npmjs.com/package/node-forge#sha256)
- [MD5 in Node Forge](https://www.npmjs.com/package/node-forge#md5)

### Node JS Crypto https://nodejs.org/api/crypto.html
- [createHmac](https://nodejs.org/api/crypto.html#cryptocreatehmacalgorithm-key-options)
- [createHash - sha256 example](https://nodejs.org/api/crypto.html#cryptocreatehashalgorithm-options)


## .NET 8.0
- [.NET Cryptographic Security](https://learn.microsoft.com/en-us/dotnet/standard/security/cryptographic-services)
- [System.Security.Cryptography Namespace](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography?view=net-8.0)
- [MD5 Class](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.md5?view=net-8.0)
- [SHA256 Class](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.sha256?view=net-8.0)

## Java Cryptography Architecture (JCA)
https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html

- [Computing a MessageDigest Object](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#MDEx)
- [HMAC-SHA256 Example](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#HmacEx)

## PHP Hashing 

- [PHP Hash Lib](https://www.php.net/manual/en/function.hash.php)
- [Hashing a File](https://www.php.net/manual/en/function.hash-file.php)
- [HMAC SHA256 of a File](https://www.php.net/manual/en/function.hash-hmac-file.php)
- [PHP Hash Algols](https://www.php.net/manual/en/function.hash-algos.php)

## C

### [OpenSSL Sha256.c](https://github.com/openssl/openssl/blob/master/crypto/sha/sha256.c)

## Rust 

https://docs.rs/sha2/latest/sha2/

## Ruby 

https://ruby-doc.org/stdlib-2.4.0/libdoc/digest/rdoc/Digest/SHA2.html

## MD5 

### https://md5deep.sourceforge.net/

md5deep is a set of programs to compute MD5, SHA-1, SHA-256, Tiger, or Whirlpool message digests on an arbitrary number of files

## Digest Hashing
- [MD5](https://www.ietf.org/rfc/rfc1321.txt) (dated cryptographic standard)
- [SHA1](https://www.ietf.org/rfc/rfc3174.txt) (dated cryptographic standard)
- [SHA2 or SHA256](https://csrc.nist.gov/files/pubs/fips/180-2/final/docs/fips180-2.pdf)
- [SHA3](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
- [SHA512, Windows](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.sha512?view=net-8.0)
- [SHA512, Linux](https://github.com/coreutils/coreutils/blob/9e60f2db903b17c1a31e24b89bda90a12446459d/src/digest.c#L969)
 
- [FIPS 180-4 Secure Hashing Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)
- [NIST CSRC FIPS 180-4 Documentation](https://csrc.nist.gov/publications/fips#fips180-4)

- [NIST Retires SHA-1 Cryptographic Algorithm](https://www.nist.gov/news-events/news/2022/12/nist-retires-sha-1-cryptographic-algorithm)

## Password Hashing

Also done with MD5, SHA1, SHA2, SHA3, and others; password hashing is done with various algorithms.

- [BCrypt](https://en.wikipedia.org/wiki/Bcrypt)
- [BCrypt-Paper.pdf - A Future-Adaptable Password Scheme](https://www.openbsd.org/papers/bcrypt-paper.pdf)

- [Windows Passwords](https://learn.microsoft.com/en-us/windows-server/security/kerberos/passwords-technical-overview)
- [Cryptography Next Generation Algorithm Identifiers](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers)
- [NETNTLM_README: john-the-ripper](https://github.com/piyushcse29/john-the-ripper/blob/master/doc/NETNTLM_README)

- [3DES / TDES | Triple Data Encryption Standard](https://csrc.nist.gov/glossary/term/triple_data_encryption_standard)

## Advanced Encryption Standard (AES)

https://csrc.nist.gov/pubs/fips/197/final

[AES-128, AES-192, and AES-256](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf)

## Cracking LM NTLM, Net-NTLMv2 Passwords

- [John The Ripper](https://github.com/piyushcse29/john-the-ripper/blob/master/doc/README)
- [Article from Medium.com](./files/LM-NTLM-Net-NTLMv2_-_oh_my.pdf)

## QR Codes

- [ISO/IEC 18004:2024 QR Code Specification](https://www.iso.org/standard/83389.html)
- [QR Code Specification](https://www.qrcode.com/en/about/standards.html)

# JA4+ Network Fingerprinting
https://medium.com/foxio/ja4-network-fingerprinting-9376fe9ca637