import os
import subprocess
import time

def start_emulator():
    """Launches the Android emulator."""
    emulator_path = "C:\\Users\\DELL\\AppData\\Local\\Android\\Sdk\\emulator"
    avd_name = "Medium_Phone_API_34"

    try:
        subprocess.Popen([os.path.join(emulator_path, "emulator"), "-avd", avd_name])
        print("Starting emulator...")
        time.sleep(30)  # Allow time for the emulator to boot
    except Exception as e:
        print(f"Error launching emulator: {e}")


def install_apk(apk_path):
    """Installs an APK file into the emulator."""
    try:
        result = subprocess.run(["adb", "install", apk_path], capture_output=True, text=True)
        if result.returncode == 0:
            print("APK installed successfully.")
        else:
            print(f"Error installing APK: {result.stderr}")
    except Exception as e:
        print(f"Error: {e}")


def retrieve_system_info():
    """Retrieves and logs system information."""
    try:
        result = subprocess.run(["adb", "shell", "getprop"], capture_output=True, text=True)
        if result.returncode == 0:
            with open("system_info.log", "w") as log_file:
                log_file.write(result.stdout)
            print("System information logged to system_info.log.")
        else:
            print(f"Error retrieving system info: {result.stderr}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to manage the virtual Android system."""
    apk_path = "C:\\Users\\DELL\\Downloads\\sample-app.apk"  # Update with your APK path

    print("--- Virtual Android System Simulation ---")

    # Step 1: Start the emulator
    start_emulator()

    # Step 2: Install the sample app
    install_apk(apk_path)

    # Step 3: Retrieve and log system information
    retrieve_system_info()

    print("Task completed.")

if __name__ == "__main__":
    main()
