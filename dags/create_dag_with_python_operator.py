from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'phidelist',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

def greet():
    print("Hello World!")


with DAG(
    default_args=default_args,
    dag_id='v1_python_operator',
    description='dag using python operator',
    start_date=datetime(2024,10,6),
    schedule_interval='@daily'
) as dag:
      task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )