# MAC - Message Authentication Code
- [Wikipedia | Message Authentication Code](https://en.wikipedia.org/wiki/Message_authentication_code)
- [CS121.org | Message Authentication Codes (MACs)](https://textbook.cs161.org/crypto/macs.html)
- [G4G | How Message Authentication Codes work](https://www.geeksforgeeks.org/how-message-authentication-code-works/)
- [NIST | Message Authentication Code (MAC) Algorithm](https://csrc.nist.gov/glossary/term/message_authentication_code_algorithm)
- [NIST | Recommendation for Pair-Wise Key Establishment Using Integer Factorization Cryptography](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Br2.pdf)
- [WSUTL.edu | Message Authentication Codes](https://www.cse.wustl.edu/~jain/cse571-11/ftp/l_12mac.pdf)

### Types of MACs
- [HMAC - Hash-based Message Authentication Code](./Message%20Authentication%20Code/HMAC_Hash-Based%20MAC.md)
- [CMAC - Cipher-based Message Authentication Code](./Message%20Authentication%20Code/CMAC_Cipher-based%20MAC.md)
- [CBC-MAC - Chained Block Cipher Message Authentication Code](./Message%20Authentication%20Code/CBC-MAC_Chained%20Block%20Cipher%20MAC.md)

### NIST Definition for MAC
```
 A family of cryptographic functions that is parameterized by a symmetric key. Each of the functions can act on input data (called a “message”) of variable length to produce an output value of a specified length. The output value is called the MAC of the input message. An approved MAC algorithm is expected to satisfy the following property (for each of its supported security levels): It must be computationally infeasible to determine the (as yet unseen) MAC of a message without knowledge of the key, even if one has already seen the results of using that key to compute the MAC's of other (different) messages. A MAC algorithm can be used to provide data-origin authentication and data-integrity protection. In this Recommendation, a MAC algorithm is used for key confirmation; the use of MAC algorithms for key derivation is addressed in SP 800-56C
```

### YouTube | 16. Message Authentication Code MAC
[![16. Message Authentication Code MAC](https://img.youtube.com/vi/zmvwYWaAZ-g/sddefault.jpg)](https://www.youtube.com/watch?v=zmvwYWaAZ-g)

### YouTube | MAC (Message Authentication Codes) and HMAC by Christoff Paar
[![MAC (Message Authentication Codes) and HMAC by Christoff Paar](https://img.youtube.com/vi/DiLPn_ldAAQ/sddefault.jpg)](https://www.youtube.com/watch?v=DiLPn_ldAAQ)

### Definition
- A `message authentication code (MAC)` is a piece of information used for authenticating and integrity-checking a message.
- MACs rely on the sender and receiveer to share the same key. The sender generates a fixed-size output of a cryptographic checksum or message authentication code and appends it to the original message.
- MACs take a `Message`, a `Key`, `MAC algorithm`, and a `MAC value`.
- MAC values allow verifiers (who also posess a secret key to detect any changes to the message content).
- MACs are different from cryptographic hashing functions. A MAC is also known as a `keyed checksum`. MACs are also different from signing algorithms.