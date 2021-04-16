"""Define types for the script."""

from dataclasses import dataclass
from typing import Union


@dataclass
class BashCommand():
    """Bash Command."""

    command: str


Tag = str
Action = Union[str, BashCommand]
