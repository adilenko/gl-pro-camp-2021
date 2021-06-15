import pytest
from libs.api_client import ApiClient
from configuration.config import get_config_variable_by_name, ConfigModel


@pytest.fixture(scope="session")
def api_session():
    user = get_config_variable_by_name(ConfigModel.user)
    password = get_config_variable_by_name(ConfigModel.password)
    response = ApiClient.loggin(user, password)
    return ApiClient
