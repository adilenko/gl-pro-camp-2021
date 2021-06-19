import os
from typing import Optional
import jsonschema
from assertpy import add_extension
from json import loads
from constants import SCHEMAS_DIRECTORY
import allure


@allure.step("Validate json schema")
def schema_valid(self, schema_name: Optional[str], status_code: int = 200):
    if self.val.status_code != status_code:
        self.error(f"Unexpected status code: {self.val.status_code} is NOT {status_code}!")

    try:
        instance = self.val.json()
        schema = schema_to_dict(schema_name)
        jsonschema.validate(instance, schema)
    except jsonschema.ValidationError as validation_error:
        self.error(validation_error)
    return self


def schema_to_dict(file_name):
    with open(os.path.join(SCHEMAS_DIRECTORY, file_name)) as file:
        return loads(file.read())

def add_assertpy_extensions():
    add_extension(schema_valid)
