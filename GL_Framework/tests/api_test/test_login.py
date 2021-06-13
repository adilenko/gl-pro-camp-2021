import pytest
from my_libs.api_client import ApiClient
from configuration.config import ConfigModel, get_config_variable_by_name


def test_login():
    resp = ApiClient.loggin(
        get_config_variable_by_name(ConfigModel.user),
        get_config_variable_by_name(ConfigModel.password))
    assert resp.status_code == 200

def test_file(api_session):
    res = api_session.file_count(1)
    assert res["total"] == 58


