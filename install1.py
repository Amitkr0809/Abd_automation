import subprocess


apk_path = "C:\Users\DELL\Downloads"

adb_command = f"adb install {apk_path}"

try:
    subprocess.check_output(adb_command.split())
    print("App installed successfully")
except subprocess.CalledProcessError as e:
    print(f"Error installing app: {e}")