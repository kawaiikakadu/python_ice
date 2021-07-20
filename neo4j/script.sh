#!/usr/bin/env bash

docker pull docker.elastic.co/elasticsearch/elasticsearch:7.13.3
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.13.3

pip install -r requirements.txt