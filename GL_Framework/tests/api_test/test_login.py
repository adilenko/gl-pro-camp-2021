import pytest
from libs.api_client import ApiClient
from configuration.config import ConfigModel, get_config_variable_by_name
from assertpy import assert_that, soft_assertions
from helpers.fake import fake


def test_login():
    resp = ApiClient.loggin(
        get_config_variable_by_name(ConfigModel.user),
        get_config_variable_by_name(ConfigModel.password))
    assert_that(resp.status_code).is_equal_to(200)


def test__invalide_login():
    name = fake.name()
    password = fake.password()
    resp = ApiClient.loggin(
        name,
        password)
    with soft_assertions():
        assert_that(resp.status_code).is_equal_to(401)
        assert_that(resp.text).is_equal_to("You are required to log in with a valid username and password")

# def test_file(api_session):
#     res = api_session.file_count()
#     assert_that(res).schema_valid("file_list.json")
#     assert res.json()["total"] == 58

def test_file_list_schema(api_session):
    res = api_session.get_files()
    assert_that(res).schema_valid("file_list.json")
