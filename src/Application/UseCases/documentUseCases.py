from Infrastructure.DB.repo_implement.document_repo_impl import document_repo_impl


class documentUseCases:

    def __init__(self, session):
        self.implement = document_repo_impl(session)

    def createDocumentUseCase(self, data):
        document = self.implement.build_document(data)
        return self.implement.add_document(document)

    def updateDocumentUseCase(self, data):
        current_data = self.implement.get_document(data.id)
        updated_data = {k: v for k, v in data.__dict__.items() if v is not None}
        updated_data = current_data.replace_items(updated_data)

        return self.implement.update_document(updated_data)

    def deleteDocumentUseCase(self, id):
        return self.implement.delete_document(id)

    def getDocumentUseCase(self, id):
        return self.implement.get_document(id)

    def listDocumentsUseCase(self):
        return self.implement.list_documents()