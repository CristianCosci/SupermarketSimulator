from Node import Node


class Processor(Node):

    def __init__(self, generator, neighbors, name="Processor 1") -> None:
        super().__init__(generator, neighbors, name)
        
    def schedule(self, evt):
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

    # def roll(self):
    #     return random.uniform(10) >= self.neighbors[True][0]

    # def __repr__(self) -> str:
    #     return f"Node[{self.name}]<gen:{self.generator}, neighbors:{self.neighbors}>"
