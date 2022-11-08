from dronekit import *
import time
vehicle=connect('127.0.0.1:14551',baud=921600,wait_ready=True)
def arm_takeoff(height):
    while not vehicle.is_armable:
        print("waiting for drone")
        time.sleep(1)
    print("arming")
    vehicle.mode=VehicleMode('GUIDED')
    vehicle.armed=True
    while not vehicle.armed:
            print("Drone arming...")
            time.sleep(1)
    if(vehicle.armed):
        print("Vehicle is armed")
    else:
        print("Vehicle is not armed")
    print("takeoff")
    vehicle.simple_takeoff(height)
    while True:
        print("Reached: ",vehicle.location.global_relative_frame.alt)
        if(vehicle.location.global_relative_frame.alt>=height*0.98):
            print("reached")
            break
        time.sleep(1)
arm_takeoff(50)
print('Hovering')
time.sleep(10)
print("preparing to decend")
vehicle.mode=VehicleMode("RTL")
print(vehicle.location.global_relative_frame.alt)
while vehicle.location.global_relative_frame.alt>=0.5:
    print("landing...", vehicle.location.global_relative_frame.alt)
    time.sleep(1)
print("resting")
time.sleep(5)
vehicle.armed=False
while vehicle.armed:
    print("diasming...")
print("closing communtication with drone")
vehicle.close()