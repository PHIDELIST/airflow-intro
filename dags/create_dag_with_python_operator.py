from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
#XComs (short for “cross-communications”) are a mechanism that let Tasks talk to each other, as by default Tasks are entirely isolated and may be running on entirely different machines.
#An XCom is identified by a key (essentially its name), as well as the task_id and dag_id it came from. They can have any (serializable) value, but they are only designed for small amounts of data; do not use them to pass around large values, like dataframes.
#XComs are explicitly “pushed” and “pulled” to/from their storage using the xcom_push and xcom_pull methods on Task Instances.
default_args = {
    'owner':'phidelist',
    'retries':0,
    'retry_delay':timedelta(minutes=2)
}

def greet(age,ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    print(f"Hello World! my name is {first_name} {last_name}"
          f" and am {age} years old")
    
def get_name(ti):
     ti.xcom_push(key='first_name', value='phidel')
     ti.xcom_push(key='last_name', value='Freeman')

with DAG(
    default_args=default_args,
    dag_id='v5_python_operator',
    description='dag using python operator',
    start_date=datetime(2023,10,16),
    schedule_interval='@daily'
) as dag:
      
      task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'age':23}
    )
      task2 = PythonOperator(
           task_id='get_name',
           python_callable=get_name
      )

      task2 >> task1