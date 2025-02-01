# Matricies
ATT&CK matrices organize TTPs into a visual representation, with tactics as columns and techniques as rows. There are different matrices for various environments:
- Enterprise
- Mobile
- ICS Industrial Control System
- Cloud

# Data Sources
Data sources in ATT&CK describe the types of data that can be collected to detect and analyze techniques. Examples include:

- Process Monitoring
- Network Traffic Analysis
- File Monitoring

# TTPs Tactics Techniques and Procedures

TTPs in MITRE ATT&CK refer to "Tactics, Techniques, and Procedures," which are core components used to categorize and describe the behavior of adversaries. The MITRE ATT&CK framework provides a comprehensive matrix that details these components to help cybersecurity professionals understand, detect, and respond to threats.

# Tactics
Tactics represent the "why" of an adversary's actions. They are the adversary's technical goals during an attack. The tactics in the MITRE ATT&CK framework include:

1. Initial Access: How adversaries gain initial foothold within a network.
2. Execution: How adversaries run malicious code.
3. Persistence: How adversaries maintain their foothold.
4. Privilege Escalation: How adversaries gain higher-level permissions.
5. Defense Evasion: How adversaries avoid detection.
6. Credential Access: How adversaries steal credentials.
7. Discovery: How adversaries gather information.
8. Lateral Movement: How adversaries move through the network.
9. Collection: How adversaries gather data of interest to their goals.
10. Command and Control: How adversaries communicate with systems under their control.
11. Exfiltration: How adversaries steal data from the network.
Impact: How adversaries manipulate, interrupt, or destroy systems and data.

# Techniques
Techniques describe "how" adversaries achieve their tactical goals. Each tactic can have multiple techniques associated with it, providing more granularity in understanding adversarial behavior. For example:

- **Spear Phishing (Initial Access)**: Sending targeted emails to gain access.
- **PowerShell (Execution)**: Using PowerShell scripts to execute commands.

# Sub-Techniques
Sub-techniques provide further granularity by breaking down techniques into more specific methods. They offer a deeper understanding of how adversaries carry out techniques. For example:

- **Spear Phishing via Service (Initial Access → Spear Phishing)**: Using social media or other services for spear-phishing attacks.
- **PowerShell Profile (Execution → PowerShell)**: Leveraging PowerShell profiles for execution.

# Procedures
Procedures are the specific, detailed methods adversaries use to carry out techniques and sub-techniques. They describe the exact steps or tools used in an attack, often documented through real-world case studies or incident reports. For example:

- **Using a specific phishing email template that mimics a legitimate service to deliver a malicious link.**
- **Deploying a well-known malware variant that exploits a specific software vulnerability.**

# Groups
Groups are collections of related intrusion activity that are tracked by common attributes. They represent known adversary groups or campaigns, often identified by their unique behaviors and methods.

# Campaigns
Campaigns refer to a set of related intrusion activities over a particular period, often tied to a specific objective or series of objectives. They provide a context for understanding adversary behavior over time.

# Relationships
ATT&CK includes information on relationships between various entities, such as:

- Groups and Techniques: Which techniques are used by specific adversary groups.
- Techniques and Mitigations: How particular techniques can be mitigated.
- Software and Techniques: Which techniques are enabled by specific software.

# Software
Software includes tools, malware, and scripts used by adversaries to achieve their goals. Each software entry provides details on its capabilities, the techniques it supports, and any known defenses against it.

# Mitigations
Mitigations are recommendations and actions that organizations can implement to protect against specific techniques. They provide guidance on how to reduce the risk and impact of attacks.
