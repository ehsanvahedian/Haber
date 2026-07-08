# import click
# from presentation.pydantic_models.transaction_pydantic import transaction_pydantic_input, TransactionType
# from Application.UseCases.transactionUseCases import transactionUseCases
# TUC = transactionUseCases()


# @click.group()
# def transactions():
#     pass


# @click.command()
# @click.option("-c", is_flag=True)
# @click.argument("amount", type=int)
# @click.argument("type", type=str)
# @click.argument("currency", type=str)
# def add_transaction(amount, type, currency, c):
#     """
#         Call 'add_task amount-of-transaction 'i'-for-income-'e'-for-expense currency' to add a task.
#         for more detailed task call 'add_task -c'
#     """
#     if c:
#         title = click.prompt("title:  (empty for None) ", type=str)
#         amount = click.prompt("amount:  (empty for None) ", type=int)
#         type = click.prompt("expense or income  (empty for Expense) enter 'i' for Income: ", type=str)
#         type = TransactionType.INCOME if type == 'i' else TransactionType.EXPENSE
#         source = click.prompt("source: (empty for None) ", type=str)
#         datetime = click.prompt(
#             "date:  (empty for None) ",
#             type=click.DateTime(formats=["%Y-%m-%d %H:%M"]),
#             default=None,
#             show_default=False
#         )
#         description = click.prompt("description:  (empty for None) ", type=str)
#         data = transaction_pydantic_input(title=title,amount=amount, type=type, source=source, date=datetime,description=description)
#         click.echo(TUC.createTransactionUseCase(data))
#         return
#     transaction_type = TransactionType.INCOME if type == 'i' else TransactionType.EXPENSE

#     data = transaction_pydantic_input(amount=amount, type=transaction_type, currency=currency)
#     click.echo(TUC.createTransactionUseCase(data))

    


# @click.command()
# @click.option("-c", is_flag=True)
# def get_tasks(c):
#     """
#         Call 'add_task title-of-task' to add a task.
#         for more detailed task call 'add_task -c'
#     """
#     if c:
#         name = click.prompt("name: ")
#         click.echo(name)

# @click.command()
# @click.option("-c", is_flag=True)
# def update_task(c):
#     """
#         Call 'add_task title-of-task' to add a task.
#         for more detailed task call 'add_task -c'
#     """
#     if c:
#         name = click.prompt("name: ")
#         click.echo(name)

# @click.command()
# @click.option("-c", is_flag=True)
# def complete_task(c):
#     """
#         Call 'add_task title-of-task' to add a task.
#         for more detailed task call 'add_task -c'
#     """
#     if c:
#         name = input("name: ")
#         print(name)

# @click.command()
# @click.option("-c", is_flag=True)
# def delete_task(c):
#     """
#         Call 'add_task title-of-task' to add a task.
#         for more detailed task call 'add_task -c'
#     """
#     if c:
#         name = input("name: ")
#         print(name)


# # return SimpleNamespace(
# #     add_task=add_task,
# #     get_tasks=get_tasks,
# #     update_task=update_task,
# #     complete_task=complete_task,
# #     delete_task=delete_task
# # )
