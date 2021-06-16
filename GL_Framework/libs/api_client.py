from libs.api_session import ApiSession
from configuration.config import get_config, get_config_variable_by_name, ConfigModel
from helpers.string_convetor import str_to_base64
from models.Models import LoginModel, FileCount, FilesList
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
    def file_count(folder_id=None):
        url = parse.urljoin(ApiClient.base_url, Path.FILES_PATH + "/count")
        params = asdict(FileCount(folder_id) if folder_id else FileCount())
        response = ApiClient.api_session.get(url, params)
        return response

    @staticmethod
    def get_files(folder_id=None, breadcrumbs=1, offset=0,limit=1000):
        url = parse.urljoin(ApiClient.base_url, Path.FILES_PATH)
        model = FilesList(breadcrumbs=breadcrumbs, offset=offset, limit=limit)
        params = asdict(model(folder_id=folder_id) if folder_id else model)
        response = ApiClient.api_session.get(url, params)
        return response


ApiClient.loggin("gl-procamp-2021@globallogic.com", "DXdUVEFNpHA8LXm")
res = ApiClient.get_files()
a=1
