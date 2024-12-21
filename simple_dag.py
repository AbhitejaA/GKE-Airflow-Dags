from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

dag = DAG(
    'simple_dag',
    default_args=default_args,
    schedule_interval='@daily',
)

task = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)