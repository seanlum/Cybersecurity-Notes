# Idea for a Arduino bug

I see people talk about bugs all the time. Just decided to brainstorm.

Build a LORA radio transmitting text transcribed on an Arduino encrypted with AES and RSA, from a bug installed in an electrical box, in a wall, behind patched drywall, with a little hole for the microphone and a small cover over the microphone that masks it from the wall and doesn't block audio. The bug runs on a 120v or 220v to 12v adapter on the houses power.

If you want this in your house, its legal. If you don't it's illegal. Don't be an asshole.

Honestly, I've also thought about turning GFCI outlets and smoke detectors into a bug before.

### Features
- Uses non-standard frequency
- Encrypts data
- Runs on lay of the land
- Arduino is modular
- Parts can be improved

# How to install electical outlet boxes
- [How to install electrical outlet boxes](https://www.youtube.com/watch?v=0wMYYJAHytg)

# How to Fix Holes in Drywall 
- [How to Fix Holes in Drywall - 4 Easy Methods](https://www.youtube.com/watch?v=uvQK7WTkKpI)

# How to install a GFCI outlet
- [HOW TO INSTALL A GFCI OUTLET](https://www.youtube.com/watch?v=TqTNJUT_lKg)

# 220v AC to 9v DC Converter 
- [How to Convert 220v AC to 9v DC | (9v DC Power Supply)](https://www.youtube.com/watch?v=sQOeOKP9_ug)

# 120v AC to 12v DC using SAE connectors
- [DIY Build your own AC/DC adapter (120v AC to 12v DC) using SAE connectors.](https://www.youtube.com/watch?v=5iMYtmXmYiU)

# Arduino Voice Recorder
- [Make your own Spy Bug (Arduino Voice Recorder)](https://www.youtube.com/watch?v=7Hn4UFi9wvs)

# Installing in-wall speakers
- [Installing in-wall speakers | Crutchfield video](https://www.youtube.com/watch?v=1exPJODQ7rs)

# Wireless Transmitter
- [You've Never Seen WiFi Like This](https://www.youtube.com/watch?v=9azEfCQNhSA)

# RSA Encryption with Arduino
1.	Install the ArduinoRSALib library: You can find it on GitHub or other sources and add it to your Arduino libraries.
2.	Example Code:
```c
#include <ArduinoRSALib.h>

RSA rsa;

void setup() {
  Serial.begin(9600);

  // Generate RSA keys
  rsa.generateKeys(512); // 512-bit key for demonstration; use larger keys for real applications

  // Example message
  char message[] = "Hello, RSA!";
  char encryptedMessage[128];
  char decryptedMessage[128];

  // Encrypt
  rsa.encrypt(encryptedMessage, message, rsa.getPublicKey());
  Serial.print("Encrypted: ");
  Serial.println(encryptedMessage);

  // Decrypt
  rsa.decrypt(decryptedMessage, encryptedMessage, rsa.getPrivateKey());
  Serial.print("Decrypted: ");
  Serial.println(decryptedMessage);
}

void loop() {
  // Nothing to do here
}
```

# AES Encryption with Arduino
1.	Install the AESLib library: You can install it via the Arduino Library Manager.
2.	Example Code:
```c
#include <AESLib.h>

AESLib aesLib;

byte aes_key[] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F};
char plainText[] = "Hello, World!";
char encryptedText[128];
char decryptedText[128];

void setup() {
  Serial.begin(9600);

  // Encrypt
  aesLib.encryptBlock(encryptedText, plainText, aes_key);
  Serial.print("Encrypted: ");
  Serial.println(encryptedText);

  // Decrypt
  aesLib.decryptBlock(decryptedText, encryptedText, aes_key);
  Serial.print("Decrypted: ");
  Serial.println(decryptedText);
}

void loop() {
  // Nothing to do here
}
```
# Estimation on data transfer
To estimate the number of bytes required for 1 minute of audio talking, transcribed to text, and then encrypted with RSA, we need to break down the process into several steps:
1.	Transcription of Audio to Text:
-	Audio Duration: 1 minute of talking.
-	Words per Minute (WPM): The average speaking rate is about 150 words per minute.
-	Average Word Length: Assuming an average word length of 5 characters (including spaces and punctuation).
2.	Text Size Calculation:
-	Total Characters: 150 words * 5 characters/word = 750 characters.
-	Bytes for Text: Assuming 1 byte per character (using ASCII encoding), the text size is 750 bytes.
3.	RSA Encryption:
-	RSA Key Size: Let's assume a 2048-bit RSA key (256 bytes).
-	Encryption Process: RSA typically encrypts data in blocks that are smaller than the key size. For a 2048-bit key, the maximum block size is 245 bytes (256 bytes - 11 bytes for padding using PKCS#1 v1.5).
Step-by-Step Calculation:
1.	Transcription to Text:
    -	1 minute of talking ≈ 150 words.
    -	150 words * 5 characters/word = 750 characters.
    -	750 characters * 1 byte/character = 750 bytes.
2.	RSA Encryption:
    -	Block Size: For a 2048-bit key, the block size is 245 bytes.
    -	Number of Blocks: 750 bytes / 245 bytes/block ≈ 4 blocks (since we need to round up to the next whole block).
    -	Encrypted Block Size: Each block, when encrypted, will be the size of the RSA key, which is 256 bytes.
3.	Total Encrypted Size:
    -	4 blocks * 256 bytes/block = 1024 bytes.

### Summary:
-	Original Text Size: 750 bytes.
-	Encrypted Text Size: 1024 bytes.
Therefore, 1 minute of audio talking, transcribed to text, and then encrypted with a 2048-bit RSA key, would result in approximately 1024 bytes of encrypted data.
Important Considerations:
-	Efficiency: RSA is not typically used for encrypting large amounts of data directly due to its inefficiency. Instead, RSA is often used to encrypt a symmetric key (e.g., AES key), which is then used to encrypt the actual data.
-	Padding: The calculation assumes PKCS#1 v1.5 padding. Different padding schemes may slightly alter the block size.
-	Encoding: The text size calculation assumes ASCII encoding. If using UTF-8 or another encoding, the byte size may vary.