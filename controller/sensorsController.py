from connections import BluetoothManager
from sensors import Relay, Sensor, LDR, Moisture 
from memoryController import MemoryController

blue = BluetoothManager()

class SensorsController:
    @staticmethod
    def add(jsonDict: dict):
        sensor = Sensor(port = jsonDict[0]["port"], 
                        min = jsonDict["min"], 
                        max = jsonDict["max"])

        if (jsonDict["type"] == "ldr"):
            MemoryController.addSensor(LDR(sensor = sensor))
            
        elif (jsonDict["type"] == "moisture"):
            MemoryController.addSensor(Moisture(sensor = sensor))

        else:
            raise Exception("Invalid sensor type")
        
    @staticmethod
    def remove(port: str):
        MemoryController.removeSensor(port)
