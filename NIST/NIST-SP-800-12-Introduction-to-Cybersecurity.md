# An Introduction to Security
- high level overview of information security principles
- high level overview of some control families from SP 800-53

## Organization
- introduction
- eight major elements regarding information security
- several roles and respective responsibilities and what those people do within an organization
- threats versus vulnerabilities
- information security policy and the differences between Program Policy, Issue-Specific Policy, and System-Specific Policy
- six steps of the NIST Risk Management Framework (RMF)
- information assurance overview
- systems support and operations overview
- cryptography overview

## Foundation Documents
- Computer Security Act of 1987
- Federal Information Resource Mangagement Regulation (FIRMR)
  - Information Technology Management Reform Act of 1996 (ITMRA)
    - Clinger-Cohen Act
- E-Government Act of 2002
- Federal Information Security Management Act (FISMA)
- Federal Information Security Management Act of 2014
- OMB Circular A-130

# Elements of Information Security
- Its critical to understand the organizational mission and how each system supports that mission.
- Its also critical to define security requirements and roles for systems
  - Security can then explicity stated in terms of the 
  organizations mission

### Determining the impact level of a system
- FIPS 199
- NIST SP 800-30
- NIST SP 800-60

### Security Controls
- NIST SP 800-53
- there is no such thing as a perfect security solution, each security solution must be tailored to the organization adopting the security practices

### Information security roles and responsibilities
Understanding the roles and responsibilities which may be required within an organization to facilitate various processes defined by a standard is mission critical, especially in terms of compliance.

- NIST SP 800-37
  - Appendix D

### An integrated approach
- The document mentions using `Defense in Depth`, yet this may conflict with how Zero Trust architecture works.

### Security Systems Engineering
Information systems have many various processes which involve engineering and adopting lifecycles within other lifecycles inside an organization. This document focuses on the responsibilities of a Security Systems Engineer.
- NIST SP 800-160

### Supply Chain Risk Management
- NIST SP 800-161

### Information Security Continuous Monitoring (ISCM)
- NIST SP 800-137

### Assessing Security Controls
- NIST SP 800-53A

### Introduction to Privacy Engineering and Risk Management in Federal Systems
- NISTIR 8062

### Guide to Protecting the Confidentiality of Peronally Identifiable Information
- NIST SP 800-122

# Roles and Responsibilities
- Risk Executive Functions (Senior Management) define the controls, and needs for controls that will be implemented by the CEO.


## Risk Executive Function (Senior Management)
- Handling the high level components of the risk management strategy
- They help implement the risk management framework for the organization
- Defines risk strategy
- Supports and possibly establishes information-sharing amongst authorizing officials and senior leaders within the organization.

### NIST Glossary
- [NIST Glossary: Executive Agency](https://csrc.nist.gov/glossary/term/executive_agency)

## Chief Executive Officer (CEO)

The CEO is largely responsible for implementing and integrating the risk management strategy that is defined by senior management. They also help implement the policies defined by senior management.

- They help with addressing concerns compliance
- helping legal requirements for the organizations
- They help implement SPPPs for incident response, risk management, requirements for resources for IR and RM programs,   privacy, business continuity, and continuous monitoring

#### AI Generated content
- [Copilot, Google Search, and Gemini](./AI-Content/CEO-Copilot-GoogleSearch-Gemini.md)
- [ChatGPT](./AI-Content/CEO_responsibilities_NIST-ChatGPT.md)
#### Written articles
- [Investopedia Description of a CEO](https://www.investopedia.com/terms/c/ceo.asp)
- [Corporate Finance Institute, Description of a CEO](https://corporatefinanceinstitute.com/resources/career/what-is-a-ceo-chief-executive-officer/)
- [CEO Worldwide, the role of the CEO in cyber security](https://www.ceo-worldwide.com/blog/the-role-of-the-ceo-in-cyber-security/)

## Chief Information Officer (CIO)

The chief information officer is mainly tasked with:
- designating a CISO
- developing and maintaining security SPPPs to address requirements set by the CEOs SPPPs
- overseeing significant information security responsibilities
- assisting senior organizational officials with their responsibilities
- reporting the effectiveness of the organization's information security program

### NIST information on CIO
- [NIST Glossary: Chief Information Officer](https://csrc.nist.gov/glossary/term/chief_information_officer)
- [NIST Glossary: CIO Council](https://csrc.nist.gov/glossary/term/chief_information_officers_cio_council)

### AI Generated content related to CIO and NIST
- [CIO Responsibilities NIST - ChatGPT](./AI-Content/CIO_responsibilities_NIST-ChatGPT.md)
- [CIO Responsibilities NIST - GitHub Copilot](./AI-Content/CIO_responsibilities_NIST-GitHub-Copilot.md)



## Information Owner/Steward
- Official with statutory or operational authority for specified information and responsibility for establishing the controls for its generation, classification, collection, processing, dissemination, and disposal.
  - <a href="https://doi.org/10.6028/NIST.SP.800-30r1" id="term-def-src-link-1-0">NIST SP 800-30 Rev. 1</a> under Information Owner
  - <a href="https://doi.org/10.6028/NIST.SP.800-39" id="term-def-src-link-1-1">NIST SP 800-39</a> under Information Owner </span>from <span id="term-def-src-src-link-1-1-0">CNSSI 4009</span>
- Official with statutory or operational authority for specified information and responsibility for establishing the controls for its generation, classification, collection, processing, dissemination, and disposal. See information steward. Note: Information steward is a related term, but it is not identical to information owner.
  - [CNSSI 4009-2015](https://www.cnss.gov/CNSS/issuances/Instructions.cfm) from [FIPS 200](https://doi.org/10.6028/NIST.FIPS.200)

### NIST Glossary information
- [NIST Glossary for Information Owner](https://csrc.nist.gov/glossary/term/information_owner)
- [NIST Glossary for Information System Owner](https://csrc.nist.gov/glossary/term/information_system_owner)


## Senior Agency Information Security Officer - (SAISO)
- Also known as CISO (Chief Information Security Officer)
- The SAISO is responsible for
  - FISMA responsbilities for CISO
  - liason between the chief information officer and the organization's authorizing officials, system owners, common control providers, and system security officers.
  - managing and implementing and organizing the information security program
  - act as a security authorizer or control assessor when needed.

### NIST Content
- [NIST Glossary for SAISO](https://csrc.nist.gov/glossary/term/senior_agency_information_security_officer)
- [NIST Glossary for CISO](https://csrc.nist.gov/glossary/term/chief_information_security_officer)
- [NIST Glossary for SISO](https://csrc.nist.gov/glossary/term/senior_information_security_officer)

### AI Generated Content
- [SAISO Responsibilities - ChatGPT](./AI-Content/SAISO-Responsibilities-ChatGPT.md)
- [SAISO Responsibilities - Github Copilot](./AI-Content/SAISO-Responsibilities-Github-Copilot.md)

## Authorizing Official
Official with the authority to formally assume responsibility for operating an information system at an acceptable level of risk to agency operations (including mission, functions, image, or reputation), agency assets, or individuals.

### NIST information
- [NIST Glossary for Authorizing Official](https://csrc.nist.gov/glossary/term/authorizing_official)

## Authorizing Official Designated Representative
The Authorizing Official Designated Representative is an organizational official who acts on behalf of an authorizing official to coordinate and conduct the required day-to-day activities associated by the security authorization process. The designated representative carries out the functions of the AO, but cannot accept risk for the system.

Responsibilities include, but are not limited to:
- Carrying out the duties of the Authorizing Official as assigned;
- Making decisions with regard to planning and resourcing of the security authorization
process, approval of the security plan, approving and monitoring the implementation of
plans of action and milestones, and the assessment and/or determination of risk; and
- Preparing the final authorization package, obtaining the authorizing official’s signature
on the authorization decision document, and transmitting the authorization package to
appropriate organizational officials

### NIST Information
- [NIST Glossary for Authorizing Official Designated Representative](https://csrc.nist.gov/glossary/term/authorizing_official_designated_representative)

## Senior Agency Official for Privacy

- Responsible for the agency's implementation of information privacy protection
- including the ageancy's full compliance with federal laws, reglations, and policies relating to information privacy, such as the Privacy Act.

### NIST Glossary Information
- [SAOP Definition](https://csrc.nist.gov/glossary/term/senior_agency_official_for_privacy)

## Common Control Provider
An organizational official responsible for the development, implementation, assessment, and monitoring of common controls (i.e., security controls inherited by information systems).

### Responsibilities example
- Documenting the organization-identified common controls in a security plan
- Common controls must be assessed with an appropriate level of independence, and also by people with proper qualifications

### Examples
- Internal IT Departments
  - IT Security Teams - responsible for implementing and managing security controls
  - Network Operations Centers (NOCs) - which manage security controls including VPNs, network segmentation, and monitoring.
- Cloud Service Providers (CSPs)
- Managed Security Service Providers (MSSPs)
- Government Agencies
  - Department of Homeland Security (DHS) - e.g. security controls and guidelines through initiatives like the Continuous Diagnostics and Mitigation (CDM) Program
  - National Institute of Standards and Technology
- Security Solution Providers - Companies which provide full security solutions like Cisco, Palo Alto Networks, and Fortinet

### NIST Glossary Information
- [common control provider definition](https://csrc.nist.gov/glossary/term/common_control_provider)

## System Owner
- The organizational official responsible for  the procurement, development, integration, modification, operation, maintenance, and disposal of a system.

### Responsibilities example
- Ensuring compliance with information security systems
- Developing and maintaining the system security plan and ensuring that the deployed system is operated upon in agreement with the implemented security controls.
- Helping users satisfy mission, business, or operational requirements of the product. 

### NIST Glossary Information
- [system owner definition](https://csrc.nist.gov/glossary/term/system_owner)
- [system owner (or program manager)](https://csrc.nist.gov/glossary/term/system_owner_or_program_manager)

## System Security Officer
-  responsible that proper operational security posture is maintained for a system
- works closely with the system owner

### Responsibilities example
- Overseeing routine `security operations` of a system
- Helps define and ensure compliance with SPPPs related to security

### NIST Glossary Information
- [system security officer](https://csrc.nist.gov/glossary/term/system_security_officer)
- [Information System Security Officer (ISSO)](https://csrc.nist.gov/glossary/term/isso)
- [systems security officer](https://csrc.nist.gov/glossary/term/systems_security_officer)

## Information Security Architect
```
 Individual, group, or organization responsible for ensuring that the information security requirements necessary to protect the organization’s core missions and business processes are adequately addressed in all aspects of enterprise architecture including reference models, segment and solution architectures, and the resulting information systems supporting those missions and business processes.
```

### Responsibilities example

- `Liason` between the `enterprise architect` and the `information security engineer`;
- Coordinating with `system owners`, `common control providers`, and `system security officers` on the allocation of `security controls` as system-specific, hybrid, or common controls.

### NIST Glossary Information
- [information security architect](https://csrc.nist.gov/glossary/term/information_security_architect)

## System Security Engineer (SSE)
The `System Security Engineer` is an individual, group, or organization responsible for conducting `system security engineering activities`

```
Responsibilities include, but are not limited to:
  • Designing and developing organizational systems or upgrading legacy systems; and
  • Coordinating security-related activities with information security architects, senior agency information security officers, system owners, common control providers, and system security officers
```

### An Example of Systems Security Engineering in Action
- [NIST SP 1800-24B](https://csrc.nist.gov/pubs/sp/1800/24/final)

### Engineering Trustworthy Secure Systems
- [NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final)
- [NIST SP 800-160v1r1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)


### NIST Glossary Information
- [SSE](https://csrc.nist.gov/glossary/term/sse)
- [System Security Engineer](https://csrc.nist.gov/glossary/term/system_security_engineer)

## Security Control Assessor
This definition under the glossary has some variations. This may also be known as a penetration tester in the cybersecurity world.
```
The individual, group, or organization responsible for conducting a security control assessment.
```
A Security Control Assessor may conduct a comprehensive assessment of various controls within the organization; such as managerial, operational, technical security controls and the degree to which these controls are implemented according to the requirements of the organization.

### Example Responsibility
A Security Control Assessor may identify vulnerabilities within a system and its operating environment; disseminate vulnerability remediation consultation to the organization; prepare and disseminate a securty assessment report notarizing the assessment and its findings.

### NIST Glossary Information
- [security control assessor](https://csrc.nist.gov/glossary/term/security_control_assessor)

## System Administrator (SA) 

A system administrator can have many roles within an environment; and may involve key points of the asset management lifecycle. This typically involves providing and maintaining access to systems for users and programs. They may also be involved with the `information assurance policies`

### Responsibilities

- creating, maintaining, retiring user accounts and resources for users in a computer system
- Running system backups and performing data recovery operations
- Installing and configuring programs for general use
- Implementing information security controls

### NIST Glossary
- [System Administrator (SA)](https://csrc.nist.gov/glossary/term/system_administrator)

## User

A user has more definitions than a system administrator. More or less it is a type of role inside of a system, whether computerized or not, which pertains to one under an administrator's governance.

### NIST Glossary
- [user](https://csrc.nist.gov/glossary/term/user)

## Supporting Roles

- Auditor
- Physical Security Staff
- Disaster Recovery/Contingency Planning Staff
- Quality Assurance Staff
- Procurement Office Staff
- Training Office Staff
- Human Resources
- Risk Management/Planning Staff
- Physical Plant Staff
- Privacy Office Staff

# Threats and Vulnerabilities

This section is mainly examples and does not go in complete detail on every type of cybersecurity threat, vulnerability, risk, response, or safeguard selection.

For more information on threat sources and threat events, see [NIST SP 800-30](https://csrc.nist.gov/pubs/sp/800/30/r1/final)

NIST SP 800-30 mostly uses MITRE CAPEC for unclassified enumeration patterns. Today there is also ATT&CK and D3FEND.

## Examples of Adversarial Threat Sources and Events

### Fraud and Theft

Fraud and theft may be automated for financial gain for various reasons and can be identified through various risk management procedures as well as illegal activities.

Criminals may gain access to resources via: 
- Social Media (Phishing)
- Social Engineering (Spear Phishing)
- Advanced Persistent Threat (Malware Access Broker)

### Insider Threat

An example of an insider threat is employee sabotage

- Employee Sabotage may include but is not limited to
  - Destroying hardware or facilities
  - Planting malicious code that destroys programs or data
  - Modifying, Disrupting, Corrupting, Deleting data
  - Crashing systems, DDoSing systems
  - Denying access through various methods such as changing passwords

### Malicious Hacker

There are multiple types of malicious hackers, and some of the ones listed by this document are:

ChatGPT says that most of the malicious hacker groups are inherited from MITRE ATT&CK.

- Attackers
- Bot-Network Operators
- Criminal Groups
- Foreign Intelligence Services
- Phishers
- Spammers
- Spyware/Malicious Code Authors
- Terrorists
- Industrial Spies

### Malicious Code

Malicious code refers to viruses, Trojan horses, worms, logic bombs, and any other software created for the purpose of attacking a platform. 

- Trojan Horse
- Worm
- Logic Bomb
- Ransomware 

Other examples may include:
- Spyware
- Virus
- Destructive Malware
- Infostealer
- Remote Access Terminal (RAT)
- Backdoor
- DDoS Botnet
- Malware Botnet

## Examples of Non-Adversarial Threat Sources and Events

### Errors and Omissions
Errors of many kinds can occur within a computer system. Errors may go undetected if not checked for. Errors may also cause vulnerabilities and even crashes. Error detection through log analysis, machine learning models, EDR tools, and MDR processes can help bring insight to an organization. 

### Loss of Physical and Infrastructure Support
Loss of infrastructure support can cause all kinds of issues with life support. For example with the "Icey Goop" attack in Ukraine in 2024; which was a cyberattack on Ukrainian power infrastructure by Russia during Winter of 2024. This attack had casualties.

### Impacts to Personal Privacy of Information Sharing
Sharing PII with websites of any kind should always be done with discretion. Giving information to the public can result in possible blackmail for example.

# Information Security Policy

They list relevance to NIST SP 800-95, Guide to Secure Web Services, as an implementation of information security policy. 

Information security policy is largely defined by the needs of the organization in the way that it manages, protects, and distributes information. 

The document also talks about how NIST SP 800-53 has it's "-1" controls which designate that each of the 20 control families within SP 800-53 must have defined policies.

## Standards, Guidelines, and Procedures

### Organizational Standards
May define how a technology is used, or how a function is performed. They may define many aspects of responsibilities and how certain scenarios are handled. Standards are normally compulsory within an organization.

### Guidelines

Guidelines are improvements or instructions to improve the results of a task or practice. They are generally not required by law or organizational grading, but they can ultimately improve how a resource or system is utilized.

### Procedures

A procedure is a set of instructions on how to implement a process related to security policies, standards, and guidelines. They ultimately help an organization maintain compliance and get repeatable results for a business requirement.

## Program Policy

```
Program policy is used to create an organization’s information security program. Program policies set the strategic direction for security and assign resources for its implementation within the organization. A management official—typically the SISO—issues program policy to establish or restructure the organization’s information security program. This high-level policy defines the purpose of the program and its scope within the organization, addresses compliance issues, and assigns responsibility to the information security organization for direct program implementation as well as other related responsibilities
```

The definition for policy is [here](https://csrc.nist.gov/glossary/term/policy)

```
  Statements, rules or assertions that specify the correct or expected behavior of an entity. For example, an authorization policy might specify the correct access control rules for a software component.
```

The definition for a [security program plan](https://csrc.nist.gov/glossary/term/information_security_program_plan)

```
Formal document that provides an overview of the security requirements for an organization-wide information security program and describes the program management controls and common controls in place or planned for meeting those requirements.
```

The definition for a security program or [IT Security program](https://csrc.nist.gov/glossary/term/it_security_program):

```
a program established, implemented, and maintained to assure thatadequate IT security is provided for all organizational information collected, processed, transmitted, stored, or disseminated in its information technology systems. Synonymous with Automated Information System Security Program, Computer Security Program, and Information Systems Security Program.
```

The `policies` of a `security program plan` within an `IT Security program` largely define the `scope`, `purpose`, and `responsibilities`, `roles`, and overall `objectives` of an `IT Security program`