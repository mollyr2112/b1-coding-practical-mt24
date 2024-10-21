import numpy as np
from uuv_mission.dynamic import get_depth #, __init__
from dynamic import Submarine, Mission

Kp = 0.15
Kd = 0.6
error = 0
prev_error = error

#__init__(self)

height = get_depth(Submarine.self)
reference = Mission.reference(t)

prev_error = error
error = height - reference

action = Kp*error + Kd*(error-prev_error)