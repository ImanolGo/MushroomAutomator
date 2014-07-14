'''   GPIO Manager

        Arguments: None
        Returns: None

'''

import Adafruit_DHT
import RPi.GPIO as GPIO

class PinNum(object):
    NONE = 0
    _1 = 11  #I2C0_SDA
    _2 = 12  #I2C0_SCL
    _3 = 23  #GPCLK0
    _4 = 7 #GPIO
    _5 = 5 #PCM_CLK
    _6 = 13 #GPIO
    _7 = 15 #GPIO
    _8 = 16 #GPIO
    _9 = 18 #GPIO
    _10 = 19 #SPI0_MOSI
    _11 = 21 #SPI0_MISO
    _12 = 22 #GPIO
    _13 = 3 #SPI0_SCLK
    _14 = 24 #SPI0_CEO_N
    _15 = 26 #SPI0_CE1_N


class GpioManager(object):
    
    def __init__(self):
        
        self._initializaMemberAttributes()
        self._setupGPIO()
        print "GpioManager::init"

    def exit(self):
        GPIO.cleanup() # this ensures a clean exit 
        print "GpioManager::exit"

    def update(self, elapsedTime):
        self._readDhtSensor()

    def _initializaMemberAttributes(self):
        self.sensor = Adafruit_DHT.DHT22
        self.SENSOR_PIN = PinNum._9
        self.HUMIDIFIER_PIN = PinNum._7
        self.COOLER_PIN = PinNum._4

        self.humidity = 0.0f
        self.temperature = 0.0f

    def _setupGPIO(self):
     
        print "GpioManager::Revision Board: " + str(GPIO.RPI_REVISION)
        print "GpioManager::RPi GPIO version: " + str(GPIO.VERSION)

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.HUMIDIFIER_PIN, GPIO.OUT)
        GPIO.setup(self.COOLER_PIN, GPIO.OUT)

        GPIO.output(HUMIDIFIER_PIN, GPIO.LOW)
        GPIO.output(COOLER_PIN, GPIO.LOW)
       
    def _readDhtSensor(self):
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        print "GpioManager::_readSensor"
        print("GpioManager:: humidity = %f ,temperature = %f " % (self.humidity, self.temperature))

    def getHumidity(self):
        return self.humidity

    def getTemperature(self):
        return self.temperature

    def turnOnHumidifier(self):
        GPIO.output(HUMIDIFIER_PIN, GPIO.HIGH)

    def turnOffHumidifier(self):
        GPIO.output(HUMIDIFIER_PIN, GPIO.LOW)

    def turnOnCooler(self):
        GPIO.output(COOLER_PIN, GPIO.HIGH)

    def turnOffCooler(self):
        GPIO.output(COOLER_PIN, GPIO.LOW)








