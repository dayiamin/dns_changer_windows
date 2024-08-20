import subprocess
import os
def to_dic(lis):
    out= {}
    for i,j in enumerate(lis):
        out[i] = j
    return out


def list_network_interfaces():
    """List all network interfaces."""
    result = subprocess.run(['netsh', 'interface', 'show', 'interface'], capture_output=True, text=True)
    interfaces = []
    
    
    for line in result.stdout.splitlines():
        if "Connected" in line:  # Filter lines containing interfaces
            # The interface name usually comes after the status, split by spaces
            interface_name = line.split()[-1]
            interfaces.append(interface_name)
    
    return to_dic(interfaces)

def clear_dns_windows(interface):
    """Clear DNS settings for a specific network interface."""
    try:
        subprocess.run(
            ['netsh', 'interface', 'ipv4', 'set', 'dns', interface, 'static', 'none']
        )
        os.system('cls')
        
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to clear DNS settings: {e}")

def set_dns_windows(interface, primary_dns, secondary_dns):
    """Set primary and secondary DNS for a specific network interface."""
    try:
        # Set primary DNS
        subprocess.run(
            ['netsh', 'interface', 'ipv4', 'set', 'dns', interface, 'static', primary_dns],
            check=True
        )
        # Set secondary DNS
        subprocess.run(
            ['netsh', 'interface', 'ipv4', 'add', 'dns', interface, secondary_dns, 'index=2'],
            check=True
        )
        print(f'changing dns to {primary_dns} , {secondary_dns}')
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to change DNS settings: {e}")


