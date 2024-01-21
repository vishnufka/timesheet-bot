import config as cfg
import send_to_slack as sts
import check_timesheets as ct


def main():
    sts.welcome_message()
    for user_id, username in cfg.user_list.items():
        sheet_info = ct.check_timesheets(user_id)
        sts.print_to_slack(username, sheet_info)
    sts.goodbye_message()


def lambda_handler(event, context):
    main()
