# Windows Security Policy Settings

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/security-policy-settings

## Exporting secedit policy

```
secedit /export /cfg C:\path\to\security-policy.inf
```

## Importing secedit policy

```
secedit /configure /db C:\Windows\Security\Database\secedit.sdb /cfg C:\path\to\security-policy.inf
```