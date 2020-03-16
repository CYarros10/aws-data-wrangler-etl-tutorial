# aws-data-wrangler-etl-tutorial

## Using AWS Data Wrangler for simple ETL

Drop CSV files into S3 and automatically convert to snappy-compressed Parquet using AWS Data Wrangler library.

### About

AWS Data Wrangler is basically Pandas on AWS. Makes reading, writing, and transforming data in S3 extremely simple. Integrates with AWS Glue, Athena, and other AWS services.


GitHub: https://github.com/awslabs/aws-data-wrangler

Documentation: https://aws-data-wrangler.readthedocs.io/en/latest/

Install Tutorial for Lambda: https://aws-data-wrangler.readthedocs.io/en/latest/install.html

Releases with Glue Egg/Wheel: https://github.com/awslabs/aws-data-wrangler/releases

----

## Create the Lambda Layer

1. Go to [Lambda Layers Console](https://console.aws.amazon.com/lambda/home?region=us-east-1#/layers).

2. Add the Lambda Layer specified in the aws-data-wrangler repository

    - https://github.com/awslabs/aws-data-wrangler/releases

    - awswrangler-layer-0.3.2-py3.8.zip

## Create the Lambda

3. Go to [Lambda Function Console](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions). Create new Lambda function. Copy code from scripts/lambda-transform.py into your Lambda Function. Update code with correct glue database: **insert-glue-database-here**

4. Create a new Lambda role with S3, Glue, and CloudWatch permissions

5. Add S3 trigger to for the bucket that you will place a CSV into.

6. Add Lambda Layer for awswrangler to function.

7. Depending on data size, modify timeout and memory.  For this example, set timeout to **30 seconds** and memory to **1024 MB**.

## Initiate Lambda ETL

8. Place samples/un-general-debates.csv (93.3 MB) into S3 Bucket containing S3 Trigger

## Viewing Results

7. Go to [Glue Data Catalog Console](https://console.aws.amazon.com/glue/home?region=us-east-1#), wait for Glue Data Catalog to update with new table. (un-general-debates)

8. Go to Athena Console and query the table.

        select * from un_general_debates limit 10;

