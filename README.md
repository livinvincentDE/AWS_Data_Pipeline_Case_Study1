# 🚀 Data Engineering in AWS

## 📌 Overview

This project demonstrates an end-to-end data engineering pipeline using AWS services.

## 🧱 Architecture

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


## ⚙️ Tech Stack

* AWS S3
* AWS Glue
* PySpark
* Athena

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

Analyze sales data by country and date.

## 👨‍💻 Author

Livin Vincent
