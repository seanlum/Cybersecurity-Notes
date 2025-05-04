# Group Policy and Networking

# `\Local Computer Policy\Computer Configuration\`
## `\Windows Settings`
### `Name Resolution Policy`
- The Name Resolution Policy Table (NRPT)
#### `DNSSEC`
#### `DNS Settings for Direct Access`
### `Deployed Printers`
- Configure deployed printers provisioned by Group Policy.
  - This may be a network-wide printer

### `Security Settings`
#### `Windows Defender Firewall with Advanced Security`
Rules may be appended to the current firewall configuration using group policy. However, the default set that is applied per Windows instance is still applied.
##### Inbound Rules
##### Outbound Rules
https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/

#### `IP Security Policies`

### [Windows Firewall Rules](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/rules)

## Updating with CSP
- Requires Microsoft Endpoint Manager (Intune), Group Policy, or PowerShell

### Using Group Policy
`Group Policy` -> `Administrative Templates`

```
Local Computer Policy
  \Computer Configuration
    \Administrative Templates
      \Network
        \Network Connections
          \Windows Defender Firewall
            \Domain Profile
            \Standard Profile
```

