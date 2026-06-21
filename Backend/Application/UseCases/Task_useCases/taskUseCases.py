from Infrastructure.DB.repo_implement.task_repo_impl import task_repo_impl
from Shared.database import get_session
session = get_session()
Implement = task_repo_impl(session)

def createTaskUseCase(data):
    task = Implement.build_task(data)
    return Implement.add_task(task)


def updateTask(data):
    task = Implement.build_task(data)
    return Implement.update_task(task)


def deleteTask(id: int):
    return Implement.delete_task(id)


def markTaskCompleteUseCase(id: int):
    return Implement.build_task(Implement.get_task(id))

def listTasksUseCase(): #we can get how to list: By status By date By priority
    return Implement.list_by_status()