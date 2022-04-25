#!/usr/bin/env python

import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

cap = cv2.VideoCapture(-1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
bridge = CvBridge()


def pubnode():
    pub = rospy.Publisher('imagefeed', Image, queue_size=1)
    rospy.init_node('webcam', anonymous=True)
    rate = rospy.Rate(30)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        rosmsg = bridge.cv2_to_imgmsg(frame, "bgr8")
        pub.publish(rosmsg)
        if rospy.is_shutdown():
            cap.release()
        rate.sleep()


if __name__ == '__main__':
    try:
        pubnode()
    except rospy.ROSInterruptException():
        pass
