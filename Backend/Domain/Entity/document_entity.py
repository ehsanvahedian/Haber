from dataclasses import dataclass
from datetime import datetime

@dataclass
class document_entity:
    id: int
    name: str
    topic: str
    content: str
    created_at: datetime
    updated_at: datetime
    
    def update_date(self, date: datetime):
        self.updated_at = date
