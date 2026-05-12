from fastapi import FastAPI
from pydantic import BaseModel

from app.workflows.dev_workflow import run_dev_workflow

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

@app.post("/run")
def run_agent(req: TaskRequest):
    result = run_dev_workflow(req.task)
    return result