#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math
import time

# ÇALIŞTIRMA ADIMLARI
# roscore # TERMİNAL 1
# roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch # TERMİNAL 2
# rosrun basit_uygulamalar deneme.py # TERMİNAL 3

class Rosbot():
     def __init__(self):

        self.rosbot_sub = rospy.Subscriber("/scan", LaserScan, self.scan_callback)
        self.rosbot_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.a = 0.0
        self.b = 0.0
        self.c= 0.0
        self.d= 0.0
        self.ctrl_c = False
        self.vel = Twist()
        self.rate = rospy.Rate(10)
        rospy.on_shutdown(self.shutdownhook)
        

     def scan_callback(self, msg):
         self.a = msg.ranges[180]
         self.b = msg.ranges[int(len(msg.ranges)/2)]
         self.c = msg.ranges[359]
         self.d = msg.ranges[1]

     def shutdownhook(self):

        self.ctrl_c = True
     
     def main(self):
         self.vel.linear.x = 0.25
         self.rosbot_pub.publish(self.vel)
         
         while True:
             print(round(self.d, 2), "metre önünde bir cisim var") 
             if self.d < 1:
                 self.vel.linear.x = 0
                 self.vel.angular.z = -1.2
             else:
                 self.vel.linear.x = 0.25
                 self.vel.angular.z = 0
             
             self.rosbot_pub.publish(self.vel)
             self.rate.sleep()


rospy.init_node('rosbot_test', anonymous=True)
rosbot_object = Rosbot()
try:
    rosbot_object.main()


except rospy.ROSInterruptException:
    pass
