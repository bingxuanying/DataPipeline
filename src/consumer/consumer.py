#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

from kafka import KafkaConsumer  # consumer of events
import boto3
import configparser
import uuid
import json

config = configparser.ConfigParser()
config.read('.env')

# Get the service resource.
session = boto3.Session(
    region_name=config['CREDS']['AWS_REGION_NAME']
)
dynamodb = session.client(
    'dynamodb',
    aws_access_key_id = config['CREDS']['AWS_ACCESS_KEY'],
    aws_secret_access_key = config['CREDS']['AWS_SECRET_KEY']
)

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
consumer = KafkaConsumer (bootstrap_servers="3.82.231.138:9092")

# subscribe to topic
consumer.subscribe (topics=["utilizations"])

# we keep reading and printing
for msg in consumer:
    # what we get is a record. From this record, we are interested in printing
    # the contents of the value field. We are sure that we get only the
    # utilizations topic because that is the only topic we subscribed to.
    # Otherwise we will need to demultiplex the incoming data according to the
    # topic coming in.
    #
    # convert the value field into string (ASCII)
    #
    # Note that I am not showing code to obtain the incoming data as JSON
    # nor am I showing any code to connect to a backend database sink to
    # dump the incoming data. You will have to do that for the assignment.
    res = str(msg.value, 'ascii')
    data = json.loads(res)
    print (data)

    # write value to dynamodb
    dynamodb.put_item(
        TableName='real-time_stock_price',
        Item={
            'id': { 'S': str(uuid.uuid4()) },
            'stock_name':  { 'S': str(data['stock_name']) },
            'stock_price':  { 'S': str(data['stock_price']) },
            'timestamp':  { 'S': str(data['timestamp']) }
        }
    )

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close ()
    






