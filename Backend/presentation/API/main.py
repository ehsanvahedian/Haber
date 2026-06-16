from fastapi import FastAPI, Depends
from Infrastructure.DB.hello_repo_impl import hello_repo_impl
from Shared.database import get_session
from typing import Annotated
from Domain.value_objects.hello import hello
HRP = hello_repo_impl(get_session())
app = FastAPI()


@app.get("/")
async def root():
    return("HEllo welcome !!")

@app.get("/hello")
async def get_hello():
    return HRP.get_hello()

@app.post("/hello")
async def set_hello(data: Annotated[hello, Depends(hello)]):
    print(data)
    return HRP.set_hello(data=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)