import pytest
from conftest import ui_session
from assertpy import assert_that, soft_assertions
from configuration.config import ConfigModel, get_config_variable_by_name



@pytest.fixture
def ui_app(ui_session):
    ui_session.logout()
    yield ui_session


@pytest.mark.ui
def test_login_ui_possitive(ui_app):
    ui_app.login_pege.open()
    user = get_config_variable_by_name(ConfigModel.user)
    ui_app.login_pege.login(get_config_variable_by_name(ConfigModel.user),
                            get_config_variable_by_name(ConfigModel.password))
