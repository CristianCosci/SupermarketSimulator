from random import choice
from typing import List


class Event:

    def __init__(self, time: int, id=0):
        self.time = time
        self.dep_time = 0
        self.id=id
        self.history: List[str] = []
        self.icon = choice(['🧔', '👩', '👨', '🧕']) 
    
    def __str__(self) -> str:
        return f"{self.icon} <💳: {self.id}, 🟢: {self.time}, 🔴: {self.dep_time}, 📊: {self.history}>"
    
    def __repr__(self) -> str:
        return f"Event[{self.id}]<start: {self.time}, end:{self.dep_time}, history: {self.history}>"
    

    
    
