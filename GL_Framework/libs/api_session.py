from requests import request, Session


class ApiSession:
    http_session = Session()

    @classmethod
    def get_default_session(cls):
        headers = {'content-type': 'application/json'}
        cls.http_session.headers.update(headers)
        return cls.http_session

