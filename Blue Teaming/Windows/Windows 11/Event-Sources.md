# Event Sources in Windows
### [Win32 Event Sources](https://learn.microsoft.com/en-us/windows/win32/eventlog/event-sources)
### [Win32 Event Logging](https://learn.microsoft.com/en-us/windows/win32/eventlog/event-logging)
## Registry Paths
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Application
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Application\<Appname>
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Security
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\System
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\System\<DriverName>
```
## Common Event Sources in Windows
```
Processes and Services
  - Process creation/termination
  - Service Status changes (start, stop, failure)
  - Scheduled tasks (creation, modification, execution)
File System
  - File creation, modification, deletion
  - File permissions changes
  - Access to sensitive files
    - System 32 
    - SAM file
    - Logs
System Logs
  - Windows Event Logs (Application, Security, System, Setup, Forwarded Events)
  - Sysmon Logs (if enabled)
User Accounts
  - User logon/logoff events
  - Privilege escalation
  - Group membership changes
  - Account lockouts
Active Directory
  - LDAP queries
  - Group policy changes
  - Authentication / Authorization Events
  - Replication status
Network Traffic
  - Inbound and outbound connections
  - DNS queries and responses
  - Firewall events
Remote Access
  - RDP usage
  - VPN connection events
  - SSH/Telnet activity
USB and External Media
  - Device Connection/Disconnection
  - File transfers to/from external devices
Printer Activity
  - Printer jobs
  - Driver installation
  - Permissions changes
Application installs/uninstalls
  - Application crashes
  - Software updates
    - Windows Updates 
    - Windows SUS logs
Browser Activity
  - URL accesses
  - Downloaded files
  - Extensions/add-ons
Antivirus/Antimalware
  - Detection Logs
  - Quarantine actions
  - Scan results
Firewall Logs
  - Policy violations
  - Rule changes
Data Loss Prevention (DLP)
  - Sensitive data access
  - Data exfiltration attempts
Authentication Mechanisms
  - Multi-factor authentication (MFA) logs
  - Smart card access events
  - Yubikey or other hardware authentication logs
Hypervisors
  - Virtual machine creation/deletion
  - Resource usage
  - Snapshot creation/modification
Containers
  - Docker/Kybernetes events
  - Image pulls and deployments
  - Container lifecycle eventsa
Power Management
  - Shutdown, restart, sleep events
  - Battery status changes
Audit Policies
  - Changes to security audit policies
  - Success/failure audit logs
Integrity monitoring
Encryption 
  - BitLocker status changes
  - Key usage logs
  - Certificate usage (SSL/TLS)
Third-Party Applications
  - Logs from custom or industry specific software
  - API usage and integration logs
Cloud Activity
  - Azure AD/Office 365 logs
  - AWS or GCP-specific logs (IAM events, CloudTrail etc)
Threat Intelligence Feeds
  - IoC Matches
  - Suspicious IP/domain alerts
Debugging and Diagnostic Logs
  - Crash dumps
  - Performance counters
  - Resource exhaustion events (CPU, RAM, I/O)
Telemetry and Metrics
  - Custom telemetry data (if developed in-house)
  - Performance monitoring (PerfMon logs)
Policy Analysis 
Configuration Analysis
Compliance Analysis 
Backup and Recovery 
  - Backup Jobs 
  - Recovery actions performed
Memory
  - Heap, stack, memory dumps
  - Memory paging
  - Swap reads and writes
Kernel 
  - Low-level operating system internals
  - Kernel drivers
  - System calls
  - Privileged events
Firmware
  - Integrity monitoring
  - BIOS information
  - UEFI information
  - Motherboard information
  - Hardware information
Security Content Automation Protocol
  - Reports 
  - Compliance
  - Regulation Information
```