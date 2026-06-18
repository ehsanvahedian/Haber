from abc import ABC, abstractmethod
from Domain.Entity.document_entity import document_entity
class document_repository(ABC):
    
    @abstractmethod
    def add_document(self, document_data: document_entity): ...

    @abstractmethod
    def update_document(self, document_data: document_entity): ...

    @abstractmethod
    def delete_document(self, document_data: document_entity): ...

    @abstractmethod
    def list_by_date(self): ...


    def biuld_document(self, document_data):
        return document_entity(**document_data.__dict__)

