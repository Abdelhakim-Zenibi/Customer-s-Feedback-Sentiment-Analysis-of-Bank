from sqlalchemy import create_engine

def load(**kwargs):
    # Retrieve the transformed data from the previous task
    transformed_data = kwargs['ti'].xcom_pull(task_ids='transform_task')
    
    # Connect to the PostgreSQL database
    engine = create_engine('postgresql://airflow_user:airflow_pass@localhost:5432/airflow_db')
    
    # Load the DataFrame into the database
    transformed_data.to_sql('banks', engine, if_exists='replace', index=False)
