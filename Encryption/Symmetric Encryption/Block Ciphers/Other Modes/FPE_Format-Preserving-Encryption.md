# Format-Preserving Encryption (FPE)
- Encrypts data while preserving its format (e.g. credit card numbers, zip codes)

### Examples
- `FF1` / `FF3` (NIST-specified FPE modes using AES)
    - **Usage**: Tokenization, payment systems, masked PII
    - **Notes**: Keeps length and charset of input (e.g. 16-digit card stays 16-digit)

### Links Explaining The Cipher
- [Wikipedia | Format-preserving encryption](https://en.wikipedia.org/wiki/Format-preserving_encryption)