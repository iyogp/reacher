from dataclasses import dataclass

from reacher.models.event import Event


@dataclass
class Results:

    wins: int
    losses: int
    withdrawls: int
    events: list[Event]
