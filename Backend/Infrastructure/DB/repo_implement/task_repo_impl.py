from Domain.repository.task_repository import task_repository
from sqlalchemy import select
from ..ORM.task_ORM import task_ORM

class task_repo_impl(task_repository):
    def __init__(self, session):
        self.session = session

    def add_task(self, task_data):
        try:
            task = task_ORM(**task_data)
            self.session.add(task)
            res = self.session.commit()
            return res
        except:
            return "Error while adding task !!!"
        
    def update_task(self, task_data):
        return super().update_task(task_data)
    
    def delete_task(self, task_data):
        return super().delete_task(task_data)
    
    def list_by_status(self):
        statement = select(task_ORM)
        return self.session.execute(statement).all()
        
