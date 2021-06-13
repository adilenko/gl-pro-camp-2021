from my_libs.api_session import ApiSession
from configuration.config import get_config, get_config_variable_by_name, ConfigModel
from helpers.string_convetor import str_to_base64
from models.Models import LoginModel
from dataclasses import asdict
from urllib import parse
from configuration.config import ConfigModel


class Path:
    LOGIN_URL = "api/v1/login"
    FILES_PATH = "api/metagenid/v2/files"


class ApiClient:
    base_url = get_config_variable_by_name(ConfigModel.base_url)
    api_session = ApiSession()

    @staticmethod
    def loggin(user, password):
        aut = str_to_base64(f"{user}:{password}")
        url = parse.urljoin(ApiClient.base_url, Path.LOGIN_URL)
        ApiClient.api_session.http_session.headers.update({"authorization": f"Basic {aut}"})
        login_model = asdict(LoginModel(expiry=86400, login_from="login page"))
        response = ApiClient.api_session.post(url, login_model)
        ApiClient.api_session.http_session.headers.update({"x-token": f"{response.json()['token']}"})
        return response

    @staticmethod
    def file_count(folder_id):
        url = parse.urljoin(ApiClient.base_url, Path.FILES_PATH +"/count")
        params = {"folder_id": "84c966d5-8dce-429d-8f92-44d5e28b1581", "_": "1623618114543"}
        response = ApiClient.api_session.get(url, params)
        return response.json()



ApiClient.loggin("gl-procamp-2021@globallogic.com", "DXdUVEFNpHA8LXm")
res = ApiClient.file_count(1)
a = 1
