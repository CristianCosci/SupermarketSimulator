from Event import Event
from Node import Node


class Starter(Node):

    def __init__(self, gen, limit, neighbors) -> None:
        super().__init__(gen, neighbors, name="Starter")
        self.counter = 0
        self.limit = limit
        self.time = 0.0

    def start(self):
        while self.time <= self.limit:
            evt = Event(self.time, self.counter)
            
            super().schedule(evt)   # forse va tolto
            
            print(f"\t➕ {evt}")

            self.time += self.generator.generate()
            self.counter += 1

             
            if isinstance(self.neighbors, Node):
                print(f"\t{evt.icon} ➡️ {self.neighbors}")
                self.neighbors.schedule(evt)
                continue
            
            print("\trolling %")
            chance = self.roll()
        
            print(f"\t{evt.icon} ➡️ {self.neighbors[chance][1]}")
            self.neighbors[chance][1].schedule(evt)
