from time import sleep
from machine import ADC, Pin

class Module:
   def __init__(self, port: int):
      self._port = port
   

class Relay(Module):
   def __init__(self, port: int):
      self._pin = Pin(port, Pin.OUT)
     
   def setValue(self, on: bool):
      self._pin.value(on)

   def onIn(self, time: int):
      self.setValue(0)
      sleep(time)
      self.setValue(1)