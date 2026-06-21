from pydantic import BaseModel
from typing import Union
from datetime import datetime

class task_pydantic(BaseModel):
    task_txt: str
    description: Union[str | None]
    created_at: datetime
    due_time: Union[datetime | None]
    completed: bool
    priority: int = 1