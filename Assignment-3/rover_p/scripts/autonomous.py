#!/usr/bin/env python

from roboclaw import RoboClaw
import rospy

#---------------------------------------------------- 


class Drive:
    def __init__(self, driver1, driver2):
        self.rightClaw = driver1
        self.leftClaw = driver2

    def drive_callback(self, inp):
        """        
        Problem Statement: Insert Code here to make the rover move 
        forwards, backwards, left, right according to input given
        """
        axes = inp.axes
        buttons = inp.buttons
        if buttons[0] == 1:
            self.rightClaw.BackwardMixed(127)
            self.leftClaw.BackwardMixed(127)
            rospy.loginfo("Rover Direction: Backward")
            rospy.loginfo("RightClaw motors: Backward")
            rospy.loginfo("LeftClaw motors: Backward")
        else:
            if buttons[1] == 1:
                self.leftClaw.ForwardMixed(127)
                self.rightClaw.BackwardMixed(127)
                rospy.loginfo("Rover Turn: Right")
                rospy.loginfo("RightClaw motors: Backward")
                rospy.loginfo("LeftClaw motors: Forward")
            else:
                if buttons[2] == 1:
                    self.rightClaw.ForwardMixed(127)
                    self.leftClaw.BackwardMixed(127)
                    rospy.loginfo("Rover Turn: Left")
                    rospy.loginfo("RightClaw motors: Forward")
                    rospy.loginfo("LeftClaw motors: Backward")
                else:
                    if buttons[3] == 1:
                        self.rightClaw.ForwardMixed(127)
                        self.leftClaw.ForwardMixed(127)
                        rospy.loginfo("Rover Direction: Forward")
                        rospy.loginfo("RightClaw motors: Forward")
                        rospy.loginfo("LeftClaw motors: Forward")
        if buttons[10] == 1:
            return

    def current_limiter(self):
        """
        Try to implement this function as well. It is a saftey feature. 
        How would you decide the current threshold? - Please elaborate
        """
        return False
                

#---------------------------------------------------                



