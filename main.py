from classdefs import *
from juilian_date import jd_calc
from timeCon import *
import math


HWD = Date(2023, 9, 18)

jd = jd_calc(HWD)


LST_SO = GST_to_LST(HWD, -71.34)
print(LST_SO)

def eclipt(RA, DEC):
    # Required as Python operates using Radians
    RA = math.radians(RA)
    DEC = math.radians(DEC)
    e = 23.441884
    E = math.radians(e)
    eLong = math.atan(
        (math.sin(RA) * math.cos(E) + math.tan(DEC) * math.sin(E)) /
        math.cos(RA)
    )

    eLat = math.asin(
        math.sin(DEC) * math.sin(E) - math.cos(DEC) * math.sin(E) * math.sin(RA)
    )
    return eLong, eLat



A_RA = (16, 29, 24)

A_DEC = (-26, -25, -55)



print(
    eclipt(
        Norm_to_decHour(*A_RA),
        Norm_to_decHour(*A_DEC)
    )
)


















