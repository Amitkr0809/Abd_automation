import subprocess
import time

class Call():

    def mtcall(self,dev_id1,phnum):
        try:
            subprocess.run(['adb', '-s',dev_id1,'shell', 'am','start',
                            '-a','android.intent.action.CALL','-d','tel:' + phnum])
            time.sleep(5)
        except Exception as e:
            raise e

    def anscall(self,dev_id2):
        try:
            subprocess.run(['adb', '-s', dev_id2, 'shell','input','keyevent', '5'])
            time.sleep(10)
        except Exception as e:
            raise e

