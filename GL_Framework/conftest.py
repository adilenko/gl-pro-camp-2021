import pytest
from libs.api_client import ApiClient
from libs.assertpy_extensions import add_assertpy_extensions
from configuration.config import get_config_variable_by_name, ConfigModel


@pytest.fixture(scope="session")
def api_session():
    user = get_config_variable_by_name(ConfigModel.user)
    password = get_config_variable_by_name(ConfigModel.password)
    response = ApiClient.loggin(user, password)
    if response.status_code != 200:
        raise Exception("Error during login.")
    return ApiClient


def pytest_configure(config):
    add_assertpy_extensions()
