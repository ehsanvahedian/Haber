from abc import ABC, abstractmethod
from Domain.value_objects.hello import hello
class helloRepository(ABC):
    
    @abstractmethod
    def get_hello(): ...

    @abstractmethod
    def set_hello(self, data: hello): ...