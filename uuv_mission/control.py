import numpy as np
from uuv_mission.dynamic import get_depth
from dynamic import Submarine, Mission

Kp = 0.15
Kd = 0.6
error = 0
prev_error = error

height = get_depth(self)
reference = Mission.reference(t)

prev_error = error
error = height - reference

action = Kp*error + Kd*(error-prev_error)