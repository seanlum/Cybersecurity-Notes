# Buffer Manipulation

Below are some format parameters which can be used and their consequences:

- ”%x” Read data from the stack
- ”%s” Read character strings from the process’ memory
- ”%n” Write an integer to locations in the process’ memory

To discover whether the application is vulnerable to this type of attack, it’s necessary to verify if the format function accepts and parses the format string parameters shown in table 2.

Table 2. Common parameters used in a Format String Attack.

| Parameters | Output | Passed as |
|------------|--------|-----------|
|%%| % character (literal)|	Reference |
|%p| External representation of a pointer to void | Reference |
|%d|Decimal|Value|
|%c|Character|	| 
|%u|Unsigned decimal|Value|
|%x|Hexadecimal|Value|
|%s|String|Reference|
|%n|Writes the number of characters into a pointer|Reference|

# Example
```c
#include  <stdio.h> 
void main(int argc, char **argv)
{
	// This line is safe
	printf("%s\n", argv[1]);

	// This line is vulnerable
	printf(argv[1]);
}
```
```
./example "Hello World %p %p %p %p %p %p"
Hello World %p %p %p %p %p %p
Hello World 000E133E 000E133E 0057F000 CCCCCCCC CCCCCCCC CCCCCCCC
```
# OWASP Info
- [OWASP | Format String Attack](https://owasp.org/www-community/attacks/Format_string_attack)
  - [WebAppSec | Format String Attack | WASC-6](http://projects.webappsec.org/w/page/13246926/Format%20String)
    - [Analysis of Format String Bugs](https://www.cs.cornell.edu/courses/cs513/2005fa/paper.format-bug-analysis.pdf)
    - [Exploiting Format String Vulnerabilities](https://julianor.tripod.com/bc/formatstring-1.2.pdf)
      - [Bypassing stackguard and stackshield | Phrack Magazine | Volume 0xa Issue 0x38 ](http://phrack.org/issues/56/5.html)

# CWE Enumerations

- [CWE Category | Memory Buffer Errors](https://cwe.mitre.org/data/definitions/1218.html)
  - [CWE-120 | Buffer Copy without Checking Size of Input ('Classic Buffer Overflow')](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-121 | Stack-based Buffer Overflow](https://cwe.mitre.org/data/definitions/121.html)
- [CWE-124 | Use of Externally-Controlled Format String](https://cwe.mitre.org/data/definitions/134.html)
# CWE Attacks
- [CWE-77 | Command Injection](https://cwe.mitre.org/data/definitions/77.html)
- [CWE-78 | OS Command Injection](https://cwe.mitre.org/data/definitions/78.html)
- (SQL Only) [CWE-89 | SQL Injection](http://cwe.mitre.org/data/definitions/77.html)

# CAPEC Standard
- [CAPEC-123 Buffer Manipulation](https://capec.mitre.org/data/definitions/123.html)
  - [CAPEC-100 Overflow Buffers](https://capec.mitre.org/data/definitions/100.html)
    - [CAPEC-8 Buffer Overflow in an API Call](https://capec.mitre.org/data/definitions/8.html)

# Related ATT&CK Techniques

- [T1203 - Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203/)
- [T1068 - Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)
- [T1190 - Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
- [T1055 - Process Injection](https://attack.mitre.org/techniques/T1055/)
- [T1105 - Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)
