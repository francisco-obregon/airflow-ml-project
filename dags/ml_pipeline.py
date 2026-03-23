from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

BASE_PATH = "{{ var.value.BASE_PATH }}"

with DAG(
    dag_id="ml_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["ml", "portfolio"]
) as dag:

    train_model = BashOperator(
        task_id="train_model",
        bash_command=f"""
        export BASE_PATH={BASE_PATH} &&
        python $BASE_PATH/ml/train_model.py
        """
    )

    predict_model = BashOperator(
        task_id="predict_model",
        bash_command=f"""
        export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES &&
        export BASE_PATH={BASE_PATH} &&
        python $BASE_PATH/ml/predict.py
        """
    )

    train_model >> predict_model