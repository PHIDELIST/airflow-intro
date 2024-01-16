from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator
default_args={
    'owner':'coder2j',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}
with DAG (
    dag_id='my_first_dag_v3',
    default_args=default_args,
    description='this is my forst dag to write',
    start_date=datetime(2024,1,29,2),
    schedule='@daily'
)as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task!'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hello world, this is the second task!'
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hello world, this is the task three and it will be runned after task 1 at same time as task two!'
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)