# DataPipeline

A simple data analytics pipeline based on Vanderbilt CS5287

## High Level Diagram

* Host machine, where Virtual Box and Vagrant installed
* Control Host - Ubuntu server created by Vagrant with ansible_local
* AWS EC2 VM 01 - Ubuntu Server with:
  * Zookeeper (single host)
  * Kafka (cluster #0)
* AWS EC2 VM 02 - Ubuntu Server with
  * Kafka (cluster #1)
  * Kafka Consumer written in python.
  * DynomaDB (Switch for CouchDB due to start error)

## Assignment 1-2 Instruction

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

## Assignment 3 Instruction

### How to provision

```shell
# To login to the Control Host
ssh -F ssh-config vagrant

# Inside control host
cd src/ansible
source CH-822922-openrc.sh

# Deploy CouchDB and Kafka Consumer
ansible-palybook -i inventory install_couchdb_palybook.yml
ansible-playbook -i inventory vandy_consumer_playbook.yml

# Start producer
python3 src/producers/producer_amzn.py
python3 src/producers/producer_appl.py

# ssh to the AWS EC2 VM 2 from different terminal
ssh -i ./vu_cs_5287.pem ec2-user@12.134.212.85

# Start Consumer
python3 src/consumer/consumer.py
```

Or:

* Change Vagrant file to use cleanup_cchosts_playbook.yml playbook
* Provision Vagrant:
  
```shell

# From the host machine
vagrant provision
```

To see data in the DynamoDB please add Credentials in Env file
and read data from DynamoDB

### How to cleanup

From the control host (see above)

```shell

# To cleanup installed services (kafka, zookeeper, couchdb)
ansible-palybook -i inventory cleanup_services_playbook.yml

# To destroy Chameleon VMs
ansible-playbook -i inventory cleanup_cchosts_playbook.yml
```

Milestone 1 has example of how it is possible to automate removal of the control host.