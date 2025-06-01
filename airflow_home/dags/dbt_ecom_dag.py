from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'you',
    'retries': 1,
    'retry_delay': timedelta(seconds=15),
}

with DAG(
    dag_id='dbt_ecom_pipeline',
    default_args=default_args,
    start_date=datetime(2025, 6, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    run_dbt_models = BashOperator(
        task_id='run_dbt_models',
        bash_command=(
            "source ~/projects/my_ecom_ae_demo/.venv/bin/activate && "
            "cd ~/projects/my_ecom_ae_demo && "
            "dbt run --profiles-dir ~/.dbt"
        )
    )

    test_dbt_models = BashOperator(
        task_id='test_dbt_models',
        bash_command=(
            "source ~/projects/my_ecom_ae_demo/.venv/bin/activate && "
            "cd ~/projects/my_ecom_ae_demo && "
            "dbt test --profiles-dir ~/.dbt"
        )
    )

    run_dbt_models >> test_dbt_models
