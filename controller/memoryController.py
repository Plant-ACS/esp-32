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
        if (len(MemoryController.__modules) == 0):
            return "no modules have been added so far"
        return_list = []
        list(map(lambda module: return_list.append(str([type(module), module.port, module.value()])), MemoryController.__modules))
        return return_list

    @staticmethod
    def addSensor(sensor):
        print("adding sensor")
        MemoryController.__sensors.append(sensor)
        print(MemoryController.__sensors)

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
        if (len(MemoryController.__sensors) == 0):
            return "no sensors have been added so far"
        return_list = []
        list(map(lambda sensor: return_list.append(str([type(sensor), sensor.port, sensor.value()])), MemoryController.__sensors))
        return return_list