
from dataclasses import dataclass, asdict



# local config stored not in variables but in json file
@dataclass
class ConfigModel:
    base_url: str = None
    port: str = None
    user: str = None
    password: str = None
    # properties which should be converted will be hidden
    _timeout: int = None

a=1