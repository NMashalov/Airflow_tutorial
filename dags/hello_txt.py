import textwrap
from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
with DAG(
    "my_bash_echo_tutorial",
    default_args={
        "retries":21,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    t1 = BashOperator(
        task_id="create_hello.txt",
        bash_command="touch hello.txt",
    )

    t2 = BashOperator(
        task_id="fill_hello.txt",
        bash_command="echo 'hello Airflow' << hello.txt",
    )

    t1 >> t2