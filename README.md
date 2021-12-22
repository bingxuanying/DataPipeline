# DataPipeline

A simple data analytics pipeline based on Vanderbilt CS5287

## Instruction

### Launch Instance

Launch AWS EC2 with Ubuntu 20.0

Go to security group and set inbound rule to accept incoming traffic to kafka port and zookeeper port from any addresses.

### Env Setup

sudo apt update

sudo apt install -y openjdk-8-jre-headless

sudo apt-get remove scala-library scala
sudo wget https://downloads.lightbend.com/scala/2.12.3/scala-2.12.3.deb
sudo dpkg -i scala-2.12.3.deb
sudo apt-get update
sudo apt-get install scala

curl "https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz" -o kafka.tgz
mkdir ~/kafka && cd ~/kafka
tar -xvzf ~/kafka.tgz --strip 1

### Start Kafka

nano ~/kafka/config/server.properties

~/kafka/bin/zookeeper-server-start.sh ~/kafka/config/zookeeper.properties

~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties

### Start Consumer

git clone https://github.com/asgokhale/CloudComputingCourse.git

nano CloudComputingCourse/ScaffoldingCode/Kafka_GettingStarted/consumer.py

sudo apt-get install -y python3-pip

python3 -m pip install kafka-python
python3 -m pip install boto3
python3 -m pip install yahoo_fin

python3 CloudComputingCourse/ScaffoldingCode/Kafka_GettingStarted/consumer.py
