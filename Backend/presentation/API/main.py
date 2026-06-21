from fastapi import FastAPI, Depends
from Shared.database import get_session
from typing import Annotated
from Infrastructure.DB.repo_implement.task_repo_impl import task_repo_impl
from .pydantic_models.task_pydanic import task_pydantic
app = FastAPI()

taskRepoImpl = task_repo_impl(get_session())


@app.get("/")
async def root():
    return("HEllo welcome !!")

@app.get("/task")
async def get_tasks():
    return taskRepoImpl.list_by_status()

@app.post("/task")
async def add_task(data: Annotated[task_pydantic, Depends(task_pydantic)]):
    return taskRepoImpl.add_task(data)

@app.put("/task")
async def update_task(data: Annotated[id: int,task_pydantic, Depends(id, task_pydantic)]):
    return taskRepoImpl.update_task(id, data)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)