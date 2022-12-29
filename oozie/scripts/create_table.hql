CREATE EXTERNAL TABLE IF NOT EXISTS ece_2022_fall_bda_${group}.${hiveUsername}_reddit_table (
  subreddit STRING,
  title STRING,
  content STRING,
  link STRING,
  id STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION '/education/ece_2022_fall_bda_${group}/${clusterUsername}/reddit_data'
TBLPROPERTIES ('skip.header.line.count'='1');
