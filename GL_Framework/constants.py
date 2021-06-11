import os

PROJECT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CONFIG_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "configuration")
CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, "config.yaml")
ENV_VAR_PREFIX: str = "FW_ENV_"
