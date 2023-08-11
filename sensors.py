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
   def __init__(self, port: int, min: int = 0, max: int = 10):
      if max <= 0:
         raise Exception('Min value is greater or equal to max value')
      if self.isSensorConnectedIn(port) == False:
         raise Exception(f"Sensor is not connected in port: {port}")
      self._min = min
      self._max = max
      self._pin = ADC(Pin(port))
      self._pin.width(ADC.WIDTH_10BIT)

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
       
class LCD(Sensor):
   pass

class Humidity(Sensor):
   pass