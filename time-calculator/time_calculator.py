def add_time(start, duration, start_day=None):
    WEEK = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    ]
    # Adjust start time
    start_split = start.split(" ")
    start_times = start_split[0].split(":")

    start_hour = int(start_times[0])
    start_minute = int(start_times[1])

    if start_split[1] == "PM":
        start_hour += 12

    # Adjust duration time
    duration_times = duration.split(":")

    duration_hour = int(duration_times[0])
    duration_minute = int(duration_times[1])

    # Convert to 12 hour time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour
    day_counter = 0

    while end_minute > 59:
        end_hour += 1
        end_minute -= 60

    while end_hour >= 24:
        day_counter += 1
        end_hour -= 24

    # Process times
    if end_minute < 10:
        final_minute = f"0{end_minute}"
    else:
        final_minute = end_minute

    if end_hour == 0:
        final_hour = 12
        am_pm = "AM"
    elif end_hour == 12:
        final_hour = end_hour
        am_pm = "PM"
    elif end_hour < 12:
        final_hour = end_hour
        am_pm = "AM"
    else:
        final_hour = end_hour - 12
        am_pm = "PM"

    # Create string
    new_time = f"{final_hour}:{final_minute} {am_pm}"

    if start_day:
        for i, day in enumerate(WEEK):
            if start_day.lower() == day:
                end_day_idx = i + day_counter

        while end_day_idx > 6:
            end_day_idx -= 7

        final_day = WEEK[end_day_idx].title()

        new_time += f", {final_day}"

    if day_counter == 1:
        new_time += " (next day)"
    elif day_counter > 1:
        new_time += f" ({day_counter} days later)"

    return new_time
