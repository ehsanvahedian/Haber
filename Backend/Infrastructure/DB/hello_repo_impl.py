from Domain.repository.hello import helloRepository
from Domain.value_objects.hello import hello
from .hello_DTO import Hello

class hello_repo_impl(helloRepository):
    def __init__(self, session):
        self.session = session

    def get_hello(self):
        result = self.session.query(Hello)
        return(result.all())

    def set_hello(self, data: hello):
        data = Hello(message = data.message)
        self.session.add(data)
        self.session.commit()
        return("OK")