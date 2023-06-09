import os

phone_number = "07838673291"
adb_command = f"adb shell am start -a android.intent.action.CALL -d tel:{phone_number}"

os.system(adb_command)