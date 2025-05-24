# Hash-Based MAC
Hash-based MACs are generally performed with any secure hashing function, such as SHA-256 and are widely used with algorithms like TLS, SSH, JWT, APIs, and key derivation (HKDF, PBKDF2). Also it is used with those algorithms in technologies like IoT, HTTPS, and SFTP. However they are not parallelizable. And are considered secure as long as the hash function is secure. This is also known as a key-hashed message authentication code or hash-based message authentication code. HMAC is mostly attack resistant.

### YouTube | Securing Stream Ciphers (HMAC) - Computerphile
[![Securing Stream Ciphers (HMAC)](https://img.youtube.com/vi/wlSG3pEiQdc/sddefault.jpg)](https://www.youtube.com/watch?v=wlSG3pEiQdc)

### Formula
```
HMAC(K, M) = H((K ⊕ opad) || H((K ⊕ ipad) || M))

or 

HMAC = hashFunc(secret key + message) 
```

## Links explaining the MAC
- [Wikipedia | HMAC](https://en.wikipedia.org/wiki/HMAC)
- [Geeks for Geeks | What is a HMAC](https://www.geeksforgeeks.org/what-is-hmachash-based-message-authentication-code/)
- [IETF | Using HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512 with IPsec](https://www.ietf.org/rfc/rfc4868.txt)
- [(OLDER) IETF | MD5-HMAC](https://datatracker.ietf.org/doc/html/rfc6151)
- [(OLDER) IETF | HMAC: Keyed-Hashing for Message Authentication](https://datatracker.ietf.org/doc/html/rfc2104)