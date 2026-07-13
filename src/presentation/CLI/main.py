import typer
from .commands.task_commands import task_app
from .commands.transaction_commands import transaction_app
from .commands.document_commands import document_app


typerapp = typer.Typer()


@typerapp.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
        raise typer.Exit()


typerapp.add_typer(task_app, name="task")
typerapp.add_typer(transaction_app, name="transaction")
typerapp.add_typer(document_app, name="document")