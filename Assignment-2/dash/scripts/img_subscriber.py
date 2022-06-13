#!/usr/bin/env python

import cv2
import rospy
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

bridge = CvBridge()


def callback(image):
    imgfeed = bridge.imgmsg_to_cv2(image)
    imgG = cv2.cvtColor(imgfeed, cv2.COLOR_RGB2BGR)
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_1000)
    arucoParams = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(imgfeed, arucoDict, parameters=arucoParams)
    cv2.aruco.drawDetectedMarkers(imgG, corners, ids)
    cv2.imshow('feed', imgG)
    if cv2.waitKey(1) == ord('q'):
        return


def subnode():
    rospy.Subscriber('/camera/rgb/image_raw', Image, callback)
    rospy.init_node('ar_vision', anonymous=True)
    rospy.spin()


if __name__ == '__main__':
    subnode()
