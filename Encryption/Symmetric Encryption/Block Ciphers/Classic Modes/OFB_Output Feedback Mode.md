# Output Feedback Mode (OFB)
- Like [Cipher Feedback](./CFB_Cipher%20Feedback.md), but the output of the cipher (not the ciphertext) is fed back for the next encryption step
- No error propagation; precompute the keystream
- Cons: Reusing the IV breaks security completely
- Used in environments needing high fault tolerance (e.g. satellite links)

### Link Explaining the Cipher
- [Tutorials Point - Output Feedback Mode](https://www.tutorialspoint.com/cryptography/output_feedback_mode.htm)