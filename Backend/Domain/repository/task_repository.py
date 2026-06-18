from abc import ABC, abstractmethod
from Domain.Entity.task_entity import task_entity
class task_repository(ABC):
    
    @abstractmethod
    def add_task(self, task_data: task_entity): ...

    @abstractmethod
    def update_task(self, task_data: task_entity): ...

    @abstractmethod
    def delete_task(self, task_data: task_entity): ...

    @abstractmethod
    def list_by_status(self): ...

    def biuld_task(self, task_data):
        return task_entity(**task_data.__dict__)

    #You can add list by date
    
    #You can add list by priority


