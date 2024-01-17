from datetime import datetime,timedelta
from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args={
    'owner':'phidelist',
    'retries':0,
    'retry_delay':timedelta(minutes=2)
}

with DAG (
    dag_id='dag_with_s3_v01',
    default_args=default_args,
    description='dag with s3 sensor',
    start_date=datetime(2023,1,29,2),
    schedule='@daily'
)as dag:
    task1 = S3KeySensor(
        task_id='sensor_s3',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id='s3_conn'
    )