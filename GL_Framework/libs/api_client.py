from requests import Session

class CommonMethods:
    def __init__(self, api):
        self.api: Session = api


    def post(self, url,  payload_model, **kwargs):
        response = self.api.post(url=url, json=payload_model, **kwargs)
        return response

    def get(self, url, param, **kwargs):
        response = self.api.get(url=f"{url}/{param}", **kwargs)
        return response

    def put(self, url, payload_model, **kwargs):
        response = self.api.put(url=url, json=payload_model, **kwargs)
        return response

    def delete(self, url, param, **kwargs):
        response = self.api.delete(url=f"{url}/{param}", **kwargs)
        return response