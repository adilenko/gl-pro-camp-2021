import requests
from requests.adapters import HTTPAdapter
import logging



class ApiSession:
    def __init__(self):
        self._http_session = None
        self.expires = 86400


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
        adapter = HTTPAdapter(max_retries=2)
        _session.mount('https://', adapter)
        return _session

    def post(self, url, payload_model, **kwargs):
        logging.debug(f"Send POST request to {url} with payload {payload_model}")
        response = self.http_session.post(url=url, json=payload_model, **kwargs)
        return response

    def get(self, url, params, **kwargs):
        logging.debug(f"Send GET request to {url} with parameters {params}")
        response = self.http_session.get(url=f"{url}", params=params, **kwargs)
        return response

    def put(self, url, payload_model, **kwargs):
        logging.debug(f"Send PUT request to {url} with payload {payload_model}")
        response = self.http_session.put(url=url, json=payload_model, **kwargs)
        return response

    def delete(self, url, **kwargs):
        logging.debug(f"Send DELETE request to {url}")
        response = self.http_session.delete(url=f"{url}", **kwargs)
        return response
