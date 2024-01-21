from datetime import datetime as dt
import sys
import os
import json
import requests


def get_sheets(month_dates, user_id):
    time_sheets = get_timesheets_from_server(user_id)

    this_months_sheets = {}
    for i in range(1, 32):
        this_months_sheets[i] = {}

    for sheet in time_sheets:
        date = dt.strptime(sheet['day'], "%Y-%m-%d").date()

        if date in month_dates:
            this_months_sheets[date.day][str(len(this_months_sheets[date.day]) + 1)] = sheet

    for i in list(this_months_sheets):
        if len(this_months_sheets[i]) == 0:
            del this_months_sheets[i]

    this_months_sheets = json.loads(json.dumps(this_months_sheets))

    return this_months_sheets


def get_timesheets_from_server(user_id):
    try:
        headers = {
            'X-API-Key': os.environ["TIMESTAMP_API_TOKEN"],
            'Content-Type': 'application/json; charset=utf-8',
        }

        params = (
            ('userId', user_id),
        )

        response = requests.get('https://api.timestamp.io/api/timeEntries', headers=headers, params=params)

    except requests.ConnectionError:
        print("SCRIPT ABORTED - Server did not respond to request")
        sys.exit()

    return json.loads(response.text)
