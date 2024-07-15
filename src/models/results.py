from dataclasses import dataclass

from src.models.event import Event


@dataclass
class Results:

    wins: int
    losses: int
    withdrawls: int
    events: list[Event]
