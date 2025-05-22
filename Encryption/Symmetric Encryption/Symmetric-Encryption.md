# Symmetric Key Encryption
- Uses the same key for encryption and decryption
- [Symmetric-key Algorithm](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)

# Block Ciphers
- [Block Ciphers](https://en.wikipedia.org/wiki/Block_cipher)
    - [Geeks for Geeks - Block Ciphers - Modes of Operation](https://www.geeksforgeeks.org/block-cipher-modes-of-operation/)
    - [Wikipedia - Block cipher mode of operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation)
    - [NIST - Block Cipher Modes](https://csrc.nist.gov/projects/block-cipher-techniques/BCM)
    - [CTF101 - What are Block Ciphers](https://ctf101.org/cryptography/what-are-block-ciphers/)
    - [Wikipedia - Authenticated Block Ciphers](https://en.wikipedia.org/wiki/Authenticated_encryption)
    - [Tink Cryptographic Library | Authenticated Encryption with Associated Data (AEAD)](https://developers.google.com/tink/aead)
###  Classic Cipher Modes

| Mode | IV Required | Parallel Encrypt | Error Propagation | Stream-Like | Notes |
|-|-|-|-|-|-|
| [ECB - Electronic Code Book](./Block%20Ciphers/Classic%20Modes/ECB_Electronic%20Code%20Book.md) | ❌ | ✅ | None | ❌ | Not secure | 
| [CBC - Cipher Block Chaining](./Block%20Ciphers/Classic%20Modes/CBC_Cipher%20Block%20Chaining.md) | ✅ | ❌ | 2 blocks | ❌ | Common, secure with padding | 
| [CFB - Cipher Feedback](./Block%20Ciphers/Classic%20Modes/CFB_Cipher%20Feedback.md) | ✅ | ❌ | 1 block	| ✅	| Stream cipher style |
| [OFB - Output Feedback](./Block%20Ciphers/Classic%20Modes/OFB_Output%20Feedback%20Mode.md) | ✅ | ✅ (precompute) | None | ✅ | Stream cipher, tolerant |
| [CTR - Counter](./Block%20Ciphers/Classic%20Modes/CTR_Counter.md) | ✅ (nonce) | ✅ | None | ✅ | Modern, fast |
| [PCBC - Propogating Cipher Block Chaining](./Block%20Ciphers/Classic%20Modes/PCBC_Propogating%20Cipher%20Block%20Chaining.md) | ✅ | ❌ | Full propagation | ❌ | Rare |

### Authenticated Cipher Modes
- [Comparing Security: Encrypt-Then-MAC vs. MAC-Then-Encrypt](https://www.e2encrypted.com/posts/encrypt-then-mac-vs-mac-then-encrypt/)
- [Popular Authenticated Encryption Methods](https://www.e2encrypted.com/posts/popular-authenticated-encryption-methods/)
- [Authenticated Encryption: How Reordering can Impact Performance (PDF)](https://eprint.iacr.org/2014/958.pdf)

| Mode	| Authenticated? |	Nonce Reuse Safe? |	Parallelizable? |	Efficiency	| Notes | 
|-|-|-|-|-|-|
| [GCM - Galois/Counter Mode](./Block%20Ciphers/Authenticated%20Modes/GCM_Galois-Counter-Mode.md) | ✅ | ❌ (very unsafe) | ✅ | Very High | Standard in TLS/IPsec | 
| [CCM - Counter with CBC-MAC](./Block%20Ciphers/Authenticated%20Modes/CCM_Counter-with-CBC-MAC.md) | ✅ | ❌ | ❌ | Medium | Used in IoT | 
| [EAX - EAX Mode](./Block%20Ciphers/Authenticated%20Modes/EAX_EAX-Mode.md) | ✅ | 🟡 (better) | ✅	| High | Patent-free |
| [OCB - Offset Codebook Mode](./Block%20Ciphers/Authenticated%20Modes/OCB_Offset-Codebook-Mode.md) | ✅ | ❌ | ✅ | Highest	| Fast but less used | 
| [SIV - Synthetic Initialization Vector](./Block%20Ciphers/Authenticated%20Modes/SIV_Synthetic-Initialization-Vector.md) | ✅ | ✅ | ❌ | Low | Misuse-resistant | 
| [ChaCha20-Poly1305](./Block%20Ciphers/Authenticated%20Modes/ChaCha20-Poly1305.md) | ✅ | ❌ | ✅ | Very High | Great for mobile, TLS 1.3 |

### 🔐 Authenticated Encryption Modes (AEAD)
| Mode | Example Algorithm | Real-World Usage |
|-|-|-|
| CCM | AES-CCM | Used in Zigbee, Bluetooth Low Energy, 802.15.4, and IoT devices |
| EAX | AES-EAX | Used in libsodium, NaCl, some embedded systems; patent-free alternative | 
| GCM | AES-GCM | Used in TLS 1.2+, SSH, IPsec, disk encryption, and HTTPS (OpenSSL) | 
| IAPM | AES-IAPM (Integrity-Aware Parallelizable Mode) | Research-grade; seen in academic papers, rarely in production | 
| OCB | AES-OCB | Formerly patented; used in Secure Messaging, OpenPGP (experimental) | 
| SIV | AES-SIV | Used in Tink, Misuse-resistant key wrapping, backup encryption where nonce reuse is possible | 

### 🧱 Classic Block Cipher Modes
| Mode | Example Algorithm | Real-World Usage | 
|-|-|-|
| CBC | AES-CBC | Used in file encryption (OpenSSL), legacy VPNs, older TLS versions, TrueCrypt/Veracrypt | 
| CFB | AES-CFB8 / CFB128 | Used in encrypted SSH sessions, some smartcards, stream-like data | 
| CTR | AES-CTR | Used in disk encryption, IPsec, OpenSSL, TLS/DTLS, GCM foundation | 
| ECB | AES-ECB | Rare; sometimes used for key wrapping, test vectors, or firmware blobs (❗ insecure for data) | 
| OFB | AES-OFB | Used in low-error-tolerant channels like satellite communications | 
| PCBC | AES-PCBC | Used in Kerberos v4 (now obsolete), and education/testing scenarios | 

### Some Examples of Types of Symmetric Encryption
- [AES (Advanced Encryption Standard)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [DES (Data Encryption Standard)](https://en.wikipedia.org/wiki/Data_Encryption_Standard)
- [Triple DES](https://en.wikipedia.org/wiki/Triple_DES)
- [RC4 (Rivest Cipher 4)](https://en.wikipedia.org/wiki/RC4)
- [Twofish](https://en.wikipedia.org/wiki/Twofish)
- [Serpent](https://en.wikipedia.org/wiki/Serpent_(cipher))
- [Camellia (cipher)](https://en.wikipedia.org/wiki/Camellia_(cipher))
- [Salsa20](https://en.wikipedia.org/wiki/Salsa20)
- [ChaCha20](https://en.wikipedia.org/wiki/ChaCha20)
- [Blowfish](https://en.wikipedia.org/wiki/Blowfish_(cipher))
= [CAST5](https://en.wikipedia.org/wiki/CAST5)
- [Kuznyechik](https://en.wikipedia.org/wiki/Kuznyechik)
- [Skipjack](https://en.wikipedia.org/wiki/Skipjack_(cipher))
- [Safer](https://en.wikipedia.org/wiki/Secure_and_Fast_Encryption_Routine)
- [IDEA](https://en.wikipedia.org/wiki/International_Data_Encryption_Algorithm)