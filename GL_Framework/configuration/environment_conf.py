import os
import json
import constants as const
from dataclasses import dataclass
import yaml


@dataclass
class EnvConfigModel:
    url: str = None
    port: str = None
    user: str = None
    password: str = None
    # properties which should be converted will be hidden
    _someIntProp: int = None

    @property
    def someIntProp(self):
        return int(self._someIntProp) if self._someIntProp else None


def get_local_config(path=None):
    """
    Read data from local json config
    Properties in file has the same name as in class
    """
    config = EnvConfigModel()
    variables = config.__dict__.keys()
    if path is None:
        path = const.CONFIG_FILE
    with open(path) as file:
        conf = json.load(file)
    for var in variables:
        # remove "_" from the name of a hidden properties
        # because in file properties do not have such prefix
        prop_name = var[1:] if var[0] == '_' else var
        config.__setattr__(var, conf.get(prop_name, None))
    return config


def get_config_form_env_variable():
    """
    Read data from env variables.
    Env Variable should have name FW_ENV_PROPERTYNAME
    """
    config = EnvConfigModel()
    variables = config.__dict__.keys()
    for var in variables:
        # remove "_" from the name of a hidden properties
        # because env variables do not have such prefix
        prop_name = var[1:] if var[0] == '_' else var
        sys_env_name = const.ENV_VAR_PREFIX + str(prop_name).upper()
        config.__setattr__(var, os.environ.get(sys_env_name, None))
    return config


def get_config_from_yaml(path=None):
    """
    Read config data from yaml file
    Properties in file has the same name as in class

    """
    config = EnvConfigModel()
    if path is None:
        return config
    with open(path) as f:
        yaml_conf = yaml.safe_load(f)
    conf_var = config.__dict__.keys()
    for var in conf_var:
        # remove "_" from the name of a hidden properties
        # because in file properties does not have such prefix
        prop_name = var[1:] if var[0] == '_' else var
        config.__setattr__(var, yaml_conf.get(prop_name, None))
    return config


def get_config(yaml_conf_file=None, local_conf_file=None):
    """
    Read config data from Env Var, yaml file and local
    json file.
     If property is found in some source it will not be
    searched in another
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
