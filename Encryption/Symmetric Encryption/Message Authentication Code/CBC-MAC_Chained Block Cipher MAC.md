# Chained Block Cipher MAC
CBC-MAC or Cipher Block Chaining Message Authentication Code (CBC-MAC) uses a general block cipher to create a message authentication code. The MAC is generally created using a block cipher in CBC mode. The CBC-MAC method was generally used in the CCM mode, and CCMP mode of encryption. The CBC-MAC algorithm was specified to use DES (Data Encryption Standard) as the block cipher in FIPS PUB 113: Computer Data Authentication. CBC-MAC is only secure for fixed-length messages. For variable-length messages, it is vulnerable to attacks, and it is recommended to use a different mode of operation, such as [CMAC](./CMAC_Cipher-based%20MAC.md).

### YouTube video explaining CBC-MAC
[![CBC-MAC](https://img.youtube.com/vi/OvoJ-6If1Os/sddefault.jpg)](https://www.youtube.com/watch?v=OvoJ-6If1Os)

### Articles
- [Wikipedia | CBC-MAC](https://en.wikipedia.org/wiki/CBC-MAC)