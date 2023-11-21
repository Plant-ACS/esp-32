class MemoryController:
    __sensors = []
    __modules = []

    @staticmethod
    def addModule(module):
        MemoryController.__modules.append(module)

    @staticmethod
    def getModules():
        return MemoryController.__modules
    
    @staticmethod
    def getModule(port: int):
        for module in MemoryController.__modules:
            if module.port == port:
                return module
        return None
    
    @staticmethod
    def removeModule(port: int):
        for module in MemoryController.__modules:
            if module.port == port:
                MemoryController.__modules.remove(module)
                return True
        return False
    
    @staticmethod
    def getModulesByType(t):
        modules = []
        for module in MemoryController.__modules:
            if type(module) == t:
                modules.append(module)
        return modules
    
    @staticmethod
    def listModules():
        if (MemoryController.__modules == []):
            return "no modules have been added so far"
        return list(map(lambda module: str([type(module), module.port, module.value()]), MemoryController.__modules))

    @staticmethod
    def addSensor(sensor):
        MemoryController.__sensors.append(sensor)

    @staticmethod
    def getSensors():
        return MemoryController.__sensors
    
    @staticmethod
    def getSensor(port: int):
        for sensor in MemoryController.__sensors:
            if sensor.port == port:
                return sensor
        return None
    
    @staticmethod
    def removeSensor(port: int):
        for sensor in MemoryController.__sensors:
            if sensor.port == port:
                MemoryController.__sensors.remove(sensor)
                return True
        return False
    
    @staticmethod
    def getSensorsByType(t):
        sensors = []
        for sensor in MemoryController.__sensors:
            if type(sensor) == t:
                sensors.append(sensor)
        return sensors
    
    @staticmethod
    def listSensors():
        if (MemoryController.__sensors == []):
            return "no sensors have been added so far"
        return list(map(lambda sensor: str([type(sensor), sensor.port, sensor.value()]), MemoryController.__sensors))