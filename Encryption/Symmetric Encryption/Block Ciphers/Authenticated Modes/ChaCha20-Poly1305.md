# ChaCha20-Poly1305
- AEAD mode using stream cipher ChaCha20 and Poly1305 MAC. Fast on software-only devices. Default in TLS 1.3 for mobile.
- The ChaCha20-Poly1305 algorithm takes as input a 256-bit key and a 96-bit nonce to encrypt a plaintext
- Ciphertext expansion of 128-bit (the tag size)
- In the ChaCha20-Poly1305 construction, ChaCha20 is used in counter mode to derive a key stream that is XORed with the plaintext. 

### Link Explaining Cipher
https://en.wikipedia.org/wiki/ChaCha20-Poly1305