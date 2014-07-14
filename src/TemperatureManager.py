'''   Temperature Manager

        Arguments: None
        Returns: Mone

'''

class TemperatureManager(object):
    
    def __init__(self, gpioManager):
        
        self._gpioManager = gpioManager
        self._setup()
        
        print "TemperatureManager::init"

    def _setup(self):
        self._initializaMemberAttributes()

    def exit(self):
        print "TemperatureManager::exit"

    def update(self, elapsedTime):
        self.temperature = self._gpioManager.getTemperature()
        self._updateLogic()

    def _initializaMemberAttributes(self):
        self.temperatureMax = 50
        self.hysteresisMargin = 20
        self.coolerState = False

    def _updateLogic(self):
        
        if( self._isHot() and self._isCoolerOff() ):
            self._turnOnCooler()
            self.temperatureMax -= hysteresisMargin

        elif( self._isCold() and self._isCoolerOn() ):
            self._turnOffCooler()
            self.temperatureMax += hysteresisMargin

    def _isHot(self):
        return self.temperature>self.temperatureMax

    def _isCoolerOff(self):
        return not(self.coolerState)

    def _isCold(self):
        return self.temperature<=self.temperatureMax

    def _isCoolerOn(self):
        return self.coolerState

    def _turnOnCooler(self):
        self._gpioManager.turnOnCooler()
        self.coolerState = True
        print "TemperatureManager::_turnOnCooler"

    def _turnOffCooler(self):
        self._gpioManager.turnOffCooler()
        self.coolerState = False
        print "TemperatureManager::_turnOffCooler"








