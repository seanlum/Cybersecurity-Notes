# NIST Cyber Security Framework 
https://www.nist.gov/cyberframework

# Development Note (personal)
I'm working on a data format that can be easily edited and also exported to XSLX, I may write a Python PoC converter. I might also implement it with NodeJS and React considering it is JSON and the schema of the JSON object could easily be implemented in GraphQL.

### [My CSF Viewer HTML](./files/csf-driver.html)
### [My CSF Viewer server](./files/server.ps1)
### [My CSF Viewer flat text export](./files/CSF-flat-text-export.txt)
### [NIST CSF 2.0 JSON Export from the CSF Viewer](./files/csf-export.json)

# Begin Document


[my experimental NIST CSF JSON format (wip)](./files/csf-draft.json)

# Links
- [NIST CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29)
- [NIST CSF 2.0 Resource & Overview Guide](https://doi.org/10.6028/NIST.SP.1299)
- [Small Business (SMB) Quick Start Guide](https://doi.org/10.6028/NIST.SP.1300)
- [Creating and Using Organizational Profiles](https://doi.org/10.6028/NIST.SP.1301)
- [Using the CSF Tiers](https://doi.org/10.6028/NIST.SP.1302.ipd)
- [Draft Cybersecurity Supply Chain Risk management (C-SCRM)](https://doi.org/10.6028/NIST.SP.1305.ipd)
- [Draft Enterprise Risk Management (ERM) Practicioners](https://doi.org/10.6028/NIST.SP.1303.ipd)

The NIST CSF was designed to help organizations of all sizes and sectors to help reduce risk. It can be implemented regardless of the maturity level and technical sophistication level of the organization's capabilities. It does not use a one-size fits all approach, and implementations vary.

The document is mainly aimed at people in the following industries: financial, privacy, supply chain, repuational, technological, or physical in nature.

# Overview
The CSF 2.0 is organized by six functions -- `Govern`, `Identify`, `Protect`, `Detect`, `Respond`, and `Recover`. 

The CSF has the three following components:
- CSF Core
- CSF Organizational Profiles
- CSF Tiers

# CSF Core
## Core Functions
### Govern (GV)
```
The organization’s cybersecurity risk management strategy, expectations, and policy are established, communicated, and monitored. The GOVERN Function provides outcomes to inform what an organization may do to achieve and prioritize the outcomes of the other five Functions in the context of its mission and stakeholder expectations. Governance activities are critical for incorporating cybersecurity into an organization’s broader enterprise risk management (ERM) strategy. GOVERN addresses an understanding of organizational context; the establishment of cybersecurity strategy and cybersecurity supply chain risk management; roles, responsibilities, and authorities; policy; and the oversight of cybersecurity strategy
```

### Identify (ID)
```
IDENTIFY (ID) — The organization’s current cybersecurity risks are understood. Understanding the organization’s assets (e.g., data, hardware, software, systems, facilities, services, people), suppliers, and related cybersecurity risks enables an organization to prioritize its efforts consistent with its risk management strategy and the mission needs identified under GOVERN. This Function also includes the identification of improvement opportunities for the organization’s policies, plans, processes, procedures, and practices that support cybersecurity risk management to inform efforts under all six Functions.
```

### Protect (PR)
```
Safeguards to manage the organization’s cybersecurity risks are used.
Once assets and risks are identified and prioritized, PROTECT supports the ability to secure those assets to prevent or lower the likelihood and impact of adverse cybersecurity events, as well as to increase the likelihood and impact of taking advantage of opportunities. Outcomes covered by this Function include identity management, authentication, and access control; awareness and training; data security; platform security (i.e., securing the hardware, software, and services of physical and virtual platforms); and the resilience of technology infrastructure.
```

### Detect (DE)
```
Possible cybersecurity attacks and compromises are found and analyzed. DETECT enables the timely discovery and analysis of anomalies, indicators of compromise, and other potentially adverse events that may indicate that cybersecurity attacks and incidents are occurring. This Function supports successful incident response and recovery activities.
```

### Respond (RS)
```
Actions regarding a detected cybersecurity incident are taken. RESPOND supports the ability to contain the effects of cybersecurity incidents. Outcomes within this Function cover incident management, analysis, mitigation, reporting, and communication.
```

### Recover (RC)
```
Assets and operations affected by a cybersecurity incident are restored. RECOVER supports the timely restoration of normal operations to reduce the effects of cybersecurity incidents and enable appropriate communication during recovery efforts.
```

## CSF Categories
- [CSF 2.0 Example Profile](https://www.nist.gov/document/csf-20-implementation-examples-xlsx)
- [CSF 2.0 Reference Tool](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/CSF_2_0_0/home?element=all)
- [CSF 2.0 Core Legacy Format Example](https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=)

Organizational profiles define the complete set of defined policy related to the core CSF functions of `Govern`, `Identify`, `Protect`, `Detect`, `Respond`, and `Recover`. Each Function has between two to six categories, and each of them have an identifier.

### Govern (GV) Categories
| Category | Category ID |
|-|-|
| Organizational Context | GV.OC |
| Risk Management Strategy | GV.RM |
| Roles, Responsibilities, and Authorities | GV.RR |
| Policy | GV.PO |
| Oversight | GV.OV |
| Cybersecurity Supply Chain Risk Management | GV.SC |

### Identify (ID) Categories
| Category | Category ID |
|-|-|
| Asset Management | ID.AM |
| Risk Assessment | ID.RA |
| Improvement | ID.IM |


### Protect (PR) Categories
| Category | Category ID |
|-|-|
| Identity Management, Authentication, and Access Control | PR.AA |
| Awareness and Training | PR.AT |
| Data Security | PR.DS |
| Platform Security | PR.PS |
| Technology Infrastructure Resilience | PR.IR |

## CSF Core
For a complete description of each function category rule, check out [NIST CSF 2.0, Appendix A. CSF Core, Page 21 of 32](https://doi.org/10.6028/NIST.CSWP.29) 

## CSF Tiers
There are four tiers within the CSF: `Partial`, `Risk Informed`, `Repeatable`, `Adaptive`
For a complete description of each CSF Tier check out [NIST CSF 2.0, Appendix B. CSF Tiers, Page 29 of 32](https://doi.org/10.6028/NIST.CSWP.29)


# Reference Documents

## ChatGPT suggested reading order for NIST Documents
### First read NIST CSF
```
NIST CSF (1.1 or 2.0)
  -	Purpose: Understand the overall structure, core functions, categories, and subcategories of the CSF.
  -	Focus: Familiarize yourself with the Identify, Protect, Detect, Respond, Recover, and (in 2.0) Govern functions.
```
1.	NIST SP 800-39: Managing Information Security Risk
    -	Purpose: Provides an overarching framework for managing information security risk at the organizational, mission, and information system levels.
    -	Focus: Establishes the context for risk management and integrates it into the organization’s overall risk management strategy.
2.	NIST SP 800-30: Guide for Conducting Risk Assessments
    -	Purpose: Offers detailed guidance on conducting risk assessments, which are a critical component of the risk management process.
    -	Focus: Describes the risk assessment process, including preparation, execution, and maintenance.
3.	NIST SP 800-37: Risk Management Framework (RMF) for Information Systems and Organizations
    -	Purpose: Provides a structured process for integrating security and risk management activities into the system development life cycle.
    -	Focus: Details the steps in the RMF, including categorization, selection, implementation, assessment, authorization, and continuous monitoring.
4.	NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations
    -	Purpose: Lists security and privacy controls that can be applied to information systems to protect organizational operations, assets, and individuals.
    -	Focus: Provides a comprehensive catalog of controls that align with the CSF categories and subcategories.
5.	NIST SP 800-60: Guide for Mapping Types of Information and Information Systems to Security Categories
    -	Purpose: Helps organizations categorize information and information systems based on impact levels.
    -	Focus: Provides guidelines for mapping information types to security categories, which is essential for implementing appropriate security controls.
6.	NIST SP 800-61: Computer Security Incident Handling Guide
    -	Purpose: Offers guidance on handling and responding to cybersecurity incidents.
    -	Focus: Describes the incident response lifecycle, including preparation, detection, analysis, containment, eradication, and recovery.
7.	NIST SP 800-207: Zero Trust Architecture
    -	Purpose: Introduces the principles and implementation of a Zero Trust Architecture, which is a modern approach to cybersecurity.
    -	Focus: Explains Zero Trust concepts, logical components, and deployment models, emphasizing the need for continuous verification of user and device trustworthiness.
### Summary of Reading Order
1.	NIST SP 800-39: Managing Information Security Risk
2.	NIST SP 800-30: Guide for Conducting Risk Assessments
3.	NIST SP 800-37: Risk Management Framework (RMF) for Information Systems and Organizations
4.	NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations
5.	NIST SP 800-60: Guide for Mapping Types of Information and Information Systems to Security Categories
6.	NIST SP 800-61: Computer Security Incident Handling Guide
7.	NIST SP 800-207: Zero Trust Architecture

## Suggested Reading NIST Documents

### 1.	NIST SP 800-30: Guide for Conducting Risk Assessments
-	Purpose: Provides guidance on conducting risk assessments, which is a critical component of the risk management process.
-	Usage: Helps identify, estimate, and prioritize risks to organizational operations, assets, individuals, and other organizations.
### 2.	NIST SP 800-39: Managing Information Security Risk: Organization, Mission, and Information System View
-	Purpose: Provides a structured approach to managing information security risk at the organizational, mission, and information system levels.
-	Usage: Helps integrate risk management into the organization’s overall governance structure.
### 3.	NIST SP 800-61: Computer Security Incident Handling Guide
-	Purpose: Provides guidelines for incident handling, including preparation, detection, analysis, containment, eradication, and recovery.
-	Usage: Helps establish and improve incident response capabilities.
### 4.	NIST SP 800-88: Guidelines for Media Sanitization
-	Purpose: Provides guidelines for the sanitization of data storage media to ensure that sensitive information is properly destroyed.
-	Usage: Helps ensure that data is irretrievably deleted from storage media before disposal or reuse.
### 5.	NIST SP 800-115: Technical Guide to Information Security Testing and Assessment
-	Purpose: Provides guidelines for planning and conducting technical information security testing and assessments.
-	Usage: Helps identify vulnerabilities and assess the effectiveness of security controls.
### 6.	NIST SP 800-160: Systems Security Engineering: Considerations for a Multidisciplinary Approach in the Engineering of Trustworthy Secure Systems
-	Purpose: Provides guidelines for integrating security into the engineering of systems.
-	Usage: Helps ensure that security is considered throughout the system development lifecycle.
### 7.	NIST SP 800-171A: Assessing Security Requirements for Controlled Unclassified Information
-	Purpose: Provides assessment procedures for the security requirements in NIST SP 800-171.
-	Usage: Helps assess the implementation of security requirements for protecting controlled unclassified information (CUI).
### 8.	NIST SP 800-184: Guide for Cybersecurity Event Recovery
-	Purpose: Provides guidance on recovering from cybersecurity incidents.
-	Usage: Helps develop and implement recovery plans to restore normal operations after a cybersecurity event.
### 9.	NIST SP 800-207: Zero Trust Architecture
-	Purpose: Provides guidelines for implementing a Zero Trust Architecture (ZTA).
-	Usage: Helps design and deploy a security architecture that assumes no implicit trust and continuously verifies every request.

## Other frameworks and things that can integrate with the NIST CSF
### 1.	ITIL (Information Technology Infrastructure Library)
-	Purpose: Provides best practices for IT service management (ITSM).
-	Usage: Focuses on aligning IT services with the needs of the business and improving service delivery. ITIL practices can complement NIST CSF by enhancing service management processes.
### 2.	CIS Controls (Center for Internet Security Controls)
-	Purpose: Provides a prioritized set of actions to protect organizations from cyber threats.
-	Usage: Offers practical and actionable guidelines that can be mapped to NIST CSF categories and subcategories to enhance security controls.
### 3.	PCI DSS (Payment Card Industry Data Security Standard)
-	Purpose: Provides security standards for organizations that handle credit card transactions.
-	Usage: Ensures the protection of cardholder data and can be referenced in a NIST CSF profile for organizations involved in payment processing.
### 4.	GDPR (General Data Protection Regulation)
-	Purpose: Provides regulations for data protection and privacy for individuals within the European Union.
-	Usage: Ensures compliance with data protection laws and can be integrated into a NIST CSF profile for organizations handling personal data of EU citizens.
### 5.	HIPAA (Health Insurance Portability and Accountability Act)
-	Purpose: Provides regulations for protecting sensitive patient health information.
-	Usage: Ensures compliance with healthcare data protection requirements and can be referenced in a NIST CSF profile for healthcare organizations.
### 6.	SOX (Sarbanes-Oxley Act)
-	Purpose: Provides regulations for financial reporting and internal controls.
-	Usage: Ensures compliance with financial reporting requirements and can be integrated into a NIST CSF profile for publicly traded companies.
### 7.	FISMA (Federal Information Security Management Act)
-	Purpose: Provides a framework for managing information security for federal agencies.
-	Usage: Ensures compliance with federal information security requirements and can be referenced in a NIST CSF profile for federal contractors and agencies.
### 8.	CSA CCM (Cloud Security Alliance Cloud Controls Matrix)
-	Purpose: Provides a cybersecurity control framework for cloud computing.
-	Usage: Ensures the security of cloud environments and can be integrated into a NIST CSF profile for organizations using cloud services.