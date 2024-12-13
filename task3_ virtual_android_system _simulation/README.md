# Virtual Android System Simulation

This project simulates a virtual Android environment, allowing you to perform basic tasks like launching an emulator, installing an APK, and retrieving system information.

## Prerequisites

### Software Requirements
- **Python**: Version 3.7+
- **Android Studio**: Installed with a configured Android SDK
- **ADB**: Ensure `adb` is included in your PATH
- **QEMU/Emulator**: Comes with Android SDK

### Emulator Configuration
- Emulator Path: `C:\Users\DELL\AppData\Local\Android\Sdk\emulator`
- AVD Name: `Medium_Phone_API_34`
- APK File: Place your APK file (e.g., `sample-app.apk`) in the directory `C:\Users\DELL\Downloads`.

---

## File Structure

```
project_root/
├── virtual_android_system.py    # Main Python script
├── system_info.log              # Output log for system information
└── README.md                    # Documentation
```

---

## How to Run

### Step 1: Start the Emulator

1. Open a terminal or command prompt.
2. Navigate to the emulator directory:
   ```bash
   cd C:\Users\DELL\AppData\Local\Android\Sdk\emulator
   ```
3. Start the emulator:
   ```bash
   emulator -avd Medium_Phone_API_34 -no-snapshot
   ```

### Step 2: Install Python Dependencies

Ensure Python is installed and verify required modules:
```bash
pip install subprocess os shutil
```

### Step 3: Run the Python Script

1. Navigate to the project directory:
   ```bash
   cd <project_root>
   ```
2. Execute the script:
   ```bash
   python virtual_android_system.py
   ```

---

## Expected Outputs

### 1. APK Installation
- The specified APK (`sample-app.apk`) will be installed on the emulator.

### 2. System Information Logging
- A file named `system_info.log` will be generated in the project directory, containing details like OS version, device model, and available memory.

---

## Troubleshooting

### Emulator Fails to Start
- Ensure the AVD name (`Medium_Phone_API_34`) is correct by listing available devices:
  ```bash
  emulator -list-avds
  ```
- Start the emulator manually with a cold boot:
  ```bash
  emulator -avd Medium_Phone_API_34 -no-snapshot
  ```

### ADB Not Found
- Add `C:\Users\DELL\AppData\Local\Android\Sdk\platform-tools` to your system's PATH variable.
- Restart the terminal and verify ADB:
  ```bash
  adb devices
  ```

---

## Notes
- Ensure that the emulator is running before executing the Python script.
- The script requires the paths for the emulator and APK to be accurate.

Feel free to modify the script for additional functionalities or custom AVD configurations.
