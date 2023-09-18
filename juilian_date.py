from classdefs import Date, Scalar
from math import trunc






def jd_calc(date: Date) -> Scalar:
    """
    Calculates the Julian date for a given "real" date, returns a scalar
    :param date:
    :return:
    """
    OCT15_1582 = Date(1582, 10, 15)

    if (date.month == 1) or (date.month == 2):
        date.year -= 1
        date.month += 12

    A = trunc(date.year / 100)  # A is int part of y/100


    # B = 0
    # if date >= OCT15_1582:
    #     B = 2 - A + trunc(A / 4)

    B = 2 - A + trunc(A / 4)



    if date.year <= 0:
        C = trunc(365.25 * date.year - .75)
    else:
        C = trunc(365.25 * date.year)

    D = trunc(30.6001 * (date.month + 1))

    return (B + C + D + date.day + 1720994.5) + .5  #Added .5 as to start the day on Noon as is the start of the day
    # for juilan days

















