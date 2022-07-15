#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from inputs import get_gamepad


def pubnode():
    pub = rospy.Publisher('joy_msg', String, queue_size=1)
    rospy.init_node('base', anonymous=True)
    rate = rospy.Rate(30)
    joy_msg = "NONE"
    while not rospy.is_shutdown():
        [event] = get_gamepad()
        button_codes = ["BTN_TRIGGER", "BTN_THUMB", "BTN_THUMB2", "BTN_TOP"]
        messages = ["FORWARD", "RIGHT", "BACKWARD", "LEFT"]
        for i in range(len(button_codes)):
            if event.ev_type == "Key" and event.code == button_codes[i]:
                if event.state == 1:
                    joy_msg = messages[i]
                else:
                    joy_msg = "NONE"
        pub.publish(joy_msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        pubnode()
    except rospy.ROSInterruptException():
        pass
