# Galois/Counter Mode
- Based on CTR + a Galois field MAC for authentication
- Fast and parallizable, authenticated
- Standard in TLS 1.2+, SSH, IPsec, disk encryption, etc.
- Requires a Nonce/IV which never repeats (96 bits is recommended)
- Pros
    - Fast, parallelizable, hardware-accelerated (AES-NI)
    - AEAD standard in TLS, SSH, IPsec
- Cons
    - Nonce reuse is catastrophic
    - More complex implementation (Galois math)
### NIST Galois/Counter Mode of Operation
- https://csrc.nist.rip/groups/ST/toolkit/BCM/documents/proposedmodes/gcm/gcm-spec.pdf

### Link Explaining GCM
- [https://en.wikipedia.org/wiki/Galois/Counter_Mode](https://en.wikipedia.org/wiki/Galois/Counter_Mode)