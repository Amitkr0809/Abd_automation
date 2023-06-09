import subprocess
import time
import operator
class call:
    def moCall(self):
        try:
             subprocess.run("adb shell am start -a android.intent.action.VIEW -d https://www.sharetechnote.com/html/Handbook_LTE.html")
             time.sleep(20)

        except Exception as e:
            raise e

    def callterm(self):
        try:
             subprocess.run("adb shell input keyevent 6")
        except Exception as e:
            raise e

    def logmsg(self):
        try:
            res=subprocess.check_output("adb logcat -d",shell=True)
            r=str(res)
            result="onServiceStateChanged"
            if operator.contains(r,result):
                print("PASS")
            else:
                print("FAIL")


        except Exception as e:
            raise e




obj=call()
i=0
while i <= 1:
    obj.moCall()
    obj.callterm()
    obj.logmsg()
    i+=1