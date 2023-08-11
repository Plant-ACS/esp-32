from machine import Timer, Pin
import network
import ubluetooth
from time import sleep, sleep_ms

ble_msg = ""

class Bluetooth():
    def __init__(self, name):
        # Create internal objects for the onboard LED
        # blinking when no BLE device is connected
        # stable ON when connected
        self.led = Pin(2, Pin.OUT)
        self.timer1 = Timer(0)
        
        self.name = name
        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self.disconnected()
        self.ble.irq(self.ble_irq)
        self.register()
        self.advertiser()

    def connected(self):
        self.led.value(1)
        self.timer1.deinit()

    def disconnected(self):        
        self.timer1.init(period=100, mode=Timer.PERIODIC, callback=lambda t: self.led.value(not self.led.value()))

    def ble_irq(self, event, data):
        global ble_msg
        
        if event == 1: #_IRQ_CENTRAL_CONNECT:
                       # A central has connected to this peripheral
            self.connected()

        elif event == 2: #_IRQ_CENTRAL_DISCONNECT:
                         # A central has disconnected from this peripheral.
            self.advertiser()
            self.disconnected()
        
        elif event == 3: #_IRQ_GATTS_WRITE:
                         # A client has written to this characteristic or descriptor.          
            buffer = self.ble.gatts_read(self.rx)
            ble_msg = buffer.decode('UTF-8').strip()
            
    def register(self):        
        # Nordic UART Service (NUS)
        NUS_UUID = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
        RX_UUID = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
        TX_UUID = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'
            
        BLE_NUS = ubluetooth.UUID(NUS_UUID)
        BLE_RX = (ubluetooth.UUID(RX_UUID), ubluetooth.FLAG_WRITE)
        BLE_TX = (ubluetooth.UUID(TX_UUID), ubluetooth.FLAG_NOTIFY)
            
        BLE_UART = (BLE_NUS, (BLE_TX, BLE_RX,))
        SERVICES = (BLE_UART, )
        ((self.tx, self.rx,), ) = self.ble.gatts_register_services(SERVICES)

    def send(self, data):
        self.ble.gatts_notify(0, self.tx, data + 'n')

    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        adv_data = bytearray('x02x01x02') + bytearray((len(name) + 1, 0x09)) + name
        self.ble.gap_advertise(100, adv_data)
        print(adv_data)
        print("rn")

class WiFiManager:
    wifi = network.WLAN(network.STA_IF)
    @staticmethod
    def getList() -> list:
      WiFiManager.wifi.active(True)
      scan_results = WiFiManager.wifi.scan()
      
      wifi_list = []
      for result in scan_results:
          ssid = result[0].decode("utf-8")
          rssi = result[3]
          encrypted = "Open" if result[4] == 0 else "Password"
          
          wifi_info = {
              "ssid": ssid,
              "rssi": rssi,
              "encrypted": encrypted
          }
          wifi_list.append(wifi_info)
      
      return wifi_list
    
    @staticmethod
    def connect(ssid: str, password: str) -> bool:       
        if not WiFiManager.wifi.isconnected():
            WiFiManager.wifi.active(True)
            WiFiManager.wifi.connect(ssid, password)
            print("connecting in wifi: "+ssid)
            print("connect", end="")
            for _ in range(20):
                if WiFiManager.wifi.isconnected():
                    return True
                print(".", end="")
                sleep(1)
        return False
