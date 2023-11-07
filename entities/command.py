class Command:
  def __init__(self):
    self.__commandNames: list[str] = []
    self.__commandFunctions: list[callable] = []
  
  def add(self, name: str, command: callable):
    if name in self.__commandNames:
      raise Exception("the command already exists")
    
    self.__commandNames.append(name)
    self.__commandFunctions.append(command)

  def get(self, name: str) -> callable:
    try:    
      return self.__commandFunctions[self.__commandNames.index(name)]
    except:
      raise Exception("the command does not exist")
  
  def remove(self, name: str) -> bool:
    try:
      i = self.__commandNames.index(name)
    except:
      return False

    self.__commandNames.remove(i)
    self.__commandFunctions.remove(i)
    return True
