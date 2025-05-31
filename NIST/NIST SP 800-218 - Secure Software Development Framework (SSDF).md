# Reference Notes to SP 800-218
```
The SSDF defines only a high-level subset of what organizations may need to do, so
organizations should consult the references and other resources for additional information on
implementing the practices. Not all practices are applicable to all use cases; organizations should
adopt a risk-based approach to determine what practices are relevant, appropriate, and effective
to mitigate the threats to their software development practices.

Organizations can communicate how they are addressing the clauses from Section 4 of the
President’s Executive Order (EO) on “Improving the Nation’s Cybersecurity (14028)” by
referencing the SSDF practices and tasks described in Appendix A.
```

### EO 14028 § 4 
- Emphasizes securing software security, supply chain and critical software
- Notes that the National Institute of Standards and Technology will publish documents pertaining to the standards

### [Documents from NIST](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity)
- Supply Chain Risk Management
- IoT Security and Labeling
- Consumer IoT and Software
- Guidelines for Enhancing Software Supply Chain Security

## Introduction

- Software Development Life Cycle 
- NIST CSF
- SAFECode
- Microsoft SDL

### SAFECode Fundamentals
```
• Design
  • Secure Design Principles
  • Threat Modeling
  • Perform Architectural and Design Reviews
  • Develop an Encryption Strategy
  • Standardize Identity and Access Management
  • Establish Log Requirements and Audit Practices
• Secure Coding Practices
  • Establish Coding Standards and Conventions
  • Use Safe Functions Only
  • Use Current Compiler and Toolchain Versions and Secure Compiler Options
  • Use Code Analysis Tools To Find Security Issues Early
  • Handle Data Safely
  • Handle Errors
• Manage Security Risk Inherent in the Use of Third-party Components
• Manual Testing
  • Perform Manual Verification of Security Features/Mitigations
  • Perform Penetration Testing
• Automated Testing
  • Use Static Analysis Security Testing Tools
  • Perform Dynamic Analysis Security Testing
  • Fuzz Parsers
  • Network Vulnerability Scanning
  • Verify Secure Configurations and Use of Platform Mitigations
  • Perform Automated Functional Testing of Security Features/Mitigations
• Manage Security Findings
  • Define Severity
  • Risk Acceptance Process
• Vulnerability Response and Disclosure
  • Define Internal and External Policies
  • Define Roles and Responsibilities
  • Ensure that Vulnerability Reporters Know Who to Contact
  • Manage Vulnerability Reporters
  • Monitor and Manage Third-party Component Vulnerabilities
  • Fix the Vulnerability
  • Identify Mitigating Factors or Workarounds
  • Vulnerability Disclosure
  • Secure Development Lifecycle Feedback
```

## Practice Groups
```
1. Prepare the Organization (PO): Organizations should ensure that their people,
processes, and technology are prepared to perform secure software development at the
organization level. Many organizations will find some PO practices to also be applicable
to subsets of their software development, like individual development groups or projects.

2. Protect the Software (PS): Organizations should protect all components of their
software from tampering and unauthorized access.

3. Produce Well-Secured Software (PW): Organizations should produce well-secured
software with minimal security vulnerabilities in its releases.

4. Respond to Vulnerabilities (RV): Organizations should identify residual vulnerabilities
in their software releases and respond appropriately to address those vulnerabilities and
prevent similar ones from occurring in the future
```