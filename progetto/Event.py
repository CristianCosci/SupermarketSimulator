class Event:
    ARRIVAL = 0
    DEPARTURE = 1
    SIM_END = 2
    __strings = ["ARRIVAL", "DEPARTURE", "SIM_END"]

    def __init__(self, type: int, time: int):
        self.type = type
        self.time = time
  
    def __str__(self) -> str:
        return f"Event {self.__strings[self.type]} @ {self.time}"

    def __repr__(self) -> str:
        return f"Event <type: {self.__strings[self.type]}, time: {self.time}>"

