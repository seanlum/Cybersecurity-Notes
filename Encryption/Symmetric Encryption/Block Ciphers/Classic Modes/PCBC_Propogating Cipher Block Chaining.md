# Propogating Cipher Block Chaining (PCBC)
- Like CBC, but the plaintext and ciphertext of the previous block are both XORed with the current plaintext block
- Pros
    - Enhanced error propagation - useful for tamper detection
- Cons
    - Not widely used or supported
- Used for educational purposes, some older systems like Kerberos 4

### Link Explaining the Cipher
- [oleskii - Propagating Cipher Block Chaining](https://oleksii.shmalko.com/20200318130825/)