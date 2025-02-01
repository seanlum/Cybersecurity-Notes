
# OWASP Developer Guide - References
Obviously if you install every tool required in this book; there are many potential consequences of bloat and process fatigue. Automation or simplification or streamlining are important with this guide.

- CyBOK - The Cyber Security Body of Knowledge
- OWASP Software Assurance Maturity Model (SAMM)
- CIA Triad - Confidentiality, Integrity, Availability
- AAA Triad - Authentication, Authorization, Accounting/Auditing
- WHATWG HTML Living Standard
- OWASP Cheat Sheet Series
- Secure SDLC 
- DevOps Continual-Integration / Continual-Deployment
- DependencyTrack SBOM
- DependencyCheck (SCA)
## OWASP Verification Projects
- Application Security Verification Standard (ASVS)
- Amass project
- Code Pulse
- Defect Dojo
- Mobile Application Security (MAS)
- Nettacker
- Offensive Web Testing Framework
- Web Security Testing Guide (WSTG)
## OWASP Training Projects
- API Security Project (API Top 10)
- Juice Shop
- Mobile Top 10
- Security Shepherd
- Snakes and Ladders
- Top Ten Web Application security risks
- WebGoat
## OWASP resources
- CSRFGuard Library
- Dependency-Check Software Composition Analysis (SCA)
- Dependency-Track Continuous SBOM Analysis Platform
- Enterprise Security API (ESAPI)
- Integration Standards project Application Security Wayfinder
- Mobile Application Security (MAS)
- Pythonic Threat Modeling
- Threat Dragon
- SecurityRAT (Requirement Automation Tool)

## Authentication Notes
- OpenID OAuth 2.0 with HMAC SHA AES-256 BCrypt
- Encryption Services: TPM, DRM, and UEFI Secure Boot
- SAML Security
- PKI with Elliptic Curve Cryptography such as Diffie Helman is suggested

## Software Vulnerabilities
They mention the various OWASP Top 10s for 2021
- API Security Top 10
- Data Security Top 10
- Low-Code/No-Code Top 10
- Mobile Top 10
- Serverless Top 10
- Top CI/CD Security Risks
- Top 10 for Large Language Model Applications
- Top 10 Privacy Risks
- Top 10 Proactive Controls
- Top 10 Web Application Security Risks

# Requirements
## OWASP Security Knowledge Framework
- OWASP Secure Assurance Maturation Model 
- Application Security Verification Standard
- Mobile Application Security Verification Standard
- OWASP Risk Rating Methodology
- TAME - Transfer, Acceptance, Mitigation, Eliminate / Avoid
- NIST SP 800-30 - Guide for Conducting Risk Assessments 
- Government of Canada - The Harmonized Threat and Risk Assessment Methodology
- Mozilla's Risk Assessment Summary and Rapid Risk Assessment (RRA)
- NIST Common Vulnerability Scoring System (CVSS)
- OWASP Application Security Fragmentation
- OWASP Integration Standards Project
- OWASP Security RAT - Requirement Automation Tool
- OWASP Security CAT - Compliance Automation Tool
## OpenCRE
OpenCRE is a compendium of standards and reference material for enumerating vulnerabilities. 
- CAPEC
- CWE
- NIST SP 800-53, 800-63
- OWASP ASVS
- OWASP Top 10 
- OWASP Proactive Controls
- OWASP Cheat Sheets
- OWASP WSTG
- ZAP
# Design
- PoLP and Separation of Duties
- Defense-in-Depth
- Zero Trust
- Security in the Open
- Secure Development Lifecycle (SDLC)
- OWASP Threat Model
- Shostack's Four Question Framework
1. What are we working on?
```
Threat Modeling
	- Architecture Diagrams
	- Dataflow Transitions
	- Data classifications
```
2. What can go wrong?
```
CIA Triad Components
STRIDE
LINDUN
Cyber Kill Chains
PASTA
CAPEC
```
3. What are we going to do about that?
```
TAME Tactics
``` 
4. Did we do a good enough job?
```
OWASP Threat Modeling Playbook referenced in step 4?
```

### Methodology Process
```
1. Define Terminology
2. Define Scope
3. Define Documentation
4. Decompose the system into manageable processes
5. Establish trusts and boundaries
6. Declare agents, actors, and capabilities
7. Categorize factors of impact and probability
8. Remediate identified threats, the purpose of modeling
```

## Design References
- Threat Modeling Manifesto
- OWASP Threat Model Project 
- OWASP Threat Modeling Cheat Sheet
- OWASP Threat Modeling Playbook (OTMP)
- OWASP Attack Surface Analysis Cheat Sheet
- Threat Modeling Process
- The Four Question Framework
- Lockheeds Cyber Kill Chain
- VerSprite's Process for Attack Simulation and Threat Analysis (PASTA)
- Threat Modeling: Designing for Security
- Threat Modeling: A Practical Guide for Development Teams
- OWASP pytm Pythonic Threat Modeling Tool
- OWASP Threat Dragon
- Microsoft Threat Modeling Tool
- Threatspec
- MITRE's CAPEC
- NIST CVSS

### pytm 
Allows you to perform threat modeling on application code bases. Models are output as PlantUML.jar sequences or Markdown, PDF, ePub, or HTML. Input models are in JSON and YAML. Requires Python 3, Graphviz, OpenJDK 10 or 11, PlantUML.

### OWASP Threat Dragon
Allows small teams to create threat models quickly and easily with simplicity, flexibility, and accessibility in mind. Threat Dragon can output models into diagrams for other applications. It can also export models into PDF reports which are GRC compliant.

## OWASP Cornucopia
A card game which may be played in various ways to play about an ecommerce system.
### References for Website Edition
- OWASP Application Security Verification Standard
- OWASP Secure Coding Practices quick reference guide
- OWASP AppSensor
- MITRE CAPEC
- SAFEcode
### References for Mobile App Edition
- OWASP Mobile Application Security Verification Standard (MASVS)
- OWASP Mobile Application Security Testing Guide (MASTG)
- MITRE CAPEC
- SAFEcode
## LINDDUN GO
- Helps identify potential privacy threats based on the key LINDDUN threats to privacy
- Linking
- Identifying
- Non-repudiation
- Detecting
- Data Disclosure
- Unawareness
- Non-compliance

### OWASP Threat Modeling Toolkit
## Web Application Checklist
```
4.2.1 Checklist: Define Security Requirements
4.2.1.1 System Configuration
4.2.1.2 Cryptographic Practices
4.2.1.3 File Management
4.2.2 Checklist: Leverage Security Frameworks and Libraries
4.2.2.1 Security Frameworks and Libraries
4.2.3 Checklist: Secure Database Access
4.2.4 Checklist: Encode and Escape Data
4.2.5 Checklist: Validate All Inputs
4.2.6 Checklist: Implement Digital Identity
4.2.7 Checklist: Enforce Access Controls
4.2.8 Checklist: Protect Data Everywhere
4.2.9 Checklist: Implement Security Logging and Monitoring
4.2.10 Checklist: Handle all Errors and Exceptions
```
- OWASP Top 10 Proactive Controls
- OWASP Java Encoder Project
- OWASP Java HTML Sanitizer Project
- OWASP Cheat Sheets
- OWASP Improper Error Handling
- OWASP Code Review Guide: Error handling
- OWASP  MAS Checklist 
- OWASP MASVS, MASTG, MAS, MAS Cheatsheet

# Implementation
## References
- OWASP Top 10 Proactive Controls
- Go Secure Coding Practices
- Cheatsheet Series
- ESAPI for Java
- ESAPI Documentation
- ESAPI project
- [Spring Security](https://docs.spring.io/spring-security/reference/features/index.html) 
- CSRFGuard
- OWASP Secure Headers Project
- OWASP MASWE
- MITRE CWE
- OWASP Go Secure Coding Practices Quick Reference Guide

# Verification
- Guides
	- WSTG
	- MASTG
	- ASVS
- Tools
	- DAST Tools
	- Amass
	- Kali Linux
	- OWTF
	- Nettacker
	- OSHP verification
- Frameworks
	- secureCodeBox
		- Container analysis
			- Trivy SBOM / Vulnerability Scan
		- CMS Analysis
			- CMSeeK for Joomla
			- Typo3Scan for Typo3 CMS
			- WPScan for  Wordpress
		- Kubernetes
			- Kube Hunter, Kubeaudit
		- Network
			- Amass, doggo DNS client, Ncrack, Nmap, Whatweb
		- Repository Analsys
			- Git Repo Scanner, Gitleaks, Semgrep
		- SSH/TLS policy scanning with SSH-audit and SSLyze
		- Web Application analysis
			- ffuf, Nikto, Nuclei vulnerability Scanner, Screenshooter
		- Helm package manager for Kubernetes
	- Vulnerability management
		- DefectDojo
		- We Hack Purple discussion
		- Threagile Threat Modeling

# Training and Verification
- Vulnerable Applications
	- OWASP Vulnerable Web Applications Directory Project
	- Juice Shop -> Node.js -> `Commonly run on Docker in the cloud and validated against OWASP Project 25`
	- WebGoat -> Java
		- Contains WebWolf an attacker client
	- PyGoat -> Python
	- Security Shepherd
- Secure Coding Dojo
	- SANS 25
	- MITRE Most Dangerous Software Errors
- SKF Education
- SamuraiWTF -> Dojo / Katana 
	- For learning container and instance security using the Samurai Web Training Framework
- OWASP WrongSecrets
- OWASP Top 10 Projects
```
What is the Mobile Top 10?

The Mobile Top 10 identifies and lists the top ten vulnerabilities found in 
mobile applications. These risks of application vulnerabilities have been 
determined by the project team from various sources including incident reports, 
vulnerability databases, and security assessments. The list has been built 
using a data-based approach from unbiased sources, an approach detailed in the 
repository read-me.

• M1: Improper Credential Usage
• M2: Inadequate Supply Chain Security
• M3: Insecure Authentication/Authorization
• M4: Insufficient Input/Output Validation
• M5: Insecure Communication
• M6: Inadequate Privacy Controls
• M7: Insufficient Binary Protections
• M8: Security Misconfiguration
• M9: Insecure Data Storage
• M10: Insufficient Cryptography

The project also provides a comprehensive list of security controls and techniques that should be applied to mobile applications to provide a minimum level of security:

1. Identify and protect sensitive data on the mobile device
2. Handle password credentials securely on the device
3. Ensure sensitive data is protected in transit
4. Implement user authentication,authorization and session management correctly
5. Keep the backend APIs (services) and the platform (server) secure
6. Secure data integration with third party services and applications
7. Pay specific attention to the collection and storage of consent for the collection and use of the user’s data
8. Implement controls to prevent unauthorized access to paid-for resources (wallet, SMS, phone calls etc)
9. Ensure secure distribution/provisioning of mobile applications
10. Carefully check any runtime interpretation of code for errors

The list of mobile controls has been created and maintained by a collaboration of OWASP and the European Network and Information Security Agency (ENISA) to build a joint set of controls
```
- OWASP Snakes and Ladders
- OWASP Proactive Controls 

# Security Culture and Process maturing
- SAMM Organization and Culture
- SAMM Education and Guidance 
- Security Champions
	- Security champions program
	- Security Champions Guide
	- Security Champions Playbook
- SAMM
- ASVS process
- MAS process
- SAMMY management tool
- OWASP SAMM Project
- MAS Crackmes reverse engineering challenges for mobile applications
# Operations
- DevSecOps Guideline
- Coraza WAF
- ModSecurity WAF
- OWASP CRS
```
• Static Application Security Testing (SAST)
• Dynamic Application Security Testing (DAST)
• Interactive Application Security Testing (IAST)
• Software Composition Analysis (SCA)
• Infrastructure Vulnerability Scanning
• Container Vulnerability Scanning
```
# Metrics
- OWASP Integration Standards project Application Wayfinder
# Gap Analysis
- SAMM Gap analysis
- ASVS gap analysis
- WSVS gap analysis?
- MAS gap analysis
- ISO 27001 Information Security, Cybersecurity and Privacy Protection

# Appendicies
- Implementation Do's and Don'ts 
- Container security
- Secure coding
- Cryptographic practices
- Application spoofing
- Content Security Policy (CSP)
- Exception and error handling
- File management
- Memory management
- Verification Do's and Don'ts 12.2.1 Secure environment
- 12.2.2 System Hardening
- 12.2.3 Open Source software
```
 Address vulnerabilities with: where source code sharing is a part of the license
– GitHub CodeQL / third party tool
– If within the budget of your organization, use an SCA tool to scan for vulnerabilities
...
 Maintaining open source software/components: Binaries / pre-compiled code / packages where source
code sharing is not a part of the license
– Monitor for deprecated packages
– Use dependency graphs
– Lock files
– Monitor vulnerabilities with:
∗ Check for vulnerabilities for the selected binaries in vulnerability disclosure databases like
· CVE database (https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=bouncy+castle)
· VulnDB (https://vuldb.com/?id.173918)
– If within the budget of your organization, use an SCA tool to scan for vulnerabilities
• Copying source code off public domain (internet) For example source code that is on a blog or in
discussion forums like stacktrace or snippets of example on writeups *******Don’t do it!!!*******
```