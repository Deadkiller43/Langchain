from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class DebateState:
    topic: str = ""
    current_round: int = 0
    current_speaker: str = "agent_a"
    arguments: List[Dict[str, Any]] = None
    memory_summary: str = ""
    debate_finished: bool = False
    winner: str = ""
    judgment: str = ""

    def __post_init__(self):
        if self.arguments is None:
            self.arguments = []
