import sys
from time import sleep
from connections import WiFiManager, BluetoothManager
from entities import command
from sensors import Relay, Sensor, LDR, Moisture 
blue = BluetoothManager("ACS #9181")

sensorsConnected = []
commands = command.Command()

commands.add(
    "list-wifi",
    lambda: list(map(lambda e: blue.send(str(e)), WiFiManager.getList()))
)
commands.add(
    "connect-wifi",
    lambda: 
        blue.send("connected to wifi") 
        if WiFiManager.connect([blue.send("SSID: ", end=""), blue.write()][1], [blue.send("Password: ", end=""), blue.write()][1])
        else blue.send("failed to connect to wifi")
)
commands.add(
    "disconnect-wifi",
    lambda: [WiFiManager.disconnect(), blue.send("disconnected from wifi")]
)
commands.add(
    "exit",
    lambda: [blue.send("Bye"), sys.exit()]
)
commands.add(
    "add-sensor",
    lambda: 
        sensorsConnected.append(LDR(commands.get("create-sensor"))) 
        if [blue.send("Sensor type (ldr, moisture): "), blue.write()][1] == "ldr" 
        else sensorsConnected.append(Moisture(commands.get("create-sensor")))
)
commands.add(
    "create-sensor",
    lambda: 
        Sensor([blue.send("Port: ", end=""), blue.write()][1], 
        [blue.send("Minimum value (optional): ", end=""), blue.write()][1]
        [blue.send("Maximum value (optional): ", end=""), blue.write()][1]
        )
)
commands.add(
    "list-sensors",
    lambda: 
        list(map(lambda s: blue.send(str([s.getType(), s.getPort()])), sensorsConnected))
        if len(sensorsConnected) != 0
        else blue.send("no sensors added so far")
)

while True:
    msg = blue.write()
    try:
        commands.get(msg)()
    except Exception as e:
        print(e)