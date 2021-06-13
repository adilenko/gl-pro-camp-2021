from api_session import ApiSession
from configuration.config import get_config, get_config_variable_by_name, ConfigModel, ConfigVariables
from helpers.string_convetor import str_to_base64
from models.Models import LoginModel
from dataclasses import asdict
from urllib import parse

LOGIN_URL = "api/v1/login"


class ApiClient:
    def __init__(self):
        self.base_url = get_config_variable_by_name("base_url")
        self.api = ApiSession()

    def loggin(self, user, password):
        aut = str_to_base64(f"{user}:{password}")
        url = parse.urljoin(self.base_url, LOGIN_URL)
        self.api.http_session.headers.update({"authorization": f"Basic {aut}"})
        login_model = asdict(LoginModel(expiry=86400, login_from="login page"))
        response = self.api.post(url, login_model)
        self.api.http_session.headers.update({"x-token": f"Basic {response.json()['token']}"})
        return response


    def file(self):
        return self.api

api = ApiClient()
api.loggin("gl-procamp-2021@globallogic.com", "DXdUVEFNpHA8LXm")
res = api.file()
a=1