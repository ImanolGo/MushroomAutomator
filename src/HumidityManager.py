'''   Humidity Manager

        Arguments: None
        Returns: None

'''

import GpioManager

class HumidityManager(object):
    
    def __init__(self, gpioManager):
        
        self._gpioManager = gpioManager
        self._setup()
        
        print "HumidityManager::init"

    def _setup(self):
        self._initializaMemberAttributes()

    def exit(self):
        print "HumidityManager::exit"

    def update(self, elapsedTime):
        self.humidity = self._gpioManager.getHumidity()
        self._updateLogic()

    def _initializaMemberAttributes(self):
        self.humidityMin = 30
        self.hysteresisMargin = 30
        self.humidifierState = False

    def _updateLogic(self):
        
        if( self._isDry() and self._isHumidifierOff() ):
            self._turnOffHumidifier()
            self.humidyMinimun += hysteresisMargin

        elif( self._isHumid() and self._isHumidifierOn() ):
            self._turnOnHumidifier()
            self.humidyMinimun -= hysteresisMargin

    def _isDry(self):
        return self.humidity<self.humidityMin

    def _isHumidifierOn(self):
        return self.humidifierState

    def _isHumid(self):
        return self.humidity>=self.humidityMin

    def _isHumidifierOff(self):
        return not(self.humidifierState)

    def _turnOnHumidifier(self):
        self._gpioManager.turnOnHumidifier()
        self.humidifierState = True
        print "HumidityManager::_turnOnHumidifier"

    def _turnOffHumidifier(self):
        self._gpioManager.turnOffHumidifier()
        self.humidifierState = False
        print "HumidityManager::_turnOffHumidifier"








