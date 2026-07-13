from fastapi.routing import APIRouter
from fastapi import Depends
from typing import Annotated

from Application.UseCases.taskUseCases import taskUseCases
from ...pydantic_models.task_pydanic import task_pydantic, task_pydantic_input
from Shared.database import get_session

session = get_session()

TUC = taskUseCases(session)

router = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)

@router.get("")
async def get_tasks():
    return TUC.listTasksUseCase()

@router.post("/add")
async def get_tasks(data: Annotated[task_pydantic_input, Depends(task_pydantic_input)]):
    return TUC.createTaskUseCase(data)

@router.put("/update")
async def update_task(data: Annotated[task_pydantic, Depends(task_pydantic)]):
    return TUC.updateTaskUseCase(data)

@router.delete("/delete/{id}")
async def delete_task(id: int):
    return TUC.deleteTaskUseCase(id)

@router.put("/complete/{id}")
async def mark_complete(id: int):
    return TUC.markTaskCompleteUseCase(id)