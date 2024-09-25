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