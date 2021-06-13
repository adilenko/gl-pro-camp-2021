from libs.api_client import ApiClient
from configuration.config import get_config_variable_by_name
import pytest


@pytest.fixture(scope="session")
def api_session():
    user = get_config_variable_by_name("user")
    password = get_config_variable_by_name("password")
    ApiClient.loggin()

