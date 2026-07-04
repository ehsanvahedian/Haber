from Infrastructure.DB.repo_implement.transaction_repo_impl import transaction_repo_impl
from Domain.value_objects.Money import Money
from Shared.database import get_session


class transactionUseCases:
    def __init__(self):
        session = get_session()
        self.implement = transaction_repo_impl(session)

    def createTransactionUseCase(self, data):
        transaction = self.implement.build_transaction(data)
        return self.implement.add_transaction(transaction)

    def updateTransactionUseCase(self, data):
        current_data = self.implement.get_transaction(data.id).to_entity()
        updated_data = {k: v for k, v in data.__dict__.items() if v is not None}
        updated_data = current_data.replace_items(updated_data)

        return self.implement.update_transaction(updated_data)

    def deleteTransactionUseCase(self, id):
        return self.implement.delete_transaction(id)

    def listTransactionsByDateUseCase(self):
        return self.implement.list_by_date()

    def listExpensesUseCase(self):
        return self.implement.list_expenses()

    def listIncomesUseCase(self):
        return self.implement.list_incomes()

    def getTransactionUseCase(self, id):
        return self.implement.get_transaction(id)