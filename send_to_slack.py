import config as cfg


def format_sheet_info(username, sheet_info):
    response = username
    response += "\n\n"
    response += "\n".join([line for line in sheet_info])
    response += "\n------------------------------------"
    return response


def print_to_slack(username, sheet_info):
    message = format_sheet_info(username, sheet_info)
    post_to_slack(cfg.channel, message)


def welcome_message():
    message = "TIMESHEET CHECK - " + str(cfg.today)
    post_to_slack(cfg.channel, message)


def goodbye_message():
    message = "I just posted in #timesheets!"
    post_to_slack(cfg.channel_alert, message)


def post_to_slack(channel, message):
    cfg.slack_client.chat_postMessage(
        channel=channel,
        text=message,
        as_user=True)
