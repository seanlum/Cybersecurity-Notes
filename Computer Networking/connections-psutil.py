import psutil
import socket

def resolve_ip(ip):
    """Attempt to resolve an IP to a hostname; fallback to IP string."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        return ip

def list_remote_connections_with_details():
    connections = psutil.net_connections(kind='inet')
    seen_pids = set()

    for conn in connections:
        if conn.raddr and conn.pid and conn.pid not in seen_pids:
            seen_pids.add(conn.pid)
            try:
                proc = psutil.Process(conn.pid)
                print(f"PID: {conn.pid}")
                print(f"Program: {proc.name()}")
                print(f"Executable: {proc.exe()}")
                print(f"Cmdline: {' '.join(proc.cmdline())}")
                
                local_ip = conn.laddr.ip
                local_port = conn.laddr.port
                local_host = resolve_ip(local_ip)
                
                remote_ip = conn.raddr.ip
                remote_port = conn.raddr.port
                remote_host = resolve_ip(remote_ip)

                print(f"Local Address: {local_host}:{local_port}")
                print(f"Remote Address: {remote_host}:{remote_port}")
                print(f"Status: {conn.status}")
                print("-" * 80)
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                print(f"PID {conn.pid} - Access denied or process exited")
                print("-" * 80)

if __name__ == "__main__":
    list_remote_connections_with_details()
