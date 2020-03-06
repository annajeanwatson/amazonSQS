import logging
import boto3
from botocore.exceptions import ClientError


def send_sqs_message(sqs_queue_url, msg_body):
    """
    :param sqs_queue_url: String URL of existing SQS queue
    :param msg_body: String message body
    :return: Dictionary containing information about the sent message. If
        error, returns None.
    """

    # Send the SQS message
    sqs_client = boto3.resource('sqs')
    queue = sqs_client.get_queue_by_name(QueueName='ec21.fifo')
    try:
        msg = queue.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=msg_body, MessageGroupId='string', MessageDeduplicationId='string')
    except ClientError as e:
        logging.error(e)
        return None
    return msg


def main():
    """Exercise send_sqs_message()"""

    # Assign this value before running the program
    sqs_queue_url = 'https://sqs.us-east-2.amazonaws.com/630265412085/ec21.fifo'

    # Send some SQS messages
    for i in range(1, 6):
        msg_body = 'SQS message'
        msg = send_sqs_message(sqs_queue_url, msg_body)


if __name__ == '__main__':
    main()