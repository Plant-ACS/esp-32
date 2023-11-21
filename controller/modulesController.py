from controller import memoryController

class ModuleController:
    @staticmethod
    def add(jsonDict: dict):
        pass

    @staticmethod
    def remove(port: int):
        memoryController.MemoryController.removeModule(port)