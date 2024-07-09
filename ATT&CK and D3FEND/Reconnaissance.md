# Reconnaissance
Reconnaissance is a tactic within the MITRE ATT&CK framework, specifically aimed at adversaries' efforts to gather information they can use to plan and execute an attack. This phase often involves the collection of details about the target's network, systems, personnel, and other assets. By understanding the reconnaissance techniques, organizations can better detect and defend against initial phases of an attack.

### Reconnaissance Tactic
Reconnaissance involves adversaries trying to gather information they can use to identify and exploit weaknesses in the target's defenses. This information can include details about the target's infrastructure, employee information, publicly exposed systems, and more.

# Techniques Associated with Reconnaissance
Here are some common reconnaissance techniques as defined in the MITRE ATT&CK framework:

### 1. Active Scanning (T1595)
- Description: Using tools to actively probe and scan the target's network and systems to identify live hosts, open ports, services, and vulnerabilities.
- Sub-techniques:
  - **Scanning IP Blocks (T1595.001)**: Scanning a range of IP addresses to discover live hosts.
  - **Vulnerability Scanning (T1595.002)**: Identifying vulnerabilities in systems and applications by scanning for known flaws.

### 2. Gather Victim Identity Information (T1589)
- **Description**: Collecting information about target individuals, such as usernames, email addresses, and job roles.
- **Sub-techniques**:
  - **Email Addresses (T1589.001)**: Gathering email addresses of target individuals.
  - **Employee Names (T1589.002)**: Identifying names of employees to use in social engineering or spear-phishing attacks.

### 3. Gather Victim Network Information (T1590)

- **Description**: Collecting information about the target's network infrastructure, including domain names, IP addresses, and network topology.
- **Sub-techniques**:
  - **Domain Properties (T1590.001)**: Gathering information about domain names and associated properties.
  - **DNS (T1590.002)**: Using DNS queries to gather information about the target's domain infrastructure.
  - **IP Addresses (T1590.003)**: Collecting IP addresses associated with the target's network.

### 4. Gather Victim Organization Information (T1591)

- **Description**: Collecting information about the target organization, such as business operations, locations, and external relationships.
- **Sub-techniques**:
  - **Business Relationships (T1591.001)**: Identifying the target's business relationships and partnerships.
  - **Organizational Information (T1591.002)**: Collecting details about the organization’s structure, operations, and strategic objectives.

### 5. Phishing for Information (T1598)

- **Description**: Using phishing techniques to gather information from the target, such as credentials or other sensitive data.
- **Sub-techniques**:
  - **Spearphishing Attachment (T1598.001)**: Sending emails with malicious attachments to gather information.
  - **Spearphishing Link (T1598.002)**: Using links in emails to direct targets to malicious websites designed to gather information.
  - **Spearphishing via Service (T1598.003)**: Leveraging messaging services or social media for phishing attacks.

### 6. Search Open Technical Databases (T1596)

- **Description**: Searching publicly available technical databases for information about the target's technology stack, vulnerabilities, and infrastructure.
- **Sub-techniques**:
  - **Scan Databases (T1596.001)**: Using databases that track scans and vulnerabilities, such as Shodan or Censys, to gather information.
  - **WHOIS (T1596.002)**: Using WHOIS databases to gather information about domain registration and ownership.

### 7. Search Open Websites/Domains (T1593)

- **Description**: Collecting information from publicly accessible websites and domains.
- **Sub-techniques**:
  - **Social Media (T1593.001)**: Gathering information from social media platforms.
  - **Search Engines (T1593.002)**: Using search engines to find information about the target.
  - **Third-party Sites (T1593.003)**: Using third-party websites that may contain information about the target, such as job postings or press releases.

## Example of Reconnaissance in Action
An adversary may use multiple reconnaissance techniques in preparation for an attack. For example:

- **Active Scanning**: The adversary uses tools like Nmap to scan the target's network for open ports and services.
- **Gather Victim Identity Information**: The adversary collects email addresses and employee names from the target's website and LinkedIn profiles.
- **Phishing for Information**: Using the gathered email addresses, the adversary sends spear-phishing emails with malicious attachments to gain initial access.

By understanding and monitoring for these reconnaissance techniques, organizations can detect potential threats early in the attack lifecycle and implement measures to mitigate these threats.