from dataclasses import dataclass


@dataclass
class Profile:

    id: int
    first_name: str
    last_name: str
    gender: str
    nationality: str
    singles_utr: str
