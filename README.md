# big_data_ecosystem_g7

## Team members




##Steps
1. Clone git repo in ssh

2. Install the required python libraries (praw, pandas):

pip install praw pandas

3. Run scrapper.py in ssh:

python3.6 scrapper.py

4. Modify the job.properties file in the oozie folder with appropriate Username for Cluster and Hive

5. Put the oozie in HDFS:

hdfs dfs -put -f oozie/ "/user/$USER"

6. Copy the posts.csv into HDFS:

hdfs dfs -mkdir -p "/education/ece_2022_fall_bda_1/$USER/reddit_data"

hdfs dfs -put -f posts.csv "/education/ece_2022_fall_bda_1/$USER/reddit_data/posts.csv"

7. Run the oozie job:

oozie job -run -config oozie/job.properties -oozie http://oozie-1.au.adaltas.cloud:11000/oozie

