import json
import boto3

def lambda_handler(event, context):
    vehicle_id = event.get('vehicle_id')

    if not vehicle_id:
        return {
            'statusCode': 400,
            'body': json.dumps('Validation Failed: vehicle_id is required')
        }

    # Retrieve the status from DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('VehicleStatusUpdates')
    response = table.get_item(
        Key={
            'vehicle_id': vehicle_id
        }
    )

    item = response.get('Item')

    if not item:
        return {
            'statusCode': 404,
            'body': json.dumps('Vehicle status not found')
        }

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
