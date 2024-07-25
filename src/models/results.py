from dataclasses import dataclass

from models import Event


@dataclass
class Results:

    wins: int
    losses: int
    withdrawls: int
    events: list[Event]
