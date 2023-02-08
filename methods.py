import math


def first(first_speed, first_boost, first_length, first_x, second_x, between, max_speed, second_speed):
    if max_speed > second_speed:
        _way = (second_x + between + first_length) - first_x
        _time = _way / (max_speed - first_speed) + (max_speed - first_speed) / first_boost
        return _time


def second(first_speed, first_boost, first_length, first_x, second_x, between, max_speed, second_speed, third_x,
           third_speed, third_boost):
    if max_speed > second_speed:
        _way = (second_x + between + first_length) - first_x
        _time = _way / (max_speed - first_speed) + (max_speed - first_speed) / first_boost
        _new_first_x = first_x + first_speed * _time + (first_boost * (_time ** 2)) / 2
        _new_third_x = third_x - third_speed * _time - (third_boost * (_time ** 2)) / 2
        print(_new_first_x, _new_third_x)
        print(_time)
        if _new_third_x > _new_first_x:
            return _time
        return 'smash'
