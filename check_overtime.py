import config as cfg
import get_sheets as cs

today = cfg.today
month_range = cfg.get_month_range()
first_day_of_month = month_range[0]
month_dates = cfg.get_month_dates_list(month_range[1])
day_of_week_dict = cfg.day_of_week_dict


# check overtime
def check_overtime_helper():
    print("OVERTIME CHECK " + str(cfg.this_month) + " " + str(today.year))
    for user_id, username in cfg.user_list.items():
        this_months_sheets = cs.get_sheets(month_dates, user_id)

        overtime_return_array = check_overtime(this_months_sheets)
        overtime_hours = overtime_return_array[0]
        overtime_print_array = overtime_return_array[1]
        if overtime_print_array[0] != "OK":
            print(username)
            for el in overtime_print_array:
                print(el)
            print(str(overtime_hours) + " total")


def check_overtime(this_months_sheets):
    has_overtime = False
    overtime_hours = 0
    overtime_print_array = []
    for day in this_months_sheets:
        minutes_this_day = 0
        date_today = this_months_sheets[day]['1']['day']
        # -1 because day json starts at 1, but first_day_of_month starts at 0
        day_of_week = (first_day_of_month+int(day)-1) % 7
        for sheet in this_months_sheets[day]:
            if "[Company Name]" not in this_months_sheets[day][sheet]['clientName']:
                minutes_this_day += this_months_sheets[day][sheet]['minutes']
        hours_this_day = minutes_this_day / 60
        if day_of_week in (5, 6):
            has_overtime = True
            overtime_hours += hours_this_day
            overtime_print_array.append(date_today + " " + str(day_of_week_dict[day_of_week]) + " " +
                                        str(hours_this_day) + " hours overtime")
        elif minutes_this_day > 600:
            has_overtime = True
            hours_this_day -= 10
            overtime_hours += hours_this_day
            overtime_print_array.append(date_today + " " + str(day_of_week_dict[day_of_week]) + " " +
                                        str(hours_this_day) + " hours overtime")
    if not has_overtime:
        overtime_print_array.append("OK")

    return [overtime_hours, overtime_print_array]
