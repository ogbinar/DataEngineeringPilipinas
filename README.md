# Welcome to Data Engineering Pilipinas - a PyData group

<p align="center">
<img align="center" width="250" height="250" src="assets/DATA%20ENGINEERING%20-1.png">
</p>

<p align="center">
Data Engineering Pilipinas is a community for data engineers, data analysts, data scientists, developers, AI / ML engineers, and users of closed and open source data tools and methods / techniques in the Philippines. Data Engineering Pilipinas is a PyData group. To know more about the community, <a href="https://youtu.be/XsvrumL0ILc">click here</a> </p>

<p align="center">
This page serves as a repository of notes, thoughts, ideas, plans, dreams, datasets, analyses, and whatever else we think of.
</p>


![Data Engineering Domain](https://media.licdn.com/dms/image/D5612AQG7bJ051eTZQw/article-cover_image-shrink_720_1280/0/1692040311087?e=2147483647&v=beta&t=MIy8h1O6lwGLdLb8tEZKSuanIDRnji5jteLTQwkqCyU)

## Data Engineering
- **Primary Focus**: Data engineering focuses on the practical aspects of data collection, data transformation, and data storage, preparing data for analytical or operational use.
- **Key Responsibilities**: 
  - Building and maintaining data architecture (databases, large-scale processing systems).
  - Developing and managing data pipelines.
  - Ensuring data availability and usability for data scientists and analysts.
- **Skills and Tools**: 
  - Programming languages (Python, Java, Scala).
  - Database languages (SQL).
  - Tools and frameworks (Apache Hadoop, Apache Spark, ETL tools, data warehousing solutions).

## Related Fields

### 1. Data Analysis
- Involves extracting insights from data.
- Tools: Excel, SQL, R, Python, BI tools (like Tableau, Power BI).

### 2. Data Science
- Encompasses data analysis, predictive modeling, and machine learning.
- Tools: Python, R, TensorFlow, machine learning libraries.

### 3. Machine Learning Engineering
- Focuses on building systems that learn from data.
- Tools: Python, machine learning frameworks, cloud computing platforms.

### 4. Business Intelligence (BI)
- Analyzing data to aid business decision-making.
- Tools: SQL, BI platforms (Tableau, Power BI, Looker).

### 5. Database Administration
- Managing and maintaining databases.
- Tools: SQL, database management systems (MySQL, PostgreSQL).

### 6. Big Data
- Handling large and complex data sets.
- Tools: Hadoop, Spark, NoSQL databases.

Each field plays a unique role in the data ecosystem, often collaborating to turn data into actionable insights. As the name suggests, our community focuses on all data career paths with emphasis on data engineering.

### Awesome Data Engineering Repository from the Philippines

### For Beginners
- **Getting Started with Data Engineering**
  - A dedicated section for newcomers with easy-to-understand resources.
  - Links to introductory videos like "Getting Started with Data Engineering."
- **Study Roadmap for Beginners**
  - A clear and structured learning path for newbies.
  - Includes basic courses, tutorials, and foundational knowledge.

*Join our growing community!*

- [Data Engineering Pilipinas | Facebook Group](https://facebook.com/groups/dataengineeringpilipinas/)
- [DEP FB Page](https://www.facebook.com/DataEngineeringPilipinas/)
- [DEP FB Group Chats](https://m.me/cm/AbbnRPVsIMd34APj)
- [Data Engineering Pilipinas | Discord Group ](https://discord.com/invite/buDgydz7J9)
- [Data Engineering Pilipinas | Datacamp Studygroup Discord](https://discord.gg/eKEZuXeyxt)
- [Data Engineering Pilipinas | Meetup ](https://www.meetup.com/data-engineering-pilipinas/)
- [Data Engineering Pilipinas | Youtube ](https://www.youtube.com/@DataEngineeringPilipinas)
- [Data Engineering Pilipinas | LinkedIn Group ](https://www.linkedin.com/company/97217550/)
- [Data Engineering Pilipinas | Reddit ](https://www.reddit.com/r/DataEngineeringPH/)

## Contents

- [Study Roadmap](#study-roadmap)
- [Free Study Resources](#free-resources)
- [Data Storage & Databases](#data-storage--databases)
- [Data Ingestion](#data-ingestion)
- [Data Formats](#data-formats)
- [Stream Procesisng](#stream-processing)
- [Batch Processing](#batch-processing)
- [Workflow Orchestration](#workflow-orchestration)
- [Data Transformation](#data-transformation)
- [Data Governance](#data-governance)
- [Data Platforms](#data-platforms)
- [Community Contents](#community-contents)
- [PH-based Datasets (can be used for projects)](/datasets/PH_data_sources.md)

## Study Roadmap

## Data Engineering - by Sandy
- [DataEngineerRoadmap_Notion](https://shadow-blue-572.notion.site/b880b4ef0b1445aabec127442b97c79f?v=0a45fb3e2b5946d59708797eeea16671) - Data Engineering roadmap with a variety of course options from free to paid. 

## By Nicksy via Data Camp

### Data Engineering
![Data Engineering](assets/DataCamp%20-%20Data%20Engineer%20Track.png)

### Data Analyst
![Data Analyst](assets/DataCamp%20-%20Data%20Analyst%20Associate%20%26%20Professional%20Track.png)

## Best Practices

### Query Optimizations

- [Table Indexes](https://github.com/ogbinar/DataEngineeringPilipinas/tree/main/lessons/table_index)

## Free Resources
- [FREE_RESOURCES.md](resources/FREE_RESOURCES.md) - Compilation of Free Resources that you may find helpful in your journey.
- [Cloud Free Tier](resources/Cloud-Free-Tier-Comparison) - Contains articles comparing the free tier offers of the major cloud providers like AWS, Azure, GCP, Oracle Cloud etc.

## Data Storage & Databases

### Relational Databases

- [PostgreSQL](https://www.postgresql.org) - is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
- [MySQL](https://www.mysql.com) - the most popular Open Source SQL database management system, is developed, distributed, and supported by Oracle Corporation.
- [Amazon Relational Database System (RDS)](https://aws.amazon.com/rds/) is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud. Choose from seven popular engines — Amazon Aurora with MySQL compatibility, Amazon Aurora with PostgreSQL compatibility, MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server

### Columnar Databases
- [Amazon Redshift](https://aws.amazon.com/redshift/?nc=sn&loc=0) - Store, analyze, and process large amounts of data. Cloud Data Warehouse. PostgreSQL backend. MPP Engine and architecture. Available in **Provisioned** or **Serverless**.
- [Google BigQuery](https://cloud.google.com/bigquery?hl=en) - is a serverless and cost-effective enterprise data warehouse that works across clouds and scales with your data.

### Key-value
- [Redis](https://redis.io) - is an open source (BSD licensed), in-memory key-value cache, message broker, and streaming engine.
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) - is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale.

### Object Storage
- [Amazon S3](https://aws.amazon.com/s3/) - is an object storage service offering industry-leading scalability, data availability, security, and performance.
- [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs) - massively scalable and secure object storage for cloud-native workloads, archives, data lakes, high-performance computing, and machine learning.
- [Google Cloud Storage](https://cloud.google.com/storage?hl=en) - is a managed service for storing unstructured data. Store any amount of data and retrieve it as often as you like.

## Data Ingestion
- Apache Kafka - a distributed event streaming platform.
    - [Apache Kafka (open-source)](https://kafka.apache.org/)
    - [Apache Kafka (Confluent)](https://www.confluent.io) - A Fully Managed Service of Apache Kafka that offers support from Kafka Committer-led experts, 99.99% uptime SLA, and etc. Apache Kafka in Confluent is **Cloud-Native**
    - [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/) - is a Fully Managed Kafka Service that operates, maintains, and scales Apache Kafka clusters, provides enterprise-grade security features out of the box, and has built-in AWS integrations that accelerate development of streaming data applications. Apache Kafka in AWS is **Cloud-Hosted**
- [AWS SDK for pandas (AWS Wrangler)](https://github.com/aws/aws-sdk-pandas) - an open source python initiative that extends the power of the pandas library to AWS, connecting DataFrames and AWS data & analytics services. **Open-source**
- [AWS Kinesis](https://aws.amazon.com/kinesis/) - A fully managed, cloud-based service for real-time data processing over large, distributed data streams.
- [Airbyte](https://github.com/airbytehq/airbyte) - A data integration platform for ELT pipelines from APIs, databases & files to databases, warehouses & lakes.
    - [Open-source](https://airbyte.com/solutions/airbyte-open-source)
    - [Airbyte Cloud](https://airbyte.com/solutions/airbyte-cloud)
- [Pentaho Data Integration (Kettle)](https://www.hitachivantara.com/en-us/products/pentaho-platform/data-integration-analytics.html) - consists of a core data integration (ETL) engine, and GUI applications that allow the user to define data integration jobs and transformations.
    - [Community Edition](https://www.hitachivantara.com/en-us/products/pentaho-platform/data-integration-analytics/pentaho-community-edition.html)

## Data Formats

- [Apache Arvo](https://avro.apache.org) - is the leading serialization format for record data, and first choice for streaming data pipelines.
- [Apache Parquet](https://parquet.apache.org) - is an open source, column-oriented data file format designed for efficient data storage and retrieval.
- [Apache ORC](https://orc.apache.org) - the smallest, fastest columnar storage for Hadoop workloads.

## Data Storage Framework

- [Delta Lake](https://delta.io) - is an open-source storage framework that enables building a Lakehouse architecture with compute engines including Spark, PrestoDB, Flink, Trino, and Hive and APIs for Scala, Java, Rust, Ruby, and Python. Led by [Databricks](https://www.databricks.com).
- [Apache Iceberg](https://iceberg.apache.org) - is an open table format for huge analytic datasets. Iceberg adds tables to compute engines including Spark, Trino, PrestoDB, Flink, Hive and Impala using a high-performance table format that works just like a SQL table. Developed by [Netflix](https://github.com/Netflix/iceberg#status)
- [Apache Hudi](https://hudi.apache.org) - (pronounced Hoodie), stands for `Hadoop Upserts Deletes and Incrementals`. Hudi manages the storage of large analytical datasets on DFS (Cloud stores, HDFS or any Hadoop FileSystem compatible storage). Developed by [Uber](https://www.uber.com/en-TW/blog/hoodie/).

## Batch Processing

### Frameworks and Libraries

- [Apache Spark](https://spark.apache.org) - is a multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters.
    - [PySpark](https://spark.apache.org/docs/latest/api/python/index.html)
    - [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html)
    - [Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html) - Allows pandas function on top of Spark
    - [Spark SQL](https://spark.apache.org/docs/latest/api/sql/index.html) - List of SQL Functions
    - [SparkR](https://spark.apache.org/docs/latest/sparkr.html)
    - [Java](https://spark.apache.org/docs/latest/api/java/index.html)
- [Polars (Python)](https://www.pola.rs) - is a lightning fast DataFrame library/in-memory query engine.
- [Dask (Python)](https://docs.dask.org/en/stable/) - is a flexible library for parallel computing in Python.

### SQL

- [Presto](http://prestodb.io) - is a distributed SQL query engine for big data that allows you to run SQL queries against various data sources.
- [Apache Hive](https://hive.apache.org) - is built on top of Apache Hadoop. A distributed, fault-tolerant data warehouse system that enables analytics at a massive scale and facilitates reading, writing, and managing petabytes of data residing in distributed storage using SQL.
- [Apache Drill](https://drill.apache.org)- is an Apache open-source SQL query engine for Big Data exploration.
- [Trino](https://trino.io) - is a distributed SQL query engine designed to query large data sets distributed over one or more heterogeneous data sources.

### Managed Services (Cloud)

- [AWS Elastic MapReduce (EMR)](https://aws.amazon.com/emr/) - is the industry-leading cloud big data solution for petabyte-scale data processing, interactive analytics, and machine learning using open-source frameworks such as Apache Spark, Apache Hive, and Presto.
- [AWS Glue](https://aws.amazon.com/glue/) - is a serverless data integration service that makes it easier to discover, prepare, and combine data for analytics, machine learning (ML), and application development.

## Stream Processing

- [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) - an extension of core Spark API for processing of live data streams. **Deprecated** as of Spark 2.0.
    - [Spark Structured Streaming (DataFrames)](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) - is a stream processing engine built on the Spark SQL engine.
- [Apache Flink](https://flink.apache.org) - is a framework and distributed processing engine for stateful computations over Data Streams
- [Apache Storm](https://storm.apache.org/about/integrates.html) - is a free and open source distributed realtime computation system. Doing for realtime processing what Hadoop did for batch processing.

### Data Stores
- [Apache Druid](https://druid.apache.org) - is a high performance, real-time analytics database that delivers sub-second queries on streaming and batch data at scale and under load.
- [Apache Pinot](https://pinot.apache.org) - realtime distributed OLAP datastore, designed to answer OLAP queries with low latency

## Workflow Orchestration

- [Apache Airflow](https://airflow.apache.org) - is an open-source workflow management platform for data engineering pipelines. Built by [Airbnb](https://airbnb.io/projects/airflow/).
    - [Astronomer](https://www.astronomer.io)
    - [Amazon Managed Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/managed-workflows-for-apache-airflow/)
- [Mage](https://www.mage.ai) - Open-source data pipeline tool for transforming and integrating data. The modern replacement for Airflow.
- [Dagster](https://dagster.io) - An orchestration platform for the development, production, and observation of data assets.
    - [Open-source](https://docs.dagster.io/getting-started)
    - [Dagster Cloud](https://dagster.io/cloud)
- [Prefect](https://www.prefect.io) - is a workflow orchestration tool empowering developers to build, observe, and react to data pipelines.
    - [Open-source](https://docs.prefect.io/2.13.8/getting-started/quickstart/#__tabbed_1_2)
    - [Prefect Cloud](https://www.prefect.io/cloud)
- [Kestra](https://kestra.io) - is a universal open-source orchestrator that makes both scheduled and event-driven workflows easy
    - [Open-source](https://kestra.io/docs)
    - [Kestra Cloud](https://kestra.io/enterprise)
- [AWS Step Functions](https://aws.amazon.com/step-functions/) - is a fully managed service that makes it easier to coordinate the components of distributed applications and microservices using visual workflows.

## Data Transformation

### Frameworks

- [Data Build Tool (dbt)](https://www.getdbt.com) - is a SQL-first transformation workflow that lets teams quickly and collaboratively deploy analytics code following software engineering best practices like modularity, portability, CI/CD, and documentation.
    - [dbt-core (open-source)](https://docs.getdbt.com/docs/core/installation)
    - [dbt Cloud](https://www.getdbt.com/product/dbt-cloud)
- [SQLMesh](https://sqlmesh.readthedocs.io/en/stable/) - is an open source data transformation framework that brings the best practices of DevOps to data teams. It enables data scientists, analysts, and engineers to efficiently run and deploy data transformations written in SQL or Python.

## Data Governance

### Enterprise Data Catalog

- [DataHub Project](https://datahubproject.io) - is an extensible metadata platform that enables data discovery, data observability and federated governance to help tame the complexity of your data ecosystem. Has **open-source** and **Managed**. Built by [LinkedIn](https://engineering.linkedin.com/blog/2019/data-hub). 
- [OpenMetadata](https://open-metadata.org) - A Single Place to Discover, Collaborate and get your Data Right. **Open-source.** Inspired by Uber's metadata platform.
- [Apache Atlas](https://atlas.apache.org/#/) - is an open-source metadata and big data governance framework which helps data users collaborate on their data assets. **Open-source.** Incubated by [Hortonworks](https://www.prnewswire.com/news-releases/hortonworks-establishes-data-governance-initiative-300026958.html).
- [Amundsen](https://www.amundsen.io) - Open source data discovery and metadata engine. Created by Lyft. 

### Data Quality/Observability
- [Great Expectations](https://greatexpectations.io) - a platform for Data Quality.
    - [Open-source](https://docs.greatexpectations.io/docs/tutorials/quickstart/) - is a Python library that provides a framework for describing the acceptable state of data and then validating that the data meets those criteria.
    - [Cloud (SaaS)](https://greatexpectations.io/gx-cloud) - 

## Data Platforms

- [Databricks](https://www.databricks.com) - Founders of Apache Spark. Combines Data Warehouse and Data Lake (Data Lake House) into a platform. Unified. Open. Scalable. Try it [free](https://www.databricks.com/try-databricks#account) for 14 days. Suggest that you use AWS as the choice of platform.
- [Snowflake](https://www.snowflake.com/en/) - The Data Cloud. Cloud-native Data Warehouse Platform. Consists of Cloud Services Layer, Compute Layer, and Data Storage Layer. Try it [free](https://signup.snowflake.com) for 30 days.  

## Data dumps

*Work in progress*

## Community Contents


#### What is Data Engineering Pilipinas?

**Description:**

A 5 minute presentation on why you should join Data Engineering Pilipinas.

**Link:** [https://youtu.be/XsvrumL0ILc](https://youtu.be/XsvrumL0ILc0)

---


#### Getting Started with Data Engineering

**Description:**

This video provides an introduction to Data Engineering. In partnership with StudevPH with guest speaker, Josh Dev

**Link:** [https://www.facebook.com/studevph/videos/165090273259790](https://www.facebook.com/studevph/videos/165090273259790)

---

#### EP1 - Unlocking Your Future: Building a Career in PH Tech Startups

**Description:**

This video discusses building a career in PH Tech Startups.
* In Partnership with Filipino Web Development Peers, Hosted by FWDP Founder, David Genesis Pedeglorio
* Guest Speaker: Andoy Montiel, Chief Data Officer of Packworks

**Link:** [https://youtu.be/pzxFTFB8f6s](https://youtu.be/pzxFTFB8f6s)

---

#### Unlocking Career Opportunities: Philippine Skills Framework for AI and Analytics

**Description:**

This video discusses careers in Analytics in the Philippines.
* Guest Sherwin Pelayo, and hosted by Doc Ligot
 
**Link:** [https://www.youtube.com/watch?v=_CjsYi9ivlc](https://www.youtube.com/watch?v=_CjsYi9ivlc)

---

### TechSync 2023: Synchronizing Filipino Tech Communities

**Description:**

A FREE online event featuring content creators and thought leaders in the tech field:

* JP "Sir JP" Lazro & Rhea Alum, StudevPH
* Seiji Villafranca, Angular PH
* David Genesis Pedeglorio & Renzo Marl Peralta, Filipino Web Development Peers
* Josh "Josh Dev" Valdeleon, Data Engineering Pilipinas
* Hosted by Kuya Dev and Doc Ligot

**Link:** [https://www.facebook.com/watch/live/?ref=watch_permalink&v=1043806640102969](https://www.facebook.com/watch/live/?ref=watch_permalink&v=1043806640102969)

#### filWebDev Talks Ep. 10 ft. Myk Ogbinar of AI Network PH

**Description:**

This video provides an introduction a career in Data. In partnership with Filipino Web Development Peers and AI Network PH with guest speaker, Myk Ogbinar

**Link:** [https://www.facebook.com/fwdpeers/videos/220432324246191](https://www.facebook.com/fwdpeers/videos/220432324246191)

#### Kamustahan: A Panel Discussion on Building a Career in Tech

**Description:**

A podcast style session with Myk, Allan Aquino, JP Acuna, JP Lazaro, & Rod Basa, (and a special post from sir Nino from Learn with Jon), about navigating a tech career.

**Link:** [https://www.youtube.com/watch?v=jcFALIHBSuQ](https://www.youtube.com/watch?v=jcFALIHBSuQ)

#### Exclusive Interview: Sandy Lauguico's Data Engineering Transition

**Description:**

In this exclusive interview, join me (Doc Ligot) as we explore the inspiring journey of Sandy Lauguico, who made a remarkable shift into the world of Data Engineering. Gain valuable insights, tips, and first-hand experiences as Sandy shares her transformation story. Discover the exciting world of data and engineering with us!

**Link:** [https://www.youtube.com/watch?v=8pJMFi3kIfQ](https://www.youtube.com/watch?v=8pJMFi3kIfQ)

#### From Dropout to Tech Star: Aemy Obinguar's Inspirational Tale

**Description:**

In this exclusive interview, join me(Doc Ligot) as I delve into the remarkable journey of Aemy Obinguar, who defied the odds by dropping out of school and ultimately rising to the position of Chief Technology Officer (CTO). Discover her insights, challenges, and successes in the tech world. Don't miss this inspiring story of determination and achievement. 

**Link:** [https://www.youtube.com/watch?v=GZcYyILg3kc](https://www.youtube.com/watch?v=GZcYyILg3kc)

#### A Panel Discussion on Shifting to a Career in Data | RUG-PH 120

**Description:**

A panel answers questions on how to shift to a career in data from practicing another profession. They discuss skills and competencies required in data-related roles, including those that were gained in the practice of other professions but are also valued by data teams. Hosted by R User's group Philippines!

**Link:** [https://youtu.be/ivzmUPRqxQ8?si=c_OdyC4FvqOJv6Bq](https://youtu.be/ivzmUPRqxQ8?si=c_OdyC4FvqOJv6Bq)

### Posts from the community

- [Kyle Escosia](https://linktr.ee/klescosia) - A Data Engineer who is passionately curious in anything about data.
    - Featured Contents
        - [Introduction to Big Data and Analytics (Webinar)](https://www.facebook.com/watch/live/?ref=search&v=2388014311349277)        
        - [Building a Serverless Data Lake in AWS (Webinar)](https://www.facebook.com/watch/live/?ref=watch_permalink&v=684903669389073)
        - [Snowflake in the Philippines](https://medium.com/@kyle.escosia/the-rise-of-snowflake-in-the-philippines-why-its-the-hottest-thing-in-big-data-right-now-9b9d09c11e89)
        - [UPSERTS and DELETS using AWS Glue and Delta Lake](https://dev.to/awscommunity-asean/sql-based-inserts-deletes-and-upserts-in-s3-using-aws-glue-3-0-and-delta-lake-42f0)
