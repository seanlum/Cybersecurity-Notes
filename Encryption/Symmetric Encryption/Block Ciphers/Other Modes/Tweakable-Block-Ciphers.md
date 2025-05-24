# Tweakable Block Ciphers
Regular block ciphers will take a key, initialization vector, and a message to produce a ciphertext. A tweakable block cipher takes in a "tweak value". The IV is a generally deterministically created value which is created by the input from the key and a data stream. In a tweakable block cipher, this value is a "tweak" rather than a "nonce" or "IV". This may be metadata associated with the file or object being encrypted, rather than an external value like a reused IV. For example a lock which uses different pin settings for each room.

Tweak values may be applied to the key, a derivation value, or aspects of the message. Tweak values may be permutated from either of the inputs. And the tweak values may be unique to the context of the message being encrypted.

## Tweakable Block Chaining
Similar to cipher block chaining (CBC), instead of an initialization vector, the tweak value is used for the successive message block. Or in other cases, a CBC operation is performed, but a tweak value is added to each step in the chaining process. The tweakable block chaining replaces or augments the IV with a tweak drived from position/context in the chain. The benefit is that each block is encrypted uniquely, even if the key and the plaintext is the same. Useful for disk encryption where sectors must be encrypted independently.

#### Example
- [`XEX` XOR-Encrypt-XOR](https://en.wikipedia.org/wiki/Xor%E2%80%93encrypt%E2%80%93xor), like [`XTS-AES Mode for Confidentiality on Storage Devices`](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-38e.pdf)
- Tweak is often based on sector number + block index
```
C_i = E_K^T(P_i ⊕ Δ_i) ⊕ Δ_i

Where:
Δ_i = α^i × Tweak (in GF(2^n))
```
- Tweak is derived from metadata (e.g., disk sector number)

## Tweakable Chain Hashing
Like a cryptographic hash; constructed using tweakable block ciphers, similar to the [Merkle–Damgård construction](https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction) or [Davies-Meyer construction](https://en.wikipedia.org/wiki/One-way_compression_function#Davies%E2%80%93Meyer). These operations may help to build [Sponge](https://en.wikipedia.org/wiki/Sponge_function)-Compatible hases or keyed MACs.

- [Crypto Stack Exchange | Questions on Davies-Meyer Construction](https://crypto.stackexchange.com/questions/98159/davies-meyer-block-cipher-and-iv)
- [Cryptology ePrint Archive | Building Quantum-One-Way Functions from Block Ciphers: Davies-Meyer and Merkle-Damgård Constructions](https://eprint.iacr.org/2018/841)

#### Example
```
H₀ = IV
Hᵢ = E_K^{Tᵢ}(Hᵢ₋₁ ⊕ Mᵢ)
```

#### Used in
- [HAIFA - Hash Iterative Framework](https://en.wikipedia.org/wiki/HAIFA_construction)
- [A Framework for Iterative Hash Functions](https://eprint.iacr.org/2007/278)
- [Skein (hash function)](https://en.wikipedia.org/wiki/Skein_(hash_function))
    - [Schneier Article on Skein](https://www.schneier.com/academic/skein/)
    - [Skein Hash Function Family](https://www.schneier.com/wp-content/uploads/2015/01/skein.pdf)
    - [Skein Hash Function Family | NIST Round 3 Tweak Description](https://www.schneier.com/wp-content/uploads/2015/01/skein-1.3-modifications.pdf)

### Tweakable Authenticated Encryption
This is Authenticated Encryption (AE) where the encryption algorithm itself is tweakable. This adds stronger guarantees, such as:
- Nonce misuse resistance
- Deterministic authenticated encryption
- Key separation via tweak

#### Examples
- [SIV - Synthetic IV Mode](../Authenticated%20Modes/SIV_Synthetic-Initialization-Vector.md)
```
IV = MAC_K(P || AD)
C = AES-CTR_K^IV(P)
```

- [Wide-Block or HBSH Encryption](../Other%20Modes/Wide-Block%20Encryption.md)
- [Offset Code Book (OCB)](../Authenticated%20Modes/OCB_Offset-Codebook-Mode.md)

### Examples
- [XTS-AES](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-38e.pdf) (XEX Tweakable Block Cipher with Ciphertext Stealing)
    - **Usage**: Disk Encryption (BitLocker, FileVault, VeraCrypt)
    - **Note**: Encrypts sectors with tweaks derived from sector numbers
- `LRW`, `XEX`, and `HCTR`
    - **Usage**: Disk and database encryption
    - **Notes**: Tweak ensures ciphertext uniqueness without full rekeying

## Springer - Tweakable Block Ciphers
- [Journal of Cryptology | Tweakable Block Ciphers](https://link.springer.com/content/pdf/10.1007/s00145-010-9073-y.pdf)

## Berkeley - Twofish Tweakable Block Cipher
- [Berkeley | Tweakable Block Cipher](https://people.eecs.berkeley.edu/~daw/papers/tweak-crypto02.pdf)