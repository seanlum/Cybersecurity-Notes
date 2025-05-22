# CCM Mode
- Encrypts using [counter (CTR) mode](../Classic%20Modes/CTR_Counter.md) and authenticates with [cipher block chaining message authentication code (CBC-MAC)](https://en.wikipedia.org/wiki/CBC-MAC)
- Two-pass: one for MAC, and one for encryption
- Pros
    - Standardized (NIST), used in constrained devices. Like 802.15.4 (Zigbee)
    - Authenticated
- Cons
    - Slower than GCM
    - Not parallelizable
    - More sensitive to implementation flaws

### NIST - Recommendation for Block Cipher Modes of Operation: The CCM Mode for Authentication and Confidentiality
https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-38c.pdf

### Link Explaining CCM
https://en.wikipedia.org/wiki/CCM_mode