from typing import Self
import math
from dataclasses import dataclass




Scalar = int | float





# TODO
#   Vector Class
#   Force? ^? Class




class MathUtil:
    pass



class Vector:
    pass



class Ellipse:

    def __init__(self, a: Scalar, e: Scalar):
        #TODO, Kwargs only?, take two params and then extrapolate?
        self._a: Scalar = a  # Semi-Major Axis
        self._e: Scalar = e  # Eccentricity

        #Todo, Propertys to extrapolate all of the other values


    @property
    def a(self) -> Scalar:
        return self._a

    @a.setter
    def a(self, val: Scalar):
        #TODO, Do I want to make ellipses immutable?
        self._a = val

    @property
    def e(self) -> Scalar:
        return self._e

    @e.setter
    def e(self, val: Scalar):
        #TODO, Do I want to make ellipses immutable?
        self._e = val


    @property
    def b(self) -> Scalar:
        return self.a * math.sqrt(1 - (self.e ** 2))








@dataclass
class Time:
    Hour: int
    Minute: int
    Second: int


class Date:

    def __init__(self, year: int, month: int, day: int):
        """
        Represents a Date
        :param year:
        :param month:
        :param day:
        """


        self.year = year
        self.month = month
        self.day = day

        assert month <= 12, ValueError("There is no month past december")
        assert month > 0, ValueError()

        assert day <= 31, ValueError()
        assert day > 0, ValueError()



    def __eq__(self, other: Self):
        return (self.year == other.year) and (self.month == other.month) and (self.day == other.day)

    def __lt__(self, other: Self):

        #TODO
        #   Refactor this, yucky

        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def __gt__(self, other: Self):
        return other < self

    def __ge__(self, other: Self):
        return (self > other) or (self == other)

    def __le__(self, other: Self):
        return (self < other) or (self == other)


    def __str__(self) -> str:
        return f"{self.month}/{self.day}/{self.year}"
























