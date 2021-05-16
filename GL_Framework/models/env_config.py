from dataclasses import dataclass


@dataclass
class EnvConfigModel:
    url: str = None
    port: str = None

@dataclass
class SysVarsForEnvConfig:
    sysEnvVarPrefix: str = "TEST_ENV_"
