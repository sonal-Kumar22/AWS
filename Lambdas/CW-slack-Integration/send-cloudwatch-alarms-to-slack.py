import urllib3
import boto3 
import json
import os


#slack_url = "" #secrets --
client = boto3.client('secretsmanager')
#secret_name = os.environ['SECRET_NAME']
secret_name = os.getenv('SECRET_NAME')

http = urllib3.PoolManager()


def get_alarm_attributes(sns_message):
    alarm = dict()

    alarm['name'] = sns_message['AlarmName']
    alarm['description'] = sns_message['AlarmDescription']
    alarm['reason'] = sns_message['NewStateReason']
    alarm['region'] = sns_message['Region']
    alarm['instance_id'] = sns_message['Trigger']['Dimensions'][0]['value'] #queue name
    alarm['state'] = sns_message['NewStateValue']
    alarm['previous_state'] = sns_message['OldStateValue']

    return alarm


def register_alarm(alarm):
    return {
        "type": "home",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":warning: " + alarm['name'] + " alarm was registered"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "_" + alarm['description'] + "_"
                },
                "block_id": "text1"
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Queue Name: *" + alarm['instance_id'] + "*"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Region: *" + alarm['region'] + "*"
                    }
                ]
            }
        ]
    }


def activate_alarm(alarm):
    return {
        "type": "home",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":red_circle: Alarm: " + alarm['name'],
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "_" + alarm['reason'] + "_"
                },
                "block_id": "text1"
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Queue Name: *" + alarm['instance_id'] + "*"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Region: *" + alarm['region'] + "*"
                    }
                ]
            }
        ]
    }


def resolve_alarm(alarm):
    return {
        "type": "home",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":large_green_circle: Alarm: " + alarm['name'] + " was resolved",
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "_" + alarm['reason'] + "_"
                },
                "block_id": "text1"
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Queue Name: *" + alarm['instance_id'] + "*"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Region: *" + alarm['region'] + "*"
                    }
                ]
            }
        ]
    }


def handler(event, context):
    #print("Events-")
    #print(json.dumps(event))
    sns_message = json.loads(event["Records"][0]["Sns"]["Message"])
    #print("sns_message-")
    #print(sns_message)
    alarm = get_alarm_attributes(sns_message)

    msg = str()

    if alarm['previous_state'] == "INSUFFICIENT_DATA" and alarm['state'] == 'OK':
        msg = register_alarm(alarm)
    elif alarm['previous_state'] == 'OK' and alarm['state'] == 'ALARM':
        msg = activate_alarm(alarm)
    elif alarm['previous_state'] == 'ALARM' and alarm['state'] == 'OK':
        msg = resolve_alarm(alarm)

    encoded_msg = json.dumps(msg).encode("utf-8")
    #print("encoded_msg-")
    #print(encoded_msg)
    
    response = client.get_secret_value(SecretId=secret_name)
    #print(type(response))
    #print("response-")
    #print(response)
    url = json.loads(response['SecretString'])
    #print(url['slackwebhookurl'])
    
    resp = http.request("POST", url['slackwebhookurl'], body=encoded_msg)
    print(
        {
            "message": msg,
            "status_code": resp.status,
            "response": resp.data,
        }
    )
