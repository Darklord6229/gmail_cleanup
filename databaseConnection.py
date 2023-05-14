import os
import boto3
from time import sleep


# function for uploading email content to dynamodb
def database_Upload(messages):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('gmailAPI')

    print('Writing to DB')

    with table.batch_writer() as batch:
        for count, msg in enumerate(messages):
            batch.put_item(
                Item={
                    'messageID' : msg[0],
                    'email': os.getenv('email'),
                    'sender': msg[1],
                    'subject': msg[2],
                }
            )
            # batch speed delay for handling rate limiting
            if count % 500 == 0 & count != 0:
                print('Sleeping 15')
                sleep(15)
                print('Sleeping Done')

    print('DB Done!')