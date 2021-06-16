import pytest
from libs.api_client import ApiClient
from configuration.config import ConfigModel, get_config_variable_by_name
from assertpy import assert_that


def test_login():
    resp = ApiClient.loggin(
        get_config_variable_by_name(ConfigModel.user),
        get_config_variable_by_name(ConfigModel.password))
    assert resp.status_code == 200

def test_file(api_session):
    res = api_session.file_count()
    assert_that(res).schema_valid("file_list.json")
    assert res.json()["total"] == 58

def test_file_list_schema(api_session):
    res = api_session.get_files()
    assert_that(res).schema_valid("file_list.json")
