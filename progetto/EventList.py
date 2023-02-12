from Event import Event

class EventList:

    def __init__(self):
        self.__events = []
  
    def schedule(self, event: Event) -> None:
        if len(self.__events) == 0:
            self.__events.append(event)
            return 
    
        for index, _event in enumerate(self.__events):
            if _event.time > event.time:
                self.__events.insert(index, event)
                break
        
            elif index == len(self.__events) - 1:
                self.__events.append(event)
                break
    
    def get(self) -> Event:
        if len(self.__events) == 0:
            return None

        next_event = self.__events.pop(0)

        return next_event

    def __str__(self) -> str:
        return str(self.__events)
