# Group Policy

[Group Policy Overview | Windows Server 2012](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11))

[Group Policy Overview | Windows Server](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)

[Group Policy troubleshooting documentation for Windows Server](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/group-policy-overview)

## To view Group Policy in Windows 11 Pro

Run `gpedit.msc`

or

Run `mmc` And then add the `Group Policy` snap-in .

## Resultant Set of Policy 

RSoP gathers this information from the Common Information Management Object Model (CIMOM) database (otherwise known as CIM-compliant object repository) through Windows Management Instrumentation (WMI).

### To view Resultant Set of Policy in Windows 11 Pro

[Use Rsop.msc to gather computer policy](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-resultant-set-of-policy-logging)

Run `rsop.msc`

or 

Run `mmc` and then add the `Resultant Set of Policy` snap-in

## Generating an RSOP Report

### `gpresult`
```
PS C:\> gpresult /?

GPRESULT [/S system [/U username [/P [password]]]] [/SCOPE scope]
           [/USER targetusername] [/R | /V | /Z] [(/X | /H) <filename> [/F]]

Description:
    This command line tool displays the Resultant Set of Policy (RSoP)
    information for a target user and computer.

Parameter List:
    /S        system           Specifies the remote system to connect to.

    /U        [domain\]user    Specifies the user context under which the
                               command should run.
                               Can not be used with /X, /H.

    /P        [password]       Specifies the password for the given user
                               context. Prompts for input if omitted.
                               Cannot be used with /X, /H.

    /SCOPE    scope            Specifies whether the user or the
                               computer settings need to be displayed.
                               Valid values: "USER", "COMPUTER".

    /USER     [domain\]user    Specifies the user name for which the
                               RSoP data is to be displayed.

    /X        <filename>       Saves the report in XML format at the
                               location and with the file name specified
                               by the <filename> parameter. (valid in Windows
                               Vista SP1 and later and Windows Server 2008 and later)

    /H        <filename>       Saves the report in HTML format at the
                               location and with the file name specified by
                               the <filename> parameter. (valid in Windows
                               at least Vista SP1 and at least Windows Server 2008)

    /F                         Forces Gpresult to overwrite the file name
                               specified in the /X or /H command.

    /R                         Displays RSoP summary data.

    /V                         Specifies that verbose information should
                               be displayed. Verbose information provides
                               additional detailed settings that have
                               been applied with a precedence of 1.

    /Z                         Specifies that the super-verbose
                               information should be displayed. Super-
                               verbose information provides additional
                               detailed settings that have been applied
                               with a precedence of 1 and higher. This
                               allows you to see if a setting was set in
                               multiple places. See the Group Policy
                               online help topic for more information.

    /?                         Displays this help message.


Examples:
    GPRESULT /R
    GPRESULT /H GPReport.html
    GPRESULT /USER targetusername /V
    GPRESULT /S system /USER targetusername /SCOPE COMPUTER /Z
    GPRESULT /S system /U username /P password /SCOPE USER /V
```
#### `gpresult /r`
```
This command provides a text summary of the user and computer policies applied, including details like the domain controller, OU, and applied GPOs.
```
#### `gpresult /v`
```
Adds more detail about the applied Group Policy settings, including components like scripts, software installation, and security settings.
```
#### `gpresult /z`
```
Provides a verbose view of all applied settings, including those that were filtered out or not applied.
```
#### `gpresult /h report.html`
```
This command generates a comprehensive HTML report that provides an organized view of both user and computer policies.
```
#### `gpresult /user [username] /h report.html`
```
Replace [username] with the specific user account to generate a report for that user
```
#### `gpresult /s [computername] /h report.html`
```
Replace [computername] with the target remote computer's name.
```

### Using Powershell

These powershell cmdlets do not come with Windows.

#### `Get-GPOReport -All -ReportType XML -Path "C:\path\to\report.xml"`
#### `Get-GPOReport -All -ReportType HTML -Path "C:\path\to\report.html"`
#### `Get-GPOReport -Name "GPO Name" -ReportType HTML -Path "C:\path\to\report.html"`
#### `Get-ADUserResultantPolicy`

## Exporting Group Policy

- [Microsoft Security Compliance Toolkit](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

### Using LGPO.exe

Note: `LGPO will create backups for your local system and create a new GUID every time, even if it is the same GPO, always double check your GPO backups`


```
D:\bin\LGPO_30\LGPO.exe /b "C:\GPOBackups\" /n "SystemName"
```

### Importing with LGPO.exe

`This next example searches C:\GPOBackups for files named registry.pol, GptTmpl.inf, or audit.csv and
imports their contents into local policy, and also registers any machine or user CSEs referenced in
backup.xml files into local policy. As with the previous example, it also writes verbose output to log files.`

```cmd
LGPO.exe /g C:\GPOBackups /v > lgpo.out 2> lgpo.err
```