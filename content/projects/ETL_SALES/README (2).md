# ETL Package: Data Integration from CSV, Excel, and PostgreSQL to a Single Database

## Overview

This project is an Extract, Transform, Load (ETL) package designed to merge data from various sources, including CSV files, Excel spreadsheets, and a PostgreSQL database, into a single destination database. The ETL process involves cleaning, transforming, and loading data to facilitate efficient analysis and reporting.

## Features

- Extracts data from CSV files, Excel spreadsheets, and a PostgreSQL database.
- Applies customizable transformations to clean and format the data.
- Loads the transformed data into a single destination database.

## Usage
Run the ETL pipeline:
python PIPELINE_EXEC.py

![420171277_408831038167542_8129673976330505678_n](https://github.com/Crocsover/ETL-PIPELINES/assets/139344602/8c0c3cf8-cfa3-4585-99f8-4ae8df45cc9b)


data set from link : [DATA_SOURCE](https://github.com/imjbmkz/JDLS000-Developing-ETL-pipelines-using-SQL-Server-Integration-Services-SSIS/tree/main/data_sources)

I separate csv files into different file sources to demonstrate extracting from different file sources. 

please see below:

<img width="617" alt="raw_sales_excel" src="https://github.com/Crocsover/Data-Engineer/assets/139344602/9de91798-5181-419b-a094-362ad195dd04">

- january to april sales as excel (Sales_January_April_2019)

<img width="613" alt="raw_sales_csv" src="https://github.com/Crocsover/Data-Engineer/assets/139344602/3a4b46d2-7951-4bea-8828-bac0d2a5121c">

- may to august sales as csv(sales_csv folder)
  
<img width="625" alt="raw_sales_database" src="https://github.com/Crocsover/Data-Engineer/assets/139344602/b13800ef-f415-4966-b1be-9da8cb9507e9">

- september to december as database (sales_db)

