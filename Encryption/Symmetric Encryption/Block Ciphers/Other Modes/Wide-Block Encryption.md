# Wide-Block Encryption
- Encrypts larger blocks  (e.g. full sectors or files) to resist watermarking and some chosen-plaintext attacks.

### Examples:
- `CMC`, `EME`, `EME2` (used in Helix or DiskCryptor)
    - **Usage**: Disk encryption, secure backup
    - **Notes**: More secure against structural attacks rather than CBC or ECB
- [Adiantum (Cipher) | HBSH (hash, block cipher, stream cipher, hash)](https://en.wikipedia.org/wiki/Adiantum_(cipher))
    - [Adiantum: length-preserving encryption for entry-level processors](https://tosc.iacr.org/index.php/ToSC/article/view/7360)
    - [Adiantum and HPolyC](https://github.com/google/adiantum)
    
#### HBSH (Hash-Block-Stream-Hash)
```
C = E_K^{H(AD, nonce)}(P)
```
- Where the tweak is a universal hash of associated data
- Secure even under nonce reuse and memory faults