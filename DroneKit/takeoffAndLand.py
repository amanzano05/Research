from dronekit import connect
from dronekit import VehicleMode as DroneMode
import time

print("Connecting to the Drone...")
#myDrone= connect('COM5', wait_ready=False, baud=57600) #this is using telemtry module. make sure is the right port
#for Raspberry pi uncommemt the following
myDrone = connect('/dev/ttyAMA0', wait_ready= True, baud=921600)
myDrone.wait_ready('autopilot_version')
#myDrone.wait_ready(True, timeout=300)

print("version: %s" %myDrone.version)
print("Position: %s" %myDrone.location.global_frame)
print("Altitude: ", myDrone.location.global_relative_frame.alt )

def takeOff(Altitude):
    #dont arm until ardupilot is ready
    print("Pre-arm chekcks...")
    myDrone.mode    = DroneMode("GUIDED")
    while not myDrone.is_armable :
        print("Waiting for drone to initialise...")
        time.sleep(0.2)
           
    myDrone.armed   = True    
    print("initialized")      
    while not myDrone.armed:
        print("Waiting for arming...")
        time.sleep(1)
    print("armed")
        
    print("Taking off!....")
    
    myDrone.simple_takeoff(Altitude)
    
    while True:
        print("Altitude: ", myDrone.location.global_relative_frame.alt )
        
        if myDrone.location.global_relative_frame.alt>=Altitude * 0.95:
            print("Altitude reached...")
            break
        time.sleep(1)
    






##################main################
takeOff(3)
print("Take off completed")
time.sleep(10)
print("Overing Completed")
print("Landing...")
myDrone.mode=DroneMode("LAND")
print("Mission Completed...")

myDrone.mode=DroneMode("GUIDED")
myDrone.arm=True
myDrone.close()