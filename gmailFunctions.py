from helperClasses import gmail_authenticate

def getAllMsgIds(service):
    print('Getting All Message IDs')
    messageIds = []

    # Getting first batch of 500 emails and extracting ids
    result = service.users().messages().list(maxResults=500, userId='me').execute()
    messageExtraction(messageIds,result)

    # Looping over the remainder ids and extracting them
    while 'nextPageToken' in result:
        result = service.users().messages().list(maxResults=500, userId='me',
                                                 pageToken=result['nextPageToken']).execute()
        messageExtraction(messageIds,result)

    print("Amount of Emails: " + str(len(messageIds)))
    return messageIds

def messageExtraction(messageIds,result):
    #handles message id extraction
    messages = result.get('messages')
    for msg in messages:
        messageIds.append(msg['id'])
    return messageIds