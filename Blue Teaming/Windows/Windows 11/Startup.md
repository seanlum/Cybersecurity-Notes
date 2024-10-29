# Loading Configurable Options in Windows

1. Pre-Boot Sequence
  - a. BIOS/UEFI Initialization
    - Facility: BIOS/UEFI Firmware
    - Description: Initializes hardware components and performs Power-On Self-Test (POST).
  - b. Boot Configuration Data (BCD)
    - Facility: Boot Manager (bootmgr)
    - Description: Reads the BCD store to determine which operating system to load and boot parameters.
2. Boot Loader Phase
  - a. Windows OS Loader
    - Facility: Winload.exe
    - Description: Loads the Windows kernel (ntoskrnl.exe), HAL (hal.dll), boot-class device drivers, and system registry hive.
3. Kernel Initialization
  - a. Kernel and HAL Initialization
    - Facility: Kernel (ntoskrnl.exe) and HAL
    - Description: Initializes low-level system components, memory management, and processor control structures.
  - b. Boot-Class Device Drivers
    - Facility: System Drivers
    - Description: Loads essential drivers needed to access the boot volume and other critical hardware.
4. System Initialization
  - a. Session Manager Subsystem (SMSS)
    - Facility: smss.exe
    - Description: Initializes system sessions, loads and starts kernel-mode subsystems, and sets up the environment for the Win32 subsystem.
  - b. System Registry Hive Load
    - Facility: Registry (HKEY_LOCAL_MACHINE\SYSTEM)
    - Description: Loads system configuration settings critical for startup.
5. Service Control Manager (SCM) Initialization
  - a. Services and Drivers Start
    - Facility: services.exe
    - Description: Starts services and drivers set to Automatic start type.
6. Winlogon Initialization
  - a. Winlogon and LogonUI
    - Facility: winlogon.exe and LogonUI.exe
    - Description: Handles user authentication and logon process.
7. Machine-Level Configuration
  - a. Computer Configuration Group Policy
    - Facility: Group Policy Engine
    - Description: Applies machine-level Group Policy settings, including security settings, scripts, software installations, and preferences.
  - b. Machine Startup Scripts
    - Facility: Group Policy Scripts Extension
    - Description: Executes any startup scripts defined in Group Policy.
8. User Logon Process
  - a. User Authentication
    - Facility: LSASS.exe (Local Security Authority Subsystem Service)
    - Description: Authenticates user credentials against local or domain accounts.
  - b. User Profile Load
    - Facility: User Profile Service (ProfSvc)
    - Description: Loads the user's profile, including the user registry hive (NTUSER.DAT into HKEY_CURRENT_USER).
9. User-Level Configuration
  - a. User Registry Settings
    - Facility: Registry (HKEY_CURRENT_USER)
    - Description: Applies user-specific registry settings, preferences, and configurations.
  - b. User Configuration Group Policy
    - Facility: Group Policy Engine
    - Description: Applies user-level Group Policy settings, including software installations, folder redirections, scripts, and preferences.
  - c. User Logon Scripts
    - Facility: Group Policy Scripts Extension
    - Description: Executes any logon scripts defined in Group Policy.
10. Startup Applications and Services
  - a. Startup Programs
    - Facility: Startup Folder and Registry Run Keys
    - Startup Folders:
      - All Users: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
      - Current User: %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
    - Registry Keys:
      - Machine Level: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
      - User Level: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
    - Description: Launches applications configured to start automatically after user logon.
  - b. Scheduled Tasks
    - Facility: Task Scheduler
    - Description: Executes tasks scheduled to run at startup or user logon.
11. Windows Services and Background Tasks
  - a. Delayed Auto-Start Services
    - Facility: Service Control Manager
    - Description: Starts services set to Automatic (Delayed Start) after initial boot processes.

### Additional Configuration Facilities Involved
- System Environment Variables
  - Facility: System Properties
  - Description: Loads system-wide and user-specific environment variables.
- Local Security Policy
  - Facility: Local Security Policy Editor (secpol.msc)
  - Description: Applies security settings defined locally, including account policies and user rights assignments.
- Device Drivers
  - Facility: Plug and Play Manager
  - Description: Initializes device drivers for hardware detected after initial boot.
- Windows Management Instrumentation (WMI)
  - Facility: WMI Service (winmgmt)
  - Description: Provides system management information to applications.

### Order Summary
1. BIOS/UEFI Initialization
2. Boot Configuration Data (BCD)
3. Windows OS Loader (winload.exe)
4. Kernel Initialization
5. Boot-Class Device Drivers Load
6. System Registry Hive Load (HKLM\SYSTEM)
7. Session Manager Subsystem (smss.exe)
8. Service Control Manager Starts Auto-Start Services
9. Winlogon and User Authentication
10. Computer Configuration Group Policy Applied
11. Machine Startup Scripts Executed
12. User Profile Loaded (User Registry Hive)
13. User Registry Settings Applied (HKCU)
14. User Configuration Group Policy Applied
15. User Logon Scripts Executed
16. Startup Programs Launched
17. Scheduled Tasks Executed
18. Delayed Auto-Start Services Started