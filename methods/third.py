# With oncoming overtaking

def third(
        first_speed, first_boost, first_length,
        first_x, second_length, between_1, max_speed_1,
        second_speed, second_boost, fourth_x,
        fourth_speed, fourth_boost, fourth_length,
        between_2, max_speed_4,
        third_speed, third_boost, third_length
):
    # km/h --> m/s

    first_speed *= 1000 / 3600
    max_speed_1 *= 1000 / 3600
    second_speed *= 1000 / 3600
    max_speed_4 *= 1000 / 3600
    third_speed *= 1000 / 3600

    if max_speed_1 > second_speed and (first_speed > second_speed or first_boost > second_boost):
        _first_way = 2 * between_1 + first_length + second_length

        if first_boost == 0:
            _first_time = _first_way / abs(second_speed - first_speed)

        else:
            _first_time = _first_way / abs(second_speed - first_speed) + (second_speed - first_speed) / first_boost

        if max_speed_4 > third_speed and (fourth_speed > third_speed or fourth_boost > third_boost):
            _second_way = 2 * between_2 + third_length + fourth_length

            if fourth_boost == 0:
                _second_time = _second_way / abs(third_speed - fourth_speed)

            else:
                _second_time = _second_way / abs(third_speed - fourth_speed) + abs(third_speed - fourth_speed) / \
                               fourth_boost

        _time = max(_first_time, _second_time)

        _new_first_x = first_x + first_speed * _time + (first_boost * _time ** 2) / 2
        _new_fourth_x = fourth_x + fourth_speed * _time + (fourth_boost * _time ** 2) / 2

        if _new_first_x < _new_fourth_x:
            return _time
        else:
            return 'smash'
