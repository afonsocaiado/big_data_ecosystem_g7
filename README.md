# Reddit Data Pipeline

A comprehensive data pipeline that scrapes content from Reddit, processes it using Python, and loads it into a Hadoop ecosystem for analysis with Hive.

## Overview

This project implements an end-to-end data pipeline that:
1. Scrapes posts from popular subreddits (r/MachineLearning, r/AskHistorians, r/philosophy)
2. Processes and cleans the data
3. Loads it into HDFS (Hadoop Distributed File System)
4. Creates and populates a Hive table using an Oozie workflow

## Architecture

```
+-------------+      +------------+      +------------+      +------------+
|   Reddit    | ---> |   Python   | ---> |    HDFS    | ---> |    Hive    |
|    API      |      |  Scrapper  |      |  Storage   |      |   Table    |
+-------------+      +------------+      +------------+      +------------+
                                               ^
                                               |
                                         +------------+
                                         |   Oozie    |
                                         | Workflow   |
                                         +------------+
```

## Technologies Used

- **Python**: Data collection and preprocessing
  - PRAW (Python Reddit API Wrapper)
  - Pandas
- **Hadoop Ecosystem**:
  - HDFS for distributed storage
  - Hive for SQL-like querying
  - Oozie for workflow orchestration

## Project Structure

```
.
├── scrapper.py          # Reddit data collection script
├── oozie/               # Oozie workflow components
│   ├── job.properties   # Configuration parameters
│   ├── workflow.xml     # Workflow definition
│   └── scripts/         # HQL scripts
│       └── create_table.hql  # Hive table creation script
└── README.md            # Project documentation
```

## Setup and Installation

### Prerequisites

- Python 3.6+
- Access to a Hadoop cluster with Hive and Oozie
- PRAW and pandas Python libraries

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/reddit-data-pipeline.git
   cd reddit-data-pipeline
   ```

2. Install the required Python dependencies:
   ```bash
   pip install praw pandas
   ```

## Usage

### 1. Data Collection

Run the scraper to collect Reddit posts:

```bash
python scrapper.py
```

This will create a `posts.csv` file containing data from the specified subreddits.

### 2. Data Loading

Set up your Hadoop environment:

1. Modify the `oozie/job.properties` file with your cluster username and Hive username:
   ```properties
   clusterUsername=your_cluster_username
   hiveUsername=your_hive_username
   ```

2. Upload the Oozie workflow to HDFS:
   ```bash
   hdfs dfs -put -f oozie/ "/user/$USER"
   ```

3. Create the data directory and upload the CSV file:
   ```bash
   hdfs dfs -mkdir -p "/education/ece_2022_fall_bda_1/$USER/reddit_data"
   hdfs dfs -put -f posts.csv "/education/ece_2022_fall_bda_1/$USER/reddit_data/posts.csv"
   ```

4. Run the Oozie workflow:
   ```bash
   oozie job -run -config oozie/job.properties -oozie http://oozie-1.au.adaltas.cloud:11000/oozie
   ```

### 3. Data Query

Query the created Hive table:

```bash
beeline
```

```sql
SELECT * FROM ece_2022_fall_bda_1.[hiveUsername]_reddit_table;
```

## Contributors

- Afonso Maria Rebordão Caiado de Sousa
- Lucas Manchado Marcos
- Patryk Stradomski
- Simona Cardinale

## License

[MIT License](https://opensource.org/licenses/MIT)

## Acknowledgements

- Reddit API for providing access to post data
- Adaltas Cloud for the Hadoop cluster infrastructure
