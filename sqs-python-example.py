import boto3

# SQS CLIENT
sqs = boto3.client(
    'sqs',
    region_name='eu-central-1',
    endpoint_url='https://develop.analytics-api-dev.7senders.com/queue.xml',
    aws_access_key_id='your-7s-api-key-here', # 7S Shop API Key
    aws_secret_access_key='', # Keep it blank
)

# QUEUE URL
queue_url = sqs.get_queue_url(QueueName='').get('QueueUrl')
print('Queue URL: {}'.format(queue_url))

# MESSAGES
response = sqs.receive_message(QueueUrl='')
messages = response.get('Messages')
print('Messages in Queue: {}'.format(len(messages)))

for message in messages:
    message_id = message.get('MessageId')
    body = message.get('Body')

    print('{}: {}'.format(message_id, body))


