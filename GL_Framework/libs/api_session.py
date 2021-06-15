import requests


class ApiSession:
    def __init__(self):
        self._http_session = None
        self.expires = 86400
        # self.token = None
        # self.base_url = base_url

    @property
    def http_session(self):
        if self._http_session is None:
            self._http_session = ApiSession.get_default_session()
        return self._http_session

    @classmethod
    def get_default_session(cls):
        _session = requests.Session()
        headers = {'content-type': 'application/json'}
        _session.headers.update(headers)
        return _session

    def post(self, url, payload_model, **kwargs):
        response = self.http_session.post(url=url, json=payload_model, **kwargs)
        return response

    def get(self, url, params, **kwargs):
        response = self.http_session.get(url=f"{url}", params=params, **kwargs)
        return response

    def put(self, url, payload_model, **kwargs):
        response = self.http_session.put(url=url, json=payload_model, **kwargs)
        return response

    def delete(self, url, **kwargs):
        response = self.http_session.delete(url=f"{url}", **kwargs)
        return response
