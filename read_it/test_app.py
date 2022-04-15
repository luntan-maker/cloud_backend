import boto3

def test_table_exists():
    dynamodb = boto3.client('dynamodb')
    tables = dynamodb.list_tables()['TableNames']
    assert ((len(tables)==1) and ('user' in tables))
def test_db_size():
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.describe_table(TableName='user')
    assert response['Table']['ItemCount'] >= 0
    
def test_api_gateway():
    client = boto3.client('apigateway')
    api = "uddkyyt448"
    output = client.get_resources(
        restApiId=api
    )
    assert output['ResponseMetadata']['HTTPStatusCode'] == 200
    # Some change to get the push to go through