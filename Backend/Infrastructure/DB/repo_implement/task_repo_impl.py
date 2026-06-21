from Domain.repository.task_repository import task_repository
from ..ORM.task_ORM import task_ORM

class task_repo_impl(task_repository):
    def __init__(self, session):
        self.session = session

    def add_task(self, task_data):
        try:
            task = task_ORM(**task_data.__dict__)
            self.session.add(task)
            res = self.session.commit()
            return res
        except Exception as e:
            return {"status": "failure", "message": str(e)}
        
    def update_task(self,task_data):
        try:
            res = self.session.query(task_ORM).filter(task_ORM.id == task_data.id).update(task_ORM(**task_data.__dict__))
            return {"status": "success", "message": str(res)}
        except Exception as e:
            return {"status": "failure", "message": str(e)}
    
    def delete_task(self, id):
        try:
            res = self.session.query(task_ORM).filter(task_ORM.id == id).delete()
            return {"status": "success", "message": "task deleted : "+str(res)}
        except Exception as e:
            return {"status": "failure", "message": str(e)}   
         

    def get_task(self, id):
        try:
            task = self.session.query(task_ORM).filter(task_ORM.id == id).first()
            return task
        except Exception as e:
            return {"status": "failure", "message": str(e)}   
    

    def list_by_status(self):
        try:
            allTask: dict = self.session.query(task_ORM).fillter(not task_ORM.completed).all()
            complete: dict = self.session.query(task_ORM).fillter(task_ORM.completed).all()
            allTask.update(complete)
            return allTask
        except Exception as e:
            return {"status": "failure", "message": str(e)}
    



