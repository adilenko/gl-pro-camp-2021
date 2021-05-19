import os
import json
import constants as const
from dataclasses import dataclass
import yaml


@dataclass
class EnvConfigModel:
    url: str = None
    _port: int = None
    user: str = None
    password: str = None

    @property
    def port(self):
        return int(self._port)


def get_local_config(path=None):
    """
    TODO
    """
    config = EnvConfigModel()
    variables = config.__dict__.keys()
    if path is None:
        path = const.CONFIG_FILE
    with open(path) as file:
        conf = json.load(file)
    for var in variables:
        prop_name = var[1:] if var[0] == '_' else var
        config.__setattr__(var, conf.get(prop_name, None))
    return config


def get_config_form_env_variable():
    """
    TODO
    """
    config = EnvConfigModel()
    variables = config.__dict__.keys()
    for var in variables:
        prop_name = var[1:] if var[0] == '_' else var
        sys_env_name = const.ENV_VAR_PREFIX + str(prop_name).upper()
        config.__setattr__(var, os.environ.get(sys_env_name, None))
    return config


def get_config_from_yaml(path=None):
    """
    TODO

    """
    config = EnvConfigModel()
    if path is None:
        return config
    with open(path) as f:
        yaml_conf = yaml.safe_load(f)
    conf_var = config.__dict__.keys()
    for var in conf_var:
        prop_name = var[1:] if var[0] == '_' else var
        config.__setattr__(var, yaml_conf.get(prop_name, None))
    return config


def get_config(yaml_conf_file=None, local_conf_file=None):
    """
    TODO
    """
    final_config = EnvConfigModel()
    conf_var = final_config.__dict__.keys()
    configs = [get_config_form_env_variable(),
               get_config_from_yaml(yaml_conf_file),
               get_local_config(local_conf_file)]
    for var in conf_var:
        for conf in configs:
            if conf.__getattribute__(var):
                final_config.__setattr__(var, conf.__getattribute__(var))
                break
    return final_config
