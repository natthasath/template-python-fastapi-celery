from decouple import config
from celery import Celery
import os
import time

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", f'redis://{config("REDIS_PASS")}@{config("REDIS_HOST")}:{config("REDIS_PORT")}')
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", f'redis://{config("REDIS_PASS")}@{config("REDIS_HOST")}:{config("REDIS_PORT")}')

@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True