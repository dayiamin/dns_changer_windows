import ctypes
import sys


def is_admin():
    try:
        # Check if the script is running with admin privileges
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        # If already admin, continue running the script
        return True
    else:
        # Request admin privileges
        print("Requesting administrator privileges...")
        try:
            # Restart the script with admin privileges
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, ' '.join([f'"{arg}"' for arg in sys.argv]), None, 1
            )
            sys.exit()
        except Exception as e:
            print(f"Failed to elevate to administrator privileges: {e}")
            sys.exit(1)