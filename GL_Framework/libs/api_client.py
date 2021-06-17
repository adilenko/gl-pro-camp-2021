from api_session import ApiSession

class ApiClient:
    def __init__(self, api):
        self.api = ApiSession().get_default_session()


    def post(self, url,  payload_model, **kwargs):
        response = self.api.post(url=url, json=payload_model, **kwargs)
        return response

    def get(self, url, params, **kwargs):
        response = self.api.get(url=f"{url}", params=params, **kwargs)
        return response

    def put(self, url, payload_model, **kwargs):
        response = self.api.put(url=url, json=payload_model, **kwargs)
        return response

    def delete(self, url, **kwargs):
        response = self.api.delete(url=f"{url}", **kwargs)
        return response