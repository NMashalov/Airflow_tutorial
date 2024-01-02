# Airflow tutorial

Work with airflow can be challenging. This tutorial will guide you through everyday routine of Airflow engineer through task of OCR recognition of book.

## Intro
Airflow is orchestration tool. It means it capable of: 
- connecting all odd task together 
- advising a way for transferring data between tasks
- scheduling execution on timetable
- providing best effort to fix errors

## Technical prerequisits. 
Unfortunately, you'll need at least **4GB of RAM** on your desktop for running Airflow. I hope you'll find a way to cope with it.

## Plan


![Pipeline](assets/graphs/pipeline.excalidraw.png)

###

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
                You can modify RAM for wsl with <a href="https://learn.microsoft.com/en-us/answers/questions/1296124/how-to-increase-memory-and-cpu-limits-for-wsl2-win">question</a> from official Microsoft forum.
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

## Installing Airflow from Docker 

We will work with Docker version of Airflow as it's allows to make reproducible environment. I'll follow [official Airflow instruction]( https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) for running in Docker.

Here's step by step instruction of running airflow
- Create folders for 
    ```bash
    mkdir -p ./dags ./logs ./plugins ./config
    ```
    Here's concrete:
    

    <details>
    <summary>In case you want to delete them use</summary>
    sudo rm -r  ./dags ./logs ./plugins ./config
    </details>
- Set unique id of airflow process
    ```bash
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```
- Initialize Airflow
    ```bash
    docker compose up airflow-init
    ```
- Finally you can enjoy airflow
    ```bash
    docker compose up
    ```
    If everything gone well, you can visit Airflow website on address http://localhost:8080/home. Password will be 
    ![](assets/airflow_ui.png)
    
Furhter work 
Informal description of fode
- `dags/` - folder where you'll store your  
- `logs/` - holds journal of changes and executions of your scripts
- `plugins/` - allow to modify airflow. More info [here](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/plugins.html)
- 

Hopefully we will be interested only in `dags` folder in this tutorial.

## Dag development

Dags can be updated in runtime of airflow. It means that after small time around 15 seconds your brand new dag will be scanned by airflow and added to ui.

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