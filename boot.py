import sys
from time import sleep
from connections import WiFiManager, BluetoothManager
from entities import command, communicate
from sensors import Relay, Sensor, LDR, Moisture 
 
blue = BluetoothManager("ACS #9181")

dict = communicate.Communicate.str_to_json('{"port": 27, "min": 0, "max": 1000}')

sensors_connected = [
    # LDR(dict["port"], dict["min"], dict["max"])
]

current_json = []

commands = command.Command()
private_commands = command.Command()

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
private_commands.add(
    "get-json",
    lambda:
        current_json.append(communicate.Communicate.str_to_json(blue.read_until_find("}")))
)
private_commands.add(
    "clear-json",
    lambda:
        current_json.pop()
)
commands.add(
    "add-sensor",
    lambda: 
        sensors_connected.append(LDR(sensor = commands.get("create-sensor")())) 
        if [blue.send("Sensor type (ldr, moisture): "), blue.read_only(["ldr", "moisture"])][1] == "ldr" 
        else sensors_connected.append(Moisture(sensor = commands.get("create-sensor")()))
)
private_commands.add(
    "create-sensor",
    lambda: 
        Sensor(current_json[0]["port"], 
               current_json[0]["min"], 
               current_json[0]["max"])
)
# private_commands.add(
#     "create-sensor",
#     lambda: 
#         Sensor([blue.send("Port: ", end=""), blue.filterInt()][1], 
#         [blue.send("Minimum value (optional: 'n'): ", end=""), blue.filterIntOptional("n")][1],
#         [blue.send("Maximum value (optional: 'n'): ", end=""), blue.filterIntOptional("n")][1]
#         )
# )
commands.add(
    "list-sensors",
    lambda: 
        list(map(lambda s: blue.send(str([type(s), s.port, s.value()])), sensors_connected))
        if len(sensors_connected) != 0
        else blue.send("no sensors added so far")
)

while True:
    msg = blue.read()
    try:
        if msg == "add-sensor":
            private_commands.get("get-json")()
            commands.get(msg)()
            private_commands.get("clear-json")()
        else: 
            commands.get(msg)()
            
    except Exception as e:
        print(e)
