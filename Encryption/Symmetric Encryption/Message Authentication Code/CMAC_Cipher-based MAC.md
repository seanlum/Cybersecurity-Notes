# Cipher-based MAC

Uses a block cipher like AES. It also uses a single key and internal subkey derivation. HMAC differs from CMAC because HMAC uses hashing functions and not block ciphers. CMAC can also be considered a mode of operation of a block cipher. This type of algorithm is not parallelizable.

CMAC is touted for being mre secure because it provides a stronger level of assurance of data integrity than a checksum or error detecting code. It also needs to be performed using a FIPS approved block cipher.

### Note
- The `CMAC key` is also the `block cipher key`

### Usages
- `LTE`, `IPsec`, `embedded crypto`

### YouTube | CMAC or HMAC?
[![CMAC or HMAC?](https://img.youtube.com/vi/CYGMcfZ--Ww/sddefault.jpg)](https://www.youtube.com/watch?v=CYGMcfZ--Ww)

### Explanation: NIST SP 800-38b | The CMAC Mode for Authentication
- https://csrc.nist.gov/pubs/sp/800/38/b/upd1/final
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38B.pdf

### AES-CMAC
- [IETF | The AES-CMAC Algorithm](https://datatracker.ietf.org/doc/html/rfc4493)

