# Cipher Feedback (CFB)
- Treats the block cipher like a stream cipher. Encrypts the previous ciphertext (or Initialization Vector) and XORs with the plaintext
- The block size can be smaller than the cipher block (byte-at-a-time)
- Can self-synchronize after a few blocks; good for stream data
- Still not parallelizable for encryption
- Use: Encrypted terminal session where data arrives byte by byte

## Link Explaining the Cipher
- [Tutorials Point - Cipher Feedback](https://www.tutorialspoint.com/cryptography/cipher_feedback_mode.htm)