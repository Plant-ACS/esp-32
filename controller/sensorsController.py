from connections import BluetoothManager
from sensors import Sensor, LDR, Moisture, Temperature
from modules import Relay
from controller import memoryController

blue = BluetoothManager("ACS #9181")

class SensorsController:
    @staticmethod
    def add(jsonDict: dict):
        sensor = Sensor(port = jsonDict["port"], 
                        min = jsonDict["min"], 
                        max = jsonDict["max"])

        if (jsonDict["type"] == "ldr"):
            memoryController.MemoryController.addSensor(LDR(sensor = sensor))
            
        elif (jsonDict["type"] == "moisture"):
            memoryController.MemoryController.addSensor(Moisture(sensor = sensor))

        elif (jsonDict["type"] == "temperature"):
            memoryController.MemoryController.addSensor(Temperature(sensor = sensor))

        else:
            raise Exception("Invalid sensor type")
        
    @staticmethod
    def remove(port: str):
        memoryController.MemoryController.removeSensor(port)

    @staticmethod
    def get(port: str):
        return memoryController.MemoryController.getSensor(port)
