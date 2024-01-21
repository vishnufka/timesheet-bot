from datetime import datetime as dt
from calendar import monthrange, month_name
import slack
import os

testing = False

today_live = dt.today().date()
today_debug = dt(2020, 5, 15).date()

if testing:
    today = today_debug
else:
    today = today_live
this_month = month_name[today.month]

# instantiate Slack client
slack_client = slack.WebClient(token=os.environ["SLACK_API_TOKEN"])
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# slack params
channel_live = ""
channel_debug = ""
channel_alert = ""
if testing:
    channel = channel_debug
    channel_alert = channel_debug
else:
    channel = channel_live

day_of_week_dict = {
    0: "Mon",
    1: "Tue",
    2: "Wed",
    3: "Thu",
    4: "Fri",
    5: "Sat",
    6: "Sun",
}

# get from url on timestamp user page
user_list = {
    "0000001": "User 1",
    "0000002": "User 2",
    "0000003": "User 3",
    "0000004": "User 4",
    "0000005": "User 5",
    "0000006": "User 6",
    "0000007": "User 7"
}


def get_month_range():
    return monthrange(today.year, today.month)


def get_month_dates_list(month_range):
    month_dates = []
    days_in_month = month_range + 1
    for i in range(1, days_in_month):
        date = dt(today.year, today.month, i).date()
        month_dates.append(date)
    return month_dates


def get_month_days_list(month_range):
    month_days = []
    days_in_month = month_range + 1
    for i in range(1, days_in_month):
        day = str(i)
        month_days.append(day)
    return month_days
