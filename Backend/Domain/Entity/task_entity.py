from dataclasses import dataclass, field, replace
from datetime import datetime
from typing import Optional, Union
@dataclass
class task_entity():
    
    task_txt: str
    description: Union[str]
    created_at: datetime
    due_time: Union[datetime]
    completed: bool
    priority: int = 1
    id: int | None = field(default=None)


    def mark_complete(self):
        self.completed = True
    
    def replace_items(self, updated_data):
        return replace(self, **updated_data)