import logging

import pytest
from libs.api_client import ApiClient
from libs.assertpy_extensions import add_assertpy_extensions
from configuration.config import get_config_variable_by_name, ConfigModel
from libs.ui.browser_provider import BrowserProvider
from libs.ui.cosmo_id import CosmoID


@pytest.fixture(scope="session")
def api_session():
    user = get_config_variable_by_name(ConfigModel.user)
    password = get_config_variable_by_name(ConfigModel.password)
    response = ApiClient.loggin(user, password)
    if response.status_code != 200:
        raise Exception("Error during login.")
    return ApiClient

@pytest.fixture(scope="session")
def ui_session():
    fixture = CosmoID(driver=BrowserProvider.get_browser(get_config_variable_by_name(ConfigModel.browser)))
    try:
        fixture.ensure_login(user=get_config_variable_by_name(ConfigModel.user))
    except Exception as e:
        logging.error("Loggin failed")
    yield fixture
    fixture.ensure_logout()
    fixture.destroy()



def pytest_configure(config):
    add_assertpy_extensions()
