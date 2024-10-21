import numpy as np
from uuv_mission.dynamic import get_depth #, __init__
from dynamic import Submarine, Mission

def get_action(Kp, Kd, t, prev_error):
    height = get_depth(Submarine.self)
    reference = Mission.reference(t)
    error = height - reference
    action = Kp*error + Kd*(error-prev_error)
    return action, error