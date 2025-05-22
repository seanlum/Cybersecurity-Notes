# PASTA - Process for Attack Simulation and Threat Analysis
- https://threat-modeling.com/pasta-threat-modeling/
- https://redrays.io/blog/threat-modeling-an-overview-of-pasta-methodology/

## Threat Modeling Cheat Sheet from OWASP
https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html

# Steps of Pasta

## 1. Objective Definition
Scoping the objective is very important. Major objective can include
- General business requirements for modeled objects
- Functional requirements
- Information security requirements (policies and baselines)
- Compliance and Regulatory Requirements (frameworks and standards)
- Data classification and asset scoping
- Define what needs to be protected
- Define what needs to be inspected
- Identify involved assets
    - Networks, Databases, Components
    - Systems, VMs, Containers, Environments
    - Tools, Encryption Standards, Protocols

## 2. System Decomposition
- Identify structure of data testing
- Network Flow
- Data Flow
- Component Layout
- Process Flow

## 3. Threat Agent Identification
- Perform vulnerability assessment
- Identify affected surface area from the flows
- Identify potential adversaries and TTPs which may be used against the system
- Identify what threats may be most likely to occur
- Identify what protections and safeguards are also in place
- Identify how these protections and threats may affect system stability if exploited
- Identify threat models

## 4. Threat Analysis
- Do SCA, DCA, MCA
    - Static Code Analysis
    - Dynamic Code Analysis
    - Manual Code Analysis
- Do SBOM (Software Bill of Materials)

## 5. Vulnerability Identification
- After threats and potential vulnerabilities have been identified
- Validate which vulnerabilities which are exploitable
- Identify potential vulnerability chains which may lead to compromise 
- Perform vulnerability analysis

## 6. Analyze and Model Attacks
Do SAST, DAST, MAST
    - Static Application Security Testing
    - Dynamic Application Security Testing
    - Manal Applcation Security Testing
- Perform threat modeling implementation and testing 

## 7. Risk/impact analysis and development of countermeasures
- Collect results from scans and testing
- Identify potential risks and impacts on business systems
- Perform Business Impact Analysis
- Identify and project who may be affacted by the potential attacks
- Place countermeasures within the systems 
- Perform risk reduction, minimize risk
- Reduce attack surface area