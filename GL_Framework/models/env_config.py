from dataclasses import dataclass


@dataclass
class EnvConfigModel:
    url: str = None
    port: str = None

@dataclass
class SysVarsForEnvConfig:
    sysEnvVarPrefix: str = "TEST_ENV_"

a= EnvConfigModel()
a.__setattr__("url",10)
print(a.__dict__)