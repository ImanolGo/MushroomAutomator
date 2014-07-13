'''   Mushroom Automator App

        Arguments: None
        Interface: run 

        Returns: None

'''

import socket
import time

from HumidityManager import HumidityManager
from TemperatureManager import TemperatureManager


class MushroomAutomatorApp(object):
    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    # Here, we'll initialize some of the data.
    def __init__(self):
        # Let's add some data to the [instance of the] class.
        
        self._initializaMemberAttributes()
        self._createManagers()
        self._setButtonActions()
        self._setUdpReceiver()
        self._setSystemToDefaultLanguage()

        print "MushroomAutomatorApp::init"

    def _initializaMemberAttributes(self):
        self.elapsedTime = 0
        self.start = time.clock()

    def _createManagers(self):
        self.temperatureManager = TemperatureManager()
        self.humidityManager = HumidityManager()

    def callWhenKeyInterrupt(self):
        # exits when you press CTRL+C  
        print "\nCTRL+C  pressed!!!\nExit program"
        self._exitManagers()

    def callWhenOtherExceptions(self):
        # this catches ALL other exceptions including errors.  
        # You won't get any error messages for debugging  
        # so only use it once your code is working  
        print "Error or exception occurred!"  
        self._exitManagers()

    def callWhenFinally(self):
        self._exitManagers()

    def _exitManagers(self):
        self.temperatureManager.exit()
        self.humidityManager.exit()

    def run(self):
        print "MediaPlayerLanguageSelector::run"
        
        while True:
            self._mainLoop() 
        
    def _mainLoop(self):
        self.updateElapsedTime()
        self._updateManagers()
      
    def updateElapsedTime(self):
        self.elapsedTime = (time.clock() - self.start)
        self.start = time.clock()

    def _updateManagers(self):
        self.humidityManager.update(self.elapsedTime)
        self.temperatureManager.update(self.elapsedTime)

