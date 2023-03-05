# Without oncoming traffic
def first(
        first_speed, first_boost, first_length,
        between, max_speed, second_speed,
        second_boost, second_length
):
    first_speed *= 1000 / 3600
    max_speed *= 1000 / 3600
    second_speed *= 1000 / 3600

    if max_speed > second_speed and (first_speed > second_speed or first_boost > second_boost):

        _way = 2*between + first_length + second_length
        if first_boost == 0:
            _time = _way / abs(second_speed - first_speed)
        else:
            _time = _way / abs(second_speed - first_speed) + (second_speed - first_speed) / first_boost
        return abs(round(_time, 2))
