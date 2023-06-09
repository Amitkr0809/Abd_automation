import subprocess
import time

class Call():

    def mo_call(self):
        try:
            for i in range(1,3):
                subprocess.run("adb shell am start -a android.intent.action.CALL -d tel:+918638753379")
                time.sleep(10)
        except Exception as e:
            raise e

obj=call()
obj.moCall()