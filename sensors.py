from machine import ADC, Pin
from time import sleep

class Relay:
   def __init__(self, port: int):
      self._pin = Pin(port, Pin.OUT)
     
   def setValue(self, on: bool):
      self._pin.value(on)

   def onIn(self, time: int):
      self.setValue(1)
      sleep(time)
      self.setValue(0)

class Sensor:
   def __init__(self, port: int, min: int = 0, max: int = 10, kind: str = "sensor"):
      if max <= 0:
         raise Exception('Min value is greater or equal to max value')
      if self.isSensorConnectedIn(port) == False:
         raise Exception(f"Sensor is not connected in port: {port}")
      if (port == 26 or port == 25):
         raise Exception("Ports 25 and 26 are Digital-to-Analog Converters, choose another port")
      self._min = min
      self._max = max
      self._pin = ADC(Pin(port))
      self._pin.width(ADC.WIDTH_10BIT)
      self.kind = kind

   @staticmethod
   def isSensorConnectedIn(pin: int) -> bool:
      analog = ADC(Pin(pin))
      values = []
      for i in range(100):
         values.append(analog.read())
         sleep(0.05)
      
      media = sum(values) / len(values)

      for el in values:
         if el > media +60 or el < media -60:
            return False
      return True
   
   def read(self) -> float:
      value = 0
      for i in range(100):
         value += self._pin.read()
      return value / 100

   def value(self) -> float:
       value = (self.read() / 1023 -1)
       if(value < 0): value *= -1
       return value * (self._max - self._min) + self._min
   
   def getPort(self):
      return self.port
   
   def getKind(self): 
      return self.kind
       
class LDR(Sensor):
   def __init__(self, sensor: Sensor = None, port: int = None, min: int = 0, max: int = 10):
      if (sensor != None):
         super().__init__(sensor.port, sensor.min, sensor.max, "ldr-sensor")
      else:
         super().__init__(port, min, max, "ldr-sensor")

class Moisture(Sensor):
   def __init__(self, sensor: Sensor = None, port: int = None, min: int = 0, max: int = 10):
      if sensor != None:
         super().__init__(sensor.port, sensor.min, sensor.max, "moisture-sensor")
      else:
         super().__init__(port, min, max, "moisture-sensor")
