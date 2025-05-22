# SIV - Synthetic Initialization Vector
- Nonce-based authentication method and also deterministic nonce-less key wrapping
- Associated data is data input to an authenticated-encryption mode that will be authenticated but not encrypted
- Generateas an IV using MAC over data
- Encrypted using a CTR mode

### See also AES-GCM-SIV
https://en.wikipedia.org/wiki/AES-GCM-SIV

### Link Explaning the Cipher
https://datatracker.ietf.org/doc/html/rfc5297