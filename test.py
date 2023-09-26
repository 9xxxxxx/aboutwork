from adbutils import adb
import uiautomator2 as u2
from threading import Thread
from main import *
for d in adb.device_list():
    # print(d.serial) # print device serial
    d = u2.connect(d.serial)
    app = Thread(target=addfriends, args=(1, 1, 1))
    print(d.info)
    app.start()
