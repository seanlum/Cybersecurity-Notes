# Counter (CTR)
- Encrypts a counter (usually starting with a nonce) for each block, and XORs with plaintext
- Pros
    - Fully parallelizable
    - Precomputable keystream
    - No chaining or feedback - simple and fast
- Cons
    - Reusing the counter (nonce) with the same key breaks security
- Widely used in modern protocols (e.g. AES-CTR in TLS, IPsec, disk encryption)

### Link Explaining the Cipher
- [Tutorials Point - Counter](https://www.tutorialspoint.com/cryptography/counter_mode.htm)