#!/bin/bash

python scrapper.py
hdfs dfs -moveFromLocal HELL.txt hdfs://au/user/pk.stradomski-ece/oozie/