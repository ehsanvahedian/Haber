from dataclasses import dataclass
from datetime import datetime
from Domain.value_objects.Money import Money
from enum import Enum


class TransactionType(Enum):
    EXPENSE = "expense"
    INCOME = "income"

@dataclass
class transaction_entity:
    id: str
    title: str
    amount: Money
    type: TransactionType
    source: str
    date: datetime
    description: str

    


