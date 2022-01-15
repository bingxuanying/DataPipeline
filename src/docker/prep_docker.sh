#!/bin/bash

openssl req -newkey rsa:4096 -nodes -sha256 \
    -subj "/CN=t12-p3-vm01" \
    -addext "subjectAltName = DNS:t12-p3-vm01" \
    -x509 -days 365 \
    -keyout ./certs/docker_registry.key \
    -out ./certs/docker_registry.crt

tar zcf docker_cluster.tgz DockerCluster_wKubernetes certs
