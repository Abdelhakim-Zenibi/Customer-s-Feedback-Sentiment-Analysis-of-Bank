import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from extract import extract
from transform import transform
from load import load

etl_dag = DAG(
    dag_id="ETL_DAG",
    start_date=datetime.datetime(2023, 6, 3),
    schedule="0 0 1 * *",
)

# Define the tasks
extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract,
    dag=etl_dag
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform,
    provide_context=True,
    dag=etl_dag,
)

load_task = PythonOperator(
    task_id='load_task', 
    python_callable=load,
    provide_context=True, 
    dag=etl_dag
)


# Set up task dependencies
extract_task >> transform_task >> load_task

