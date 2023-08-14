import sys
from time import sleep
from connections import WiFiManager, BluetoothManager
from entities import command

blue = BluetoothManager("ACS #9181")

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

while True:
    msg = blue.write()
    try:
        commands.get(msg)()
    except Exception as e:
        print(e)