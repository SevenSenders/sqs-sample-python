import boto3

# SQS CLIENT
sqs = boto3.client(
    'sqs',
    region_name='eu-central-1',
    endpoint_url='https://sqs.sevensenders.com/api/v1/shipment-events',
    aws_access_key_id='your-7s-api-key-here', # 7S Shop API Key
    aws_secret_access_key='', # Keep it blank
)

# QUEUE URL
queue_url = sqs.get_queue_url(QueueName='').get('QueueUrl')
print('Queue URL: {}'.format(queue_url))

# Example for receiving messages
response = sqs.receive_message(QueueUrl=queue_url)
messages = response.get('Messages')
print('Messages in Queue: {}'.format(len(messages)))

if messages:
    # Process each message
    for message in messages:
        message_id = message.get('MessageId')
        body = message.get('Body')

        print('{}: {}'.format(message_id, body))

        # Process the message here...

        # Example for deleting messages one by one
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])

    # Example for deleting messages in batch
    # messages_to_delete = [{'Id': str(i), 'ReceiptHandle': msg['ReceiptHandle']} for i, msg in enumerate(messages)]
    # sqs.delete_message_batch(QueueUrl=queue_url, Entries=messages_to_delete)
else:
    print("No messages in the queue.")
