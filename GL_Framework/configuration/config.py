import os

import constants as const
from dataclasses import dataclass
import yaml
from configuration.local_config import LocalConfig


# local config stored not in variables but in json file
@dataclass
class ConfigModel:
    base_url: str = "base_url"
    port: str = "port"
    user: str = "user"
    password: str = "password"
    browser: str = "browser"
    # properties which should be converted will be hidden
    _timeout: str = "timeout"

    @property
    def timeout(self):
        if isinstance(self._timeout,int):
            return self._timeout
        if self._timeout.isdigit():
            return int(self._timeout)
        return self._timeout



def get_local_config():
    """
    Read data from local json config
    Properties in file has the same name as in class
    """
    config = ConfigModel()
    # convert class to dict
    conf = dict((name, getattr(LocalConfig, name)) for name in dir(LocalConfig) if not name.startswith('__'))
    for key, val in config.__dict__.items():
        config.__setattr__(key, conf.get(val, None))
    return config


def get_config_form_env_variable():
    """
    Read data from env variables.
    Env Variable should have name FW_ENV_PROPERTYNAME
    """
    config = ConfigModel()
    for key, val in config.__dict__.items():
        sys_env_name = const.ENV_VAR_PREFIX + str(val).upper()
        config.__setattr__(key, os.environ.get(sys_env_name, None))
    return config


def get_config_from_yaml(path=None):
    """
    Read config data from yaml file
    Properties in file has the same name as in class
    """
    config = ConfigModel()
    if path is None:
        path = const.CONFIG_FILE
    with open(path) as f:
        yaml_conf = yaml.safe_load(f)
    for key, val in config.__dict__.items():
        config.__setattr__(key, yaml_conf.get(val, None))
    return config


def get_config(yaml_conf_file=None):
    """
    Read config data from Env Var, yaml file and local
    config class
     If property is found in some source it will not be
    searched in another
    """
    final_config = ConfigModel()
    conf_var = final_config.__dict__.keys()
    configs = [get_config_form_env_variable(),
               get_config_from_yaml(yaml_conf_file),
               get_local_config()]
    for var in conf_var:
        for conf in configs:
            if conf.__getattribute__(var):
                final_config.__setattr__(var, conf.__getattribute__(var))
                break
            final_config.__setattr__(var, None)
    return final_config


def get_config_variable_by_name(name, yaml_conf_file=None):
    config = get_config(yaml_conf_file)
    return config.__getattribute__(name)

