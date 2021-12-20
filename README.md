# DataPipeline
A simple data analytics pipeline based on Vanderbilt CS5287

## Instruction

### Launch Instance

Launch AWS EC2 with Ubuntu 20.0

Go to security group and set inbound rule to accept incoming traffic to kafka port and zookeeper port from any addresses.

### Env Setup

sudo apt update

sudo apt install openjdk-8-jre-headless

sudo apt-get remove scala-library scala
sudo wget https://downloads.lightbend.com/scala/2.12.3/scala-2.12.3.deb
sudo dpkg -i scala-2.12.3.deb
sudo apt-get update
sudo apt-get install scala

curl "https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz" -o kafka.tgz
mkdir ~/kafka && cd ~/kafka
tar -xvzf ~/kafka.tgz --strip 1