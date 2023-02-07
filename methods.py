import math


def first(first_speed, first_boost, first_length, first_x, second_x, between, max_speed):
    # t = S/ (V — V0)
    _way = (second_x + between + first_length) - first_x
    _time = _way / (max_speed - first_speed) + (max_speed - first_speed) / first_boost
    return _time

