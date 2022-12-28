#!/bin/bash

echo "foo" > HELL.txt
hdfs dfs -moveFromLocal HELL.txt hdfs://au/user/pk.stradomski-ece/oozie/