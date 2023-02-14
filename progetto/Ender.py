from Node import Node


class Ender(Node):

    def __init__(self) -> None:
        super().__init__(None, None, "Ender")
        self.counter = 0
        self.history = []

    def schedule(self, evt):
        super().schedule(evt)

        evt.dep_time += evt.time

        print(f"\t{evt}")
        print(f"\t{evt.icon} ➡️ 🚪")
        print()
        self.history.append(evt)
        
    def __repr__(self) -> str:
        return "Ender[]"