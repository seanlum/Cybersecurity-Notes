import subprocess
import socket
import re
import os
import platform

def resolve_ip(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return ip  # fallback to IP if DNS resolution fails

def get_full_command(pid):
    try:
        if platform.system() == "Linux":
            exe_path = os.readlink(f"/proc/{pid}/exe")
        else:  # macOS or other
            result = subprocess.run(["ps", "-p", pid, "-o", "command="], capture_output=True, text=True)
            exe_path = result.stdout.strip().split("\n")[0]
        return exe_path
    except Exception:
        return "<unknown>".ljust(30)

def main():
    # Get TCP established connections
    result = subprocess.run(
        ["lsof", "-iTCP", "-sTCP:ESTABLISHED", "-nP"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.strip().split('\n')
    if len(lines) <= 1:
        print("No established connections found.")
        return

    # print(f"{'COMMAND':<100}' {'PID':<6} {'LOCAL':<22} {'REMOTE (resolved)':<50}")
    # print('-' * 110)

    for line in lines[1:]:
        parts = re.split(r'\s+', line, maxsplit=8)
        if len(parts) < 9:
            continue

        _, pid, _, _, _, _, _, _, name = parts
        pid = pid.strip()

        if '->' in name:
            local, remote = name.split('->')
            ip_port = remote.rsplit(':', 1)
            if len(ip_port) != 2:
                continue
            ip, port = ip_port
            resolved = resolve_ip(ip.strip())
            remote_resolved = f"{resolved}:{port.strip()}"
        else:
            local = name.strip()
            remote_resolved = ""

        full_cmd = get_full_command(pid)

        print('-' * 110)
        print(f"COMMAND: {full_cmd}")
        print(f'PID: {pid}')
        print(f"{local:<22} {remote_resolved:<50}")

if __name__ == "__main__":
    main()
