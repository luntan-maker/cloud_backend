import json
import boto3
from datetime import datetime as dt

my_link = "*"
# my_link = "https://myawsbucket-forcloudresumechallenge.s3.amazonaws.com/index.html"

def lambda_handler2(event, context):
    ip = event['queryStringParameters']['ip']
    date = dt.now().isoformat()

    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(
        TableName="user",
        Item={
            'User':{'S': ip},
            'Date':{'S': date}
        })
    return{
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "*",
            'Access-Control-Allow-Origin': my_link,#'*',
            'Content-Type': 'text/html',
        },
        "body": json.dumps({
            "personId": "worked?",
        })
    }

def lambda_handler(event, context):
    id="userCount"
    client = boto3.client('dynamodb', 'us-east-1')
    response = client.describe_table(TableName='user')

    return{
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "*",
            'Access-Control-Allow-Origin': my_link,#'*',
            'Content-Type': 'text/html',
        },
        "body": json.dumps({
            "UserCount": response['Table']['ItemCount'],
        })
    }