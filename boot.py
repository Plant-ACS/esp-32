# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from connections import WiFiManager, Bluetooth
Bluetooth("Micro ACS").connected()
print(WiFiManager.getList())
WiFiManager.connect("RotBraido", "rotmi210")