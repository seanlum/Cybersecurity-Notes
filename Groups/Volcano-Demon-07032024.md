# Volcano Demon
```
Indicators of Compromise
The following artifacts were associated with Volcano Demon. At the time of publishing, all were uploaded to VT with multiple being flagged:
```
| Name | Description	| SHA256 | Hash	On VirusTotal |
|-|-|-|-|
| Protector.exe	| Trojan | f83abe3d9717238755f1276c87b3b320d8c30421984a897099ce3741d9143906	| Yes; 38/73 | 
| Locker.exe | Encryptor | 4e58629158a6c46ad420f729330030f5e0b0ef374e9bb24cd203c89ec3262669 |	 Yes; 7/68 |
| Linux locker.bin | Linux Encryptor |	ac08ab5bfc5f2cfa0703115a0e2b61decc5158ec0d8a99ebc0824da2b4c3d25	| No; 0/64
| Reboot.bat |	Command line scripts as precursors to encryption event  | ed32ebb15d4abe262a34e54408ebb0680b62dc975bf6c02652d28006f45fca14 | No; 0/64 |

### Jul 1, 2024
https://www.halcyon.ai/blog/halcyon-identifies-new-ransomware-operator-volcano-demon-serving-up-lukalocker

### July 3, 2024
https://www.darkreading.com/cyberattacks-data-breaches/ransomware-eruption-novel-locker-malware-flows-from-volcano-demon

```
So the company's data is encrypted by the ransomware?

Yes, the Volcano Demon ransomware group encrypts files on your company network with LukaLocker, changing file extensions to .nba.
```

### July 4, 2024
https://www.tripwire.com/state-of-security/volcano-demon-ransomware-group-rings-its-victims-extort-money

```
The group used a double extortion technique to maximize the chances of receiving payment, Halcyon said. Prior to the LukaLocker infection, they exfiltrated victims’ data to command-and-control (C2) services and only then encrypted it.

Tracking this threat actor was challenging, researchers said. The attackers cleared log files on targeted machines  before exploitation, “making a comprehensive forensic evaluation nearly impossible.” 
```
### July 3rd, 2024
https://therecord.media/ransomware-group-volcano-demon-lukalocker

```
Halcyon researchers have recently detected new double-extortion ransomware operators, tracked as Volcano Demon, behind a series of attacks in the past two weeks. Adversaries take advantage of a Linux iteration of LukaLocker ransomware that encrypts targeted files with the .nba file extension. Volcano Demon also employs a set of adversary techniques to stay under the radar and hinder defensive measures. The LukaLocker ransomware used by adversaries is an x64 PE binary written and compiled in the C++ programming language. It leverages API obfuscation and dynamic API resolution to hide its offensive functions, making it difficult to detect, analyze, and reverse engineer.
```

https://socprime.com/blog/volcano-demon-ransomware-attack-detection-adversaries-apply-a-new-lukalocker-malware-demanding-ransom-via-phone-calls/
