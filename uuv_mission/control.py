import numpy as np
#from uuv_mission.dynamic import get_depth #, __init__
#from dynamic import Submarine, Mission

def get_action(Kd, Kp, prev_error, ref, pos):
    error = ref - pos
    action = Kp*error + Kd*(error-prev_error)
    return action, error