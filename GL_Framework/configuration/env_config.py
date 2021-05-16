import os
from models.env_config import EnvConfigModel, SysVarsForEnvConfig


class EnvironmentConfig:
    def __init__(self, configuration: EnvConfigModel):
        self.configuration = configuration

    def get_env_variable(self, variables=None):
        """
        params:
        variables- list of env variables which should be configured
           if None all variables will be configured
        """
        if variables is None:
            variables = EnvConfigModel.__dict__.keys()
        for var in variables:
            sys_env_name = SysVarsForEnvConfig.sysEnvVarPrefix + str(var).upper()
            self.configuration.__setattr__(var, os.environ.get(sys_env_name))
