from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 12, 16),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
	"catchup": False
}

dag = DAG("cloudmesh_vm_clean", default_args=default_args, schedule_interval=None)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(task_id="aws_clean", bash_command="python /cm/aws_clean.py", dag=dag)
t2 = BashOperator(task_id="azure_clean", bash_command="python /cm/azure_clean.py", dag=dag)

t2.set_upstream(t1)
