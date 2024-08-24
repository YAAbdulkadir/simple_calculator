# -*- coding: utf-8 -*-
import operator
from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(operator.mul, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float("inf")

    def avg(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue

            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    # def avg(self, it, lt=None, ut=None):
    #     if not it:
    #         return 0

    #     if lt is None:
    #         lt = min(it)

    #     if ut is None:
    #         ut = max(it)

    #     _it = [x for x in it if x >= lt and x <= ut]

    #     if not len(_it):
    #         return 0

    #     return sum(_it) / len(_it)
