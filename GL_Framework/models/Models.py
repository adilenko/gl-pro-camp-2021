from dataclasses import dataclass

@dataclass
class LoginModel:
    expiry: int = None
    login_from: str = None

