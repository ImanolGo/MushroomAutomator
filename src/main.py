from MushroomAutomatorApp import MushroomAutomatorApp

def main():
    
    mushroomAutomatorApp = MushroomAutomatorApp()

    try:  
         mushroomAutomatorApp.run() 
          
    except KeyboardInterrupt:  
        mushroomAutomatorApp.callWhenKeyInterrupt()
      
    except:  
       	mushroomAutomatorApp.callWhenOtherExceptions()
       	raise
      
    finally:  
        mushroomAutomatorApp.callWhenFinally()


if __name__ == "__main__":
    main()


