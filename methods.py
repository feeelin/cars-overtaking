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
        if _new_third_x > _new_first_x:
            return _time
        return 'smash'


def third(first_speed, first_boost, first_length, first_x, second_x, between_1, max_speed_1, second_speed, fourth_x,
          fourth_speed, fourth_boost, fourth_length, third_x, between_2, max_speed_4, third_speed):

    if max_speed_1 > second_speed and max_speed_4 > third_speed:
        _way_1 = (second_x + between_1 + first_length) - first_x
        _time_1 = _way_1 / (max_speed_1 - first_speed) + (max_speed_1 - first_speed) / first_boost

        _way_2 = - (third_x + between_2 + fourth_length) + fourth_x
        _time_2 = _way_2 / (max_speed_4 - fourth_speed) + (max_speed_4 - fourth_speed) / fourth_boost

        _new_first_x = first_x + first_speed * _time_1 + (first_boost * (_time_1 ** 2)) / 2
        _new_fourth_x = fourth_x - fourth_speed * _time_2 - (fourth_boost * (_time_2 ** 2)) / 2

        if _new_fourth_x > _new_first_x:
            return max(_time_1, _time_2)
        return 'smash'

