# Cipher Block Chaining (CBC)
- Each plaintext block is XORed with the previous ciphertext block before being encrypted
- Needs an `Initialization Vector (IV)` for the first block
- Hides patterns better than ECB
- Cannot be encrypted in a parallelizable fashion. Errors can propogate and corrupt multiple blocks
- Commonly used for secure file storage and older protocols

## Link for Explanation
- [Tutorials Point - Cipher Block Chaining](https://www.tutorialspoint.com/cryptography/cipher_block_chaining_mode.htm)