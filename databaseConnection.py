import boto3
from time import sleep
from boto3.dynamodb.conditions import Key


# function for uploading to the dynamodb weather info table
def database_Upload(messages):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('gmailAPI')

    print('Writing to DB')

    with table.batch_writer() as batch:
        for count, msg in enumerate(messages):
            batch.put_item(
                Item={
                    'messageID' : msg[0],
                    'email' : 't.cohen.6229@gmail.com',
                    'sender' : msg[1],
                    'subject' : msg[2],
                    # 'body' : msg[3]
                }
            )

            if count % 500 == 0:
                print('Sleeping 15')
                sleep(15)
                print('Sleeping Done')

    print('DB Done!')