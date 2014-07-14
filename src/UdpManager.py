'''   UDP Manager

        Arguments: None
        Returns: Mone


'''
import socket

class UdpManager(object):
    
    def __init__(self, gpioManager):
        
        self._gpioManager = gpioManager
        self._setup()
        
        print "UdpManager::init"

    def _setup(self):
        self._initializaMemberAttributes()
        self._setupUdpSocket()
        self._updateLogic()

    def exit(self):
        print "UdpManager::exit"

    def update(self, elapsedTime):
        self._updateUdpMessage()

    def _updateLogic(self):
    
        if( self.data == "CoolerOn" ):
            self._gpioManager.turnOnCooler()

        elif( self.data == "CoolerOff" ):
            self._gpioManager.turnOnCooler()
        
        elif( self.data == "HimidifierOn" ):
            self._gpioManager.turnOnHumidifier()
        
        elif( self.data == "HimidifierOff" ):
            self._gpioManager.turnOffHumidifier()

    def _initializaMemberAttributes(self):
        self.port = 5000 
        self.data = " "

    def _setupUdpSocket(self):
        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpSocket.bind(("", self.port))
        print "UdpManager::_setupUdpSocket-> Listening to port: " , port

    def _updateUdpMessage(self):
        self.data, self.addr = self.udpSocket.recvfrom(1024)
        print "UdpManager::_updateUdpMessage-> data: " , self.data









