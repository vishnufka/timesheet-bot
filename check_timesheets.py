import config as cfg
import get_sheets as cs

month_range = cfg.get_month_range()
first_day_of_month = month_range[0]
month_dates = cfg.get_month_dates_list(month_range[1])
month_days = cfg.get_month_days_list(month_range[1])
day_of_week_dict = cfg.day_of_week_dict


def check_timesheets(user_id):
    this_months_sheets = cs.get_sheets(month_dates, user_id)
    print_array = []
    for day in month_days:
        # -1 because day json starts at 1, but first_day_of_month starts at 0
        day_of_week = (first_day_of_month+int(day)-1) % 7
        date_of_day = month_dates[int(day)-1]
        minutes_this_day = 0
        day_has_sheet = False
        day_result = str(date_of_day) + " " + str(day_of_week_dict[day_of_week])

        if this_months_sheets:
            if this_months_sheets.get(day, None):
                day_has_sheet = True
                for sheet in this_months_sheets[day]:
                    minutes_this_day += this_months_sheets[day][sheet]['minutes']
                hours_this_day = minutes_this_day / 60

                # do not check today
                if cfg.today <= date_of_day:
                    day_result = day_result + " - OK"
                # checking for time over the weekend
                elif day_of_week in (5, 6):
                    if minutes_this_day > 0:
                        day_result = (day_result + " " + str(hours_this_day) + " hours - at the weekend?")
                # checking for less than 8 hours
                elif minutes_this_day < 480:
                    day_result = (day_result + " " + str(hours_this_day) + " hours - less than 8?")
                # checking for more than 8 hours
                elif minutes_this_day > 480:
                    day_result = (day_result + " " + str(hours_this_day) + " hours - more than 8?")
                # otherwise ok
                else:
                    day_result = day_result + " - OK"

        # if the day has no sheet
        if not day_has_sheet:
            # do not check today
            if cfg.today < date_of_day:
                day_result = day_result + " - OK"
            # ok if weekends are missing
            elif day_of_week in (5, 6):
                day_result = day_result + " - OK"
            # otherwise the sheet is missing
            else:
                day_result = day_result + " - MISSING"

        # only print the errors
        if "OK" not in day_result:
            print_array.append(day_result)

    return print_array
