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
