from databaseConnection import database_Upload
from gmailFunctions import getAllMsgIds
from helperClasses import gmail_authenticate
from messageDetails import messageHandler



# get the Gmail API service
service = gmail_authenticate()
messageIds = getAllMsgIds(service)
updatedMessages = messageHandler(messageIds)
# updatedMessages = messageHandler(['187497b30a5cd956','18753f1e5cc40043'])
database_Upload(updatedMessages)
print(updatedMessages)