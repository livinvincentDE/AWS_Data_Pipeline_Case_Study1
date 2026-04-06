# 🚀ETL & Data Engineering in AWS

## ⚙️ Tech Stack

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)
![AWS Glue](https://img.shields.io/badge/AWS%20Glue-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)
![Amazon Athena](https://img.shields.io/badge/Amazon%20Athena-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)

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
