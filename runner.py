from databaseConnection import database_Upload
from gmailFunctions import getAllMsgIds
from helperClasses import gmail_authenticate
from messageDetails import messageHandler

# get the Gmail API service
service = gmail_authenticate()
messageIds = getAllMsgIds(service)
updatedMessages = messageHandler(messageIds)
database_Upload(updatedMessages)