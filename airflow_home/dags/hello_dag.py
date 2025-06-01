from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def say_hello():
    print("hello from Airflow")

default_args = {
    'owner': 'airflow',
    'retries': 0,
}

with DAG(
    dag_id='hello_dag',
    default_args=default_args,
    start_date=datetime(2025, 6, 1),
    schedule_interval=None,
    catchup=False
) as dag:
    hello_task = PythonOperator(
        task_id='say_hello',
        python_callable=say_hello
    )

