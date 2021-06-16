from dataclasses import dataclass


@dataclass
class LoginModel:
    expiry: int = None
    login_from: str = None


@dataclass
class FileCount:
    folder_id: str = "84c966d5-8dce-429d-8f92-44d5e28b1581"
    _: str = "1623618114543"


@dataclass
class FilesList:
    breadcrumbs: int = 1
    offset: int = 0
    limit: int = 0
    folder_id: str = "84c966d5-8dce-429d-8f92-44d5e28b1581"
    _: str = "1623618114543"
