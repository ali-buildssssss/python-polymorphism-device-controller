class car:
    def start(self):
        print("car is starting")
    def stop(self):
        print("car is stopping")

class mobile:
    def start(self):
        print("mobile is starting")
    def stop(self):
        print("mobile is stopping")
class speaker:
    def start(self):
        print("speaker is starting")
    def stop(self):
        print("speaker is stopping")
        

car1=car()
mobile1=mobile()
speaker1=speaker()

devices=[car1,mobile1,speaker1]


    
        
      
def start_devices(device):
        device.start()
        

def stop_devices(device):
        device.stop()
while True:
    print("enter 1 for start devices")
    print("enter 2 for stop device")
    print("enter 3 for quitint")
    try:
        choices=int(input("enter your choices"))
    except ValueError:
        print("invalid! you entered text ot float")
    print(f"you enter choice {choices}")
    
    if choices==1:
        
        
        print("start devices")

        for device in devices:
         start_devices(device)
        print("_"*30)
    if choices==2:
        

      print("stop devices")
      for device in devices:
         stop_devices(device)  
    
    if choices==3:
        print("quiting...")
        break      
