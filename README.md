# 🚀 Data Engineering in AWS

## ⚙️ Tech Stack

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)
![Amazon S3](https://img.shields.io/badge/Amazon%20S3-Storage-blue?logo=amazon-s3)
![AWS Glue](https://img.shields.io/badge/AWS%20Glue-ETL-orange?logo=amazonaws)
![PySpark](https://img.shields.io/badge/PySpark-Big%20Data-yellow?logo=apache-spark)
![Athena](https://img.shields.io/badge/Amazon%20Athena-Query-blue?logo=amazonaws)

## 📌 Overview

This project demonstrates an end-to-end data engineering pipeline using AWS services.

## 🧱 Architecture

```
          ┌──────────────┐
          │   S3 (Raw)   │
          │  JSON Data   │
          └──────┬───────┘
                 ↓
        ┌──────────────────┐
        │ Glue Crawler     │
        │ Schema Inference │
        └──────┬───────────┘
               ↓
     ┌──────────────────────┐
     │ Glue Data Catalog    │
     │ Table: raw           │
     └──────┬───────────────┘
            ↓
     ┌──────────────────────┐
     │ Glue ETL Job         │
     │ PySpark Transform    │
     └──────┬───────────────┘
            ↓
     ┌──────────────────────┐
     │ S3 (Processed)       │
     │ Parquet (Partitioned)│
     └──────┬───────────────┘
            ↓
     ┌──────────────────────┐
     │ Amazon Athena        │
     │ SQL Analytics        │
     └──────────────────────┘
```

## 🔄 Features

* Incremental loading
* CDC
* Data quality checks
* Bronze/Silver/Gold layers

## 📂 Structure

* data/
* scripts/
* output/

## 📊 Use Case

Ingestion → Transformation → Analytics
Analyze sales data by country and date.

## 👨‍💻 Author

Livin Vincent
