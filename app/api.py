from fastapi import FastAPI, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from worker import create_task
from app.routers import template, tasks
from app.tag import SubTags, Tags

templates = Jinja2Templates(directory="./app/template")

app = FastAPI(
    title="FastAPI",
    description="Web API helps you do awesome stuff. 🚀",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Information and Digital Technology Center (IDT)",
        "url": "https://codeinsane.wordpress.com/",
        "email": "natthasath.sak@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    openapi_tags=Tags(),
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

app.mount("/static", StaticFiles(directory="./app/public"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})

@app.post("/", status_code=201)
def run_task(payload = Body(...)):
    task_type = payload["type"]
    task = create_task.delay(int(task_type))
    return JSONResponse({"task_id": task.id})

@app.get("/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(tasks.router)
#
#
#

subapi = FastAPI(openapi_tags=SubTags(), swagger_ui_parameters={"defaultModelsExpandDepth": -1})

subapi.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

subapi.include_router(template.router)
#
#
#

app.mount("/subapi", subapi)