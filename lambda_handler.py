import boto3
import json

client = boto3.client('lambda')


def lambda_handler(event, context):
    response = client.invoke(
        FunctionName="slack_timesheet_bot",
        InvocationType="Event")
    return {
        'statusCode': 200,
        'body': json.dumps('Task received and executing')
    }
