from threading import Thread
from numpy import array_split
from helperClasses import gmail_authenticate
import base64

class messageDetails(Thread):
    def __init__(self,messageIds,threadNum):
        Thread.__init__(self)
        self.messageIds = messageIds
        self.threadNum = threadNum
        self.value = None

    def run(self):
        service = gmail_authenticate()
        messages = []
        # decoded_data = None

        for count, id in enumerate(self.messageIds):
            result = service.users().messages().get(userId='me', id=id).execute()

            try:
                payload = result['payload']
                headers = payload['headers']

                for d in headers:
                    if d['name'] == 'Subject':
                        subject = d['value']
                    if d['name'] == 'From':
                        sender = d['value']

                # parts = payload.get('parts')[0]
                # data = parts['body']['data']
                # data = data.replace("-", "+").replace("_", "/")
                # decoded_data = base64.b64decode(data)


            except:
                pass

            messages.append((id, sender, subject))

            if count % 100 == 0:
                print('Thread ' + str(self.threadNum) + ' Currently At ' + str(count) + ' Out Of ' + str(len(self.messageIds)))

        self.value = messages


def messageHandler(messageIds):
    # splits data into 4 threads and fires off the message calls
    # then rejoins the data into one list
    splitLists = array_split(messageIds,4)

    t1 = messageDetails(splitLists[0],1)
    t2 = messageDetails(splitLists[1],2)
    t3 = messageDetails(splitLists[2],3)
    t4 = messageDetails(splitLists[3],4)

    print('Fetching message details')
    print('Thread 1 start')
    t1.start()
    print('Thread 2 start')
    t2.start()
    print('Thread 3 start')
    t3.start()
    print('Thread 4 start')
    t4.start()

    print('All threads running pulling the data in. ')
    t1.join()
    print('Thread 1 done')
    t2.join()
    print('Thread 2 done')
    t3.join()
    print('Thread 3 done')
    t4.join()
    print('Thread 4 done')

    combinedList = t1.value + t2.value + t3.value + t4.value
    return combinedList