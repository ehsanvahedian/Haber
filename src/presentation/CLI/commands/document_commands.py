import typer
from datetime import datetime
from typing import Annotated
from prompt_toolkit.shortcuts import PromptSession
from prompt_toolkit.key_binding import KeyBindings


from Application.UseCases.documentUseCases import documentUseCases
from presentation.pydantic_models.document_pydantic import document_pydantic_input
from Shared.database import get_session

session = get_session(SQLITE=True)
DUC = documentUseCases(session)
document_app = typer.Typer()

# return help while execute document_app
@document_app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
        raise typer.Exit()

#___editors_Keys___
kb = KeyBindings()

@kb.add("c-q")
def _(event):
    event.app.exit()

@kb.add("c-s")
def _(event):
    event.app.exit(result=event.app.current_buffer.text)

@document_app.command()
def add(
        name: Annotated[str, typer.Argument()],
        topic: Annotated[str, typer.Argument(help="optional")] = None
    ):
    """argument: title topic(optional)"""
    try:
        print("ctrl+S to save new content|ctrl+Q to discard changes.")
        print("Go ahead:")
        promptsession = PromptSession(multiline=True, key_bindings=kb)

        print("Enter your text: \n")
        content = promptsession.prompt()
  
        data = document_pydantic_input(name=name, topic=topic, content=content)
  
        DUC.createDocumentUseCase(data)
  
        print("Document added")

    except Exception as e:
        print("error: ", str(e))




@document_app.command()
def edit(
    id: Annotated[int, typer.Argument()]
):
    """etit 'id'"""
    try:
        doc = DUC.getDocumentUseCase(id)

        if not doc:
            print("No document with this id")
            return
        print("ctrl+S to save new content|ctrl+Q to discard changes.")
        print("Go ahead:")
        promptsession = PromptSession(multiline=True, key_bindings=kb)
        
        content = promptsession.prompt(
            message="> ",
            default=doc.content,
        )

        new_data = {"content": content, "updated_at": datetime.now()}

        DUC.updateDocumentUseCase(doc.replace_items(new_data))
        print("You've just edited the document")
  

    except Exception as e:
        print("Error: ", str(e))


@document_app.command()
def get():
    """This will list tasks."""
    try:
        documents = DUC.listDocumentsUseCase()

        if not documents.ducuments:
            print("No document added")
            return
        
        for doc in documents.ducuments:
            print(f"id: {doc.id}: {doc.name}, topic: {doc.topic}, created: {doc.created_at}, last modified: {doc.updated_at}")
            print(f"content: \n{doc.content}")
            print("___________________________________________")

    except Exception as e:
        print("Error: ", str(e))


@document_app.command()
def delete(
    id: Annotated[int, typer.Argument()]
):
    """delete 'id'"""
    confirm =typer.confirm("Are you sure you want to delete task? ", default=True)
    try:
        if confirm:
            res = DUC.deleteDocumentUseCase(id)
            if res["status"] == "success":
                print("document deleted")
                return
            print("no document with this id")
    except Exception as e:
        print("Error: ", str(e))