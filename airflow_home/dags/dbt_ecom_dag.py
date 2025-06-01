from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'you',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='dbt_ecom_pipeline',
    default_args=default_args,
    start_date=datetime(2025, 6, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    run_dbt = BashOperator(
        task_id='run_dbt_models',
        bash_command=(
            "/Users/sean/projects/my_ecom_ae_demo/.venv/bin/dbt "
            "run --profiles-dir /Users/sean/.dbt "
            "--project-dir /Users/sean/projects/my_ecom_ae_demo"
        )
    )

    test_dbt = BashOperator(
        task_id='test_dbt_models',
        bash_command=(
            "/Users/sean/projects/my_ecom_ae_demo/.venv/bin/dbt "
            "test --profiles-dir /Users/sean/.dbt "
            "--project-dir /Users/sean/projects/my_ecom_ae_demo"
        )
    )

    run_dbt >> test_dbt
