# ENEKO HERRERO TABOADA - XAVIER RODRIGUEZ HERNANDEZ
# MOBILE ROBOT NAVIGATION BASED IN Q-LEARNING
# CLASS NXT_CLASS- nxt_class.py

# Importing dependencies
import nxt, nxt.bluesock, nxt.locator, time
from nxt.sensor import *
from nxt.motor import *

# Defining class
class NXT_BRICK(object):
    def __init__(self, address): # Initial parameters
        self.b = nxt.bluesock.BlueSock(address).connect() # Brick object
        self.address = address # Address
        self.m_left = Motor(self.b, PORT_A) # Left motor object
        self.m_right = Motor(self.b, PORT_C) # Right motor object
        self.m_ultrasonic = Motor(self.b, PORT_B) # Ultrasonic motor object
        self.ultrasonic = Ultrasonic(self.b, PORT_1) # Ultrasonic sensor object

    def move_tile(self,power,secs): # "GOING FORWARD" action method
        self.m_right.run(-power)
        self.m_left.run(-power)

        time.sleep(secs)

        self.m_right.idle()
        self.m_left.idle()

    def rotate(self,power,secs): # "ROTATING 90 RIGHT" and "ROTATING 90 LEFT" action method
        self.m_right.run(power)
        self.m_left.run(-power)

        time.sleep(secs)

        self.m_right.idle()
        self.m_left.idle()

    def gf_test_threshold(self,power,threshold): # Method for calibrating distance threshold
        self.m_right.run(-power)
        self.m_left.run(-power)
        c = True
        while c==True:
            distance = self.ultrasonic.get_sample()
            print(distance)
            if distance <= threshold:
                self.emergency_stop()
                c = False
                print("Stop!")

    def spin_around_ultrasonic(self, power, degrees, secs): # Method for spining arround the ultrasonic sensor - NOT USED!
        self.m_ultrasonic.turn(power, degrees,False)
        time.sleep(secs)
        self.m_ultrasonic.turn(-power, degrees,False)
        time.sleep(secs)
        self.m_ultrasonic.turn(-power, degrees,False)
        time.sleep(secs)
        self.m_ultrasonic.turn(power, degrees,False)
        time.sleep(secs)

    def emergency_stop(self): # Emergency stop method
        self.m_left.idle();
        self.m_right.idle();
        self.m_ultrasonic.idle();

    def disconnect(self): # Disconnect socket method
        self.emergency_stop()
        self.b.sock.close()
