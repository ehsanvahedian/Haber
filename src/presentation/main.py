from .API.main import app as fastapp
from .CLI.main import typerapp

import uvicorn


def fastapi_app():
    print("running fastAPI... :")
    uvicorn.run(fastapp)

cli_app = typerapp