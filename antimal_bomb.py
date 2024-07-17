import os
import time
import ctypes
import subprocess
import platform
import winreg
import getpass

# Create VM-like registry keys
def create_vm_registry_keys():
    try:
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\VMware, Inc.\VMware Tools")
        winreg.SetValueEx(key, "InstallPath", 0, winreg.REG_SZ, "C:\\Program Files\\VMware\\VMware Tools\\")
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Error creating registry key: {e}")

# Create sandbox artifacts
def create_sandbox_artifacts():
    try:
        os.makedirs("C:\\Cuckoo")
        with open("C:\\Cuckoo\\analysis.log", "w") as f:
            f.write("Sandbox analysis log.")
    except Exception as e:
        print(f"Error creating sandbox artifacts: {e}")

# Simulate user interaction
def simulate_user_interaction():
    for _ in range(10):
        ctypes.windll.user32.LockWorkStation()
        time.sleep(2)
        # Simulating unlock by sending CTRL+ALT+DELETE and Enter key press
        ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # CTRL
        ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)  # ALT
        ctypes.windll.user32.keybd_event(0x2E, 0, 0, 0)  # DELETE
        time.sleep(1)
        ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)  # Release CTRL
        ctypes.windll.user32.keybd_event(0x12, 0, 2, 0)  # Release ALT
        ctypes.windll.user32.keybd_event(0x2E, 0, 2, 0)  # Release DELETE
        time.sleep(1)
        ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)  # Enter
        ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)  # Release Enter
        time.sleep(2)

# Simulate long periods of inactivity by sleeping
def simulate_inactivity(duration):
    print(f"Simulating inactivity for {duration} seconds.")
    time.sleep(duration)

# Change system locale and timezone
def change_locale_and_timezone():
    try:
        subprocess.run(["tzutil", "/s", "UTC"], check=True)  # Change timezone to UTC
        os.environ['TZ'] = 'UTC'
        time.tzset()
        print("Locale and timezone set to UTC.")
    except Exception as e:
        print(f"Error changing locale and timezone: {e}")

# Check for VM environment by looking for typical VM artifacts
def is_vm_environment():
    vm_indicators = ["VirtualBox", "VBOX", "VMware"]
    for indicator in vm_indicators:
        if indicator in platform.release():
            return True
    return False

# Spoof IP to appear from a different geographic location
def spoof_ip():
    try:
        # Simple way to change IP if VPN or proxy setup is available
        # Note: Implementation may vary based on the available tools and setup
        subprocess.run(["vpncmd", "localhost", "/CLIENT", "/CMD", "AccountConnect", "VPN_Account"], check=True)
        print("IP spoofed using VPN.")
    except Exception as e:
        print(f"Error spoofing IP: {e}")

# Change hardware identifiers
def change_hardware_identifiers():
    try:
        # Note: Changing hardware IDs like MAC address requires third-party tools or specific drivers
        # This is a placeholder example for MAC address spoofing
        subprocess.run(["macchanger", "-r", "eth0"], check=True)
        print("Hardware identifiers spoofed.")
    except Exception as e:
        print(f"Error changing hardware identifiers: {e}")

# Spoof usernames
def spoof_username():
    try:
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        winreg.SetValueEx(key, "RegisteredOwner", 0, winreg.REG_SZ, "AnalysisUser")
        winreg.CloseKey(key)
        print("Username spoofed.")
    except Exception as e:
        print(f"Error spoofing username: {e}")

# Simulate common analysis process names
def simulate_process_names():
    try:
        subprocess.Popen(["notepad.exe"])  # Simulate a common analysis tool
        subprocess.Popen(["calc.exe"])     # Simulate another common tool
        print("Simulated common analysis process names.")
    except Exception as e:
        print(f"Error simulating process names: {e}")

# Require password protection to access certain actions
def require_password():
    password = "securepassword"
    entered_password = getpass.getpass("Enter password to continue: ")
    if entered_password != password:
        print("Incorrect password. Exiting.")
        exit()

# Simulate CPU temperature readings
def simulate_cpu_temperature():
    # Create a mock file or registry key that malware might check
    try:
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
        winreg.SetValueEx(key, "ProcessorNameString", 0, winreg.REG_SZ, "Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz")
        winreg.SetValueEx(key, "Temperature", 0, winreg.REG_SZ, "40C")  # Mock temperature value
        winreg.CloseKey(key)
        print("Simulated CPU temperature.")
    except Exception as e:
        print(f"Error simulating CPU temperature: {e}")

# Simulate system uptime
def simulate_system_uptime():
    try:
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Windows")
        # Simulate uptime by setting a mock value
        winreg.SetValueEx(key, "SystemUptime", 0, winreg.REG_DWORD, 360000)  # Mock uptime value in seconds
        winreg.CloseKey(key)
        print("Simulated system uptime.")
    except Exception as e:
        print(f"Error simulating system uptime: {e}")

# Simulate CPU core count
def simulate_cpu_core_count():
    try:
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor")
        winreg.SetValueEx(key, "NumberOfCores", 0, winreg.REG_DWORD, 8)  # Mock core count
        winreg.CloseKey(key)
        print("Simulated CPU core count.")
    except Exception as e:
        print(f"Error simulating CPU core count: {e}")

# Create recent data with metadata
def create_recent_data():
    try:
        recent_file_path = "C:\\Users\\AnalysisUser\\Documents\\recent_file.txt"
        with open(recent_file_path, "w") as f:
            f.write("This is a recent file for analysis purposes.")
        # Modify the file's metadata to appear recent
        os.utime(recent_file_path, (time.time() - 60*60*24, time.time()))  # Access and modified times
        print("Created recent data with modified metadata.")
    except Exception as e:
        print(f"Error creating recent data: {e}")

if __name__ == "__main__":
    require_password()
    create_vm_registry_keys()
    create_sandbox_artifacts()
    simulate_user_interaction()
    simulate_inactivity(60)  # Simulate 1 minute of inactivity
    change_locale_and_timezone()
    if is_vm_environment():
        print("VM environment detected, adjusting behavior.")
    spoof_ip()
    change_hardware_identifiers()
    spoof_username()
    simulate_process_names()
    simulate_cpu_temperature()
    simulate_system_uptime()
    simulate_cpu_core_count()
    create_recent_data()
    print("Process Complete . Remember this only buys you time and shouldnt be taken as a complete security solution")
