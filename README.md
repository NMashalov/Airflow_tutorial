# Airflow tutorial

Work with airflow can be challenging. This tutorial will guide you through basic task of OCR.

## Description

In this tutorial you'll learn to manage pipeline

## Technical prerequisits. 
Unfortunatelly, you'll need at least **4GB of RAM** on your desktop for running Airflow. I hope you'll find a way to cope with it.

![Pipeline]()


## Plan

You'll need to install Docker on your work machine. I'll provide you a small guide on steps for installation for your os.


<details>
<summary>Guide</summary>
<div><ul>
    <li> Linux
        <div>       
        Follow steps of <a href="https://docs.docker.com/engine/install/ubuntu/">official Docker Guide</a>. It's free :)
        </div>
    </li>
    <li> Windows
        <ul> 
            <li> If you already have WSL2
                <div> 
                Then you can proceed with similar steps for Linux.
                </div>
            </li>    
            <li> If you don't have WSL2
                <div>
                Install WSL2. Follow <a href="https://learn.microsoft.com/en-us/windows/wsl/install">official Microsoft guide</a>. I recommend use to choose Ubuntu 20.04 as your unix system. 
                </div>
            </li>
        </ul>
    </li>
</ul></div>
</details>

1. Installing airflow from Docker 

We will work with Docker version of Airflow as it's allows to make reproducible environment. I'll follow [official Airflow instruction]( https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) for running in Docker.


Following directories will be :
- `dags/` - folder where you'll store your  
- `logs/` - holds journal of changes and executions 
- `plugins/` - allow to modify airflow. More info [here](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/plugins.html)

Hopefully we will be interested only in `dags` folder in this tutorial.

2. Dag development

After successful installation we can start writing our pipelines. We'll add them in directory dags


Actually it can be hard task for first try.

I'll provide you with some working code for your trial

```python

import textwrap
from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
with DAG(
    "tutorial",
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

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )


    t3 = BashOperator(
        task_id="templated",
        depends_on_past=False,
        bash_command=templated_command,
    )

    t1 >> [t2, t3]
```

Run in directory with `docker-compose.yml`
``` bash
docker compose up
```

You can gracefully stop simply by 

This can take time.

3. Actual task



```
!wget https://mathus.ru/math/geometric-progression.pdf
```