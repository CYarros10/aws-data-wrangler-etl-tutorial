import awswrangler as wr
import pandas

def lambda_handler(event, context):

    # Iterate thru event object
    for record in event['Records']:

        # get object details
        request_id = record['responseElements']['x-amz-request-id']

        bucket = str(record['s3']['bucket']['name'])
        key = str(record['s3']['object']['key'])
        s3_path = "s3://"+bucket+"/"+key
        print(bucket)
        print(key)

        # delete if exists
        # wr.s3.delete_objects(path="s3://...")

        df = wr.pandas.read_csv(path=s3_path)

        wr.pandas.to_parquet(  # Storing the data and metadata to Data Lake
            dataframe=df,
            database="<insert-glue-database-here>",
            path="s3://"+bucket+"/"+key.replace('.csv','')+"/"
        )
