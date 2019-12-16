from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 12, 15),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
	"catchup": False
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("cloudmesh_move", default_args=default_args, schedule_interval=timedelta(1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t0 = BashOperator(task_id="print_date", bash_command="date", dag=dag)
t1 = BashOperator(task_id="print_help", bash_command="cms help", dag=dag)
t2 = BashOperator(task_id="list_flavors", bash_command="cms flavor list --refresh", retries=3, dag=dag)
t3 = BashOperator(task_id="init", bash_command="cms init", retries=3, dag=dag)
t4 = BashOperator(task_id="set_cloud", bash_command="cms set cloud=chameleon", retries=3, dag=dag)
t5 = BashOperator(task_id="add_key", bash_command="cms key add austin --source=ssh", retries=3, dag=dag)
t6 = BashOperator(task_id="upload_key", bash_command="cms key upload austin --cloud=chameleon", retries=3, dag=dag)
t7 = BashOperator(task_id="boot_chameleon_vm", bash_command="cms vm boot", retries=3, dag=dag)

t1.set_upstream(t0)
t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t3)
t5.set_upstream(t4)
t6.set_upstream(t5)
t7.set_upstream(t6)
