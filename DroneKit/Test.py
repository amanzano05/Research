from dronekit import connect
import time


def Position_callback(self, attr_name, msg):
    print("Position: %s" %msg)
    


myDrone = connect('/dev/ttyAMA0', wait_ready= True, baud=921600)
myDrone.wait_ready('autopilot_version')
print("Ardupilot version: %s" %myDrone.version)
print("Position: %s" % myDrone.location.global_frame)

myDrone.add_attribute_listener('location.global_frame', Position_callback) #-- message type, callback function
time.sleep(30)

myDrone.remove_attribute_listener('location.global_frame', Position_callback)





myDrone.close()

