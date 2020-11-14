#try:
import os
import sys
import numpy as np
#except Exception as e:
    #print("Some of the required libraries are missing! {}".format(e))

# action 0 means new preset
# action preset_name means load said preset
# action 1 preset_name means
#action = input("")

try:
    data = np.linspace(0,1,201)
    np.savetxt('preset_data.dat', data)
    print("hello")
except Exception:
    print("Error")
