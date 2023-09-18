from classdefs import *
from juilian_date import jd_calc
import math




def decHour_to_Norm(dechour: Scalar):
    Hours = math.floor(dechour)
    Minutes = (dechour - math.floor(dechour)) * 60
    Seconds = (Minutes - math.floor(Minutes)) * 60
    Minutes = math.floor(Minutes)
    Seconds = math.floor(Seconds)
    return Hours, Minutes, Seconds


def Norm_to_decHour(H, M, S):
    return H + (M / 60) + (S / 60)


def UT_to_GST(date: Date) -> tuple[int, int, int, int]:
    """
    returns in (Hour, Minute, Second, Decimal) format
    :param date:
    :return:
    """
    JD = jd_calc(date)
    S = JD - 2451545.0
    T = S / 36525
    T0 = 6.697374558 + 2400.051336 * T + 0.000025862 * T ** 2
    UT = T0 % 24
    UT *= 1.002737909
    UT += T0
    UT %= 24


    Hours, Minutes, Seconds = decHour_to_Norm(UT)


    return Hours, Minutes, Seconds, UT



def GST_to_LST(date: Date, Long: Scalar):
    """
    Long has to be in degrees!
    West Long is Neg, East Long is Positive
    :param date:
    :param Long:
    :return:
    """
    GST = UT_to_GST(date)[3]
    Long /= 15
    GST += Long
    #GST %= 24
    #Need Mod 24?
    H, M, S = decHour_to_Norm(GST)
    return H, M, S, GST





























