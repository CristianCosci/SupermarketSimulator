from Node import Node
from typing import TypedDict, Tuple, Union
from Event import Event


class Processor(Node):

    def __init__(self, generator, neighbors: Union['Node', TypedDict('Neighbors', {'True': Tuple[int, 'Node'], 'False': Tuple[int, 'Node']})], name="Processor 1") -> None:
        super().__init__(generator, neighbors, name)
        
    def schedule(self, evt: Event) -> None:
        super().schedule(evt)

        print(f"\tevent starting time: {evt.time}")
        print(f"\tevent dep_time: {evt.dep_time}")

        time = self.generator.generate()
        evt.dep_time += time

        print(f"\tevt dep_time (updated): {evt.dep_time}")

        if isinstance(self.neighbors, Node):
            print(f"\t➡️ {evt.icon} ➡️ {self.neighbors}")
            self.neighbors.schedule(evt)
            return
        
        print("\trolling %")
        chance = self.roll()
        
        print(f"\t➡️ {evt.icon} ➡️ {self.neighbors[chance][1]}")
        self.neighbors[chance][1].schedule(evt)
