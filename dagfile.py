from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 29, 10, 0), # start at 10:00 am
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_python_script_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

run_script = BashOperator(
    task_id='run_python_script',
    bash_command='python3 intracheck.py',
    dag=dag,
)

run_script
