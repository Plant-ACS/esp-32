from time import sleep
from connections import WiFiManager, BluetoothManager

blue = BluetoothManager("ACS #9181")

while True:
    msg = blue.write()
    if msg == "list-wifi":
        for i in WiFiManager.getList():
            blue.send(str(i))
    elif msg == "connect-wifi":
        blue.send("SSID: ", end="")
        ssid = blue.write()
        blue.send("Password: ", end="")
        password = blue.write()
        if WiFiManager.connect(ssid, password):
            blue.send("Connected")
        else:
            blue.send("Failed")
    elif msg == "disconnect-wifi":
        WiFiManager.disconnect()
        blue.send("Disconnected")
    elif msg == "exit":
        blue.send("Bye")
        break