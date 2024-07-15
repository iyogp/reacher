from datetime import date

from dataclasses import dataclass

from src.models.match import Match


@dataclass
class Event:

    id: int
    name: str
    start_date: date
    end_date: date
    matches: list[Match]
