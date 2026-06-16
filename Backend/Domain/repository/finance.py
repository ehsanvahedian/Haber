from Domain.Models.Finance import expence
from abc import ABC, abstractmethod

class finance(ABC):

    @abstractmethod
    def expense(self, data:expence, addVoid): 
        return addVoid(data)

