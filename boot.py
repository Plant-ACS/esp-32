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
        if WiFiManager.connect([blue.send("SSID: ", end=""), blue.read()][1], [blue.send("Password: ", end=""), blue.read()][1])
        else blue.send("failed to connect to wifi")
)
commands.add(
    "disconnect-wifi",
    lambda: [WiFiManager.disconnect(), blue.send("disconnected from wifi")]
)
commands.add(
    "exit",
    lambda: [blue.send("Bye!"), sys.exit()]
)
commands.add(
    "add-sensor",
    lambda: 
        sensorsConnected.append(LDR(sensor = commands.get("create-sensor")())) 
        if [blue.send("Sensor type (ldr, moisture): "), blue.readOnly(["ldr", "moisture"])][1] == "ldr" 
        else sensorsConnected.append(Moisture(sensor = commands.get("create-sensor")()))
)
commands.add(
    "create-sensor",
    lambda: 
        Sensor([blue.send("Port: ", end=""), blue.filterInt()][1], 
        [blue.send("Minimum value (optional: 'n'): ", end=""), blue.filterIntOptional("n")][1],
        [blue.send("Maximum value (optional: 'n'): ", end=""), blue.filterIntOptional("n")][1]
        )
)
commands.add(
    "list-sensors",
    lambda: 
        list(map(lambda s: blue.send(str([type(s), s.getPort()])), sensorsConnected))
        if len(sensorsConnected) != 0
        else blue.send("no sensors added so far")
)

while True:
    msg = blue.read()
    try:
        commands.get(msg)()
    except Exception as e:
        print(e)
