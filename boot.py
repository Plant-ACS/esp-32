import sys
from connections import WiFiManager, BluetoothManager
from entities import command, communicate
from controller import sensorsController, modulesController, memoryController

blue = BluetoothManager("ACS #9181")

sensors_connected = []

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
        sensorsController.SensorsController.add(
            [blue.send("Type JSON: "), 
             communicate.Communicate.str_to_json(blue.read_until_find("}"))][1])
)
commands.add(
    "remove-sensor",
    lambda:
        sensorsController.SensorsController.remove(
            [blue.send("Port: "), communicate.Communicate.str_to_json(blue.read_until_find("}"))["port"]][1]
        )
)
commands.add(
    "list-sensors",
    lambda: 
        list((map(lambda element: blue.send(str(element) + "\n"), (memoryController.MemoryController.listSensors())))
    )
)
commands.add(
    "add-module",
    lambda:
        modulesController.ModuleController.add(
            [blue.send("Type JSON: "), 
             communicate.Communicate.str_to_json(blue.read_until_find("}"))][1])
)
commands.add(
    "remove-module",
    lambda:
        modulesController.ModuleController.remove(
            [blue.send("Port: "), 
             communicate.Communicate.str_to_json(blue.read_until_find("}"))["port"]][1]
        )
)
commands.add(
    "list-modules",
    lambda:
        memoryController.MemoryController.listModules()
)

invite = False

while True:
    # while not blue.isConnected():
    try:
        msg = blue.read()
        msg = communicate.Communicate.str_to_json(msg)
        commands.get(msg["name"])()
        
    except Exception as e:
        print(e)