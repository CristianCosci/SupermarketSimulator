from numpy.random import randint
from typing import TypedDict, Tuple, Union
from Event import Event


class Node:

    def __init__(self, generator, neighbors: Union['Node', TypedDict('Neighbors', {'True': Tuple[int, 'Node'], 'False': Tuple[int, 'Node']})], name="Node 1") -> None:
        self.generator = generator
        self.name = name
        self.neighbors = neighbors  

    def schedule(self, evt: Event) -> None:
        print(f"{self.name} is scheduling 🛠️ ...")
        
        evt.history.append(self.name)

    def roll(self) -> float:
        return randint(1, 100) <= self.neighbors[True][0]

    def __repr__(self) -> str:
        neig = "neighbors: "

        if isinstance(self.neighbors, Node):
            neig += f"{self.neighbors}"
        else:
            neig += f"[Node[{self.neighbors[True][1].name}]({self.neighbors[True][0]}%), Node[{self.neighbors[False][1].name}]({self.neighbors[False][0]}%)"
        
        return f"Node[{self.name}]<gen:{self.generator}, {neig}>"
