from fastapi import APIRouter, Depends, Form, Body
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from app.worker import create_task

router = APIRouter(
    prefix="/tasks",
    tags=["TASKS"],
    responses={404: {"message": "Not found"}}
)

@router.post("/", status_code=201)
def run_task(payload = Body(...)):
    task_type = payload["type"]
    task = create_task.delay(int(task_type))
    return JSONResponse({"task_id": task.id})

@router.get("/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)