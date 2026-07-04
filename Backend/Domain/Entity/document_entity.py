from dataclasses import dataclass, field, replace
from datetime import datetime

@dataclass
class document_entity:
    name: str
    topic: str
    content: str
    created_at: datetime
    updated_at: datetime
    id: int | None = field(default=None)
    
    def replace_items(self, updated_data):
        return replace(self, **updated_data)