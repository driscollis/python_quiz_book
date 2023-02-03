# 103_dataclass_difficulties.py

from dataclasses import dataclass, field

@dataclass
class Ford:
    models: list = field(default_factory=["F-150", "Mustang"])

vehicles = Ford()