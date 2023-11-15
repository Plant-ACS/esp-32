from time import sleep
from machine import ADC, Pin

class Module:
   pass

class Relay(Module):
   def __init__(self, port: int):
      self._pin = Pin(port, Pin.OUT)
     
   def setValue(self, on: bool):
      self._pin.value(on)

   def onIn(self, time: int):
      self.setValue(1)
      sleep(time)
      self.setValue(0)