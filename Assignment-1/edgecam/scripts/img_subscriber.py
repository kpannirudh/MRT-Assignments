#!/usr/bin/env python

import cv2
import rospy
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

bridge = CvBridge()


def callback(image):
    imgfeed = bridge.imgmsg_to_cv2(image)
    edge = cv2.Canny(imgfeed, 100, 200)
    edge_f = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    finalimg = np.hstack((imgfeed, edge_f))
    cv2.imshow('feed', finalimg)
    if cv2.waitKey(1) == ord('q'):
        return


def subnode():
    rospy.Subscriber('imagefeed', Image, callback)
    rospy.init_node('vision', anonymous=True)
    rospy.spin()


if __name__ == '__main__':
    subnode()
