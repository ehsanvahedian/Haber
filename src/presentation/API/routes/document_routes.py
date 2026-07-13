from fastapi.routing import APIRouter
from fastapi import Depends
from typing import Annotated

from Application.UseCases.documentUseCases import documentUseCases
from ...pydantic_models.document_pydantic import document_pydantic, document_pydantic_input
from Shared.database import get_session

session = get_session()
DUC = documentUseCases(session)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)



@router.get("/")
async def list_documents():
    return DUC.listDocumentsUseCase()


@router.get("/{id}")
async def get_document(id: int):
    return DUC.getDocumentUseCase(id)


@router.post("/add")
async def add_document(data: Annotated[document_pydantic_input, Depends(document_pydantic_input)]):
    return DUC.createDocumentUseCase(data)


@router.put("/update")
async def update_document(data: Annotated[document_pydantic, Depends(document_pydantic)]):
    return DUC.updateDocumentUseCase(data)


@router.delete("/{id}")
async def delete_document(id: int):
    return DUC.deleteDocumentUseCase(id)