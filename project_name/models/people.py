"""Model Providing for data format People and Job"""
from dataclasses import asdict, dataclass
from typing import List

@dataclass
class People:
    """People model"""
    id: str
    gender: str
    name: str
    hash: str
    credits: int

    def dict(self):
        """Return a dict of People"""
        return {k: str(v) for k, v in asdict(self).items()}

@dataclass
class Job:
    """Job model"""
    name: str
    people_list: List[People]
    type: int
    hash: str

    def dict(self) -> dict:
        """Return a dict of Job"""
        return {k: str(v) for k, v in asdict(self).items()}
