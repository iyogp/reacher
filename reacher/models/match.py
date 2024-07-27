from dataclasses import dataclass


@dataclass
class Match:

    id: int
    winner: dict
    loser: dict
    outcome: str
    score: dict
