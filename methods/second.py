# With oncoming traffic

def second(
        first_speed, first_boost, first_length,
        second_length, between,
        max_speed, second_speed, second_boost,
        third_speed, third_boost, third_between
):
    first_speed *= 1000 / 3600
    max_speed *= 1000 / 3600
    second_speed *= 1000 / 3600
    third_speed *= 1000/3600

    first_x = 0
    second_x = first_x + between + second_length
    third_x = second_x + third_between

    if max_speed > second_speed and (first_speed > second_speed or first_boost > second_boost):

        _way = 2 * between + first_length + second_length

        if first_boost == 0:
            _time = _way / abs(second_speed - first_speed)

        else:
            _time = _way / abs(second_speed - first_speed) + (second_speed - first_speed) / first_boost

        _new_first_x = first_x + first_speed * _time + (first_boost * (_time ** 2)) / 2
        _new_third_x = third_x - third_speed * _time - (third_boost * (_time ** 2)) / 2

        if _new_first_x < _new_third_x:
            return abs(round(_time, 2))

        return 'smash'

