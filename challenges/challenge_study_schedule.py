def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    students_count = 0

    for period in permanence_period:
        if not (isinstance(period[0], int)
                and isinstance(period[1], int)):
            return None
        if target_time >= period[0] and target_time <= period[1]:
            students_count += 1
    return students_count
