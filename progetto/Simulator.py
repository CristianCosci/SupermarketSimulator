from Event import Event
from EventList import EventList
from PoissonRandom import PoissonRandom
from copy import deepcopy


class Simulator:

    def __init__(self, lam: float, end=15000):
        self.history = []

        self.__running = False
        self.__end = end
        
        self.__arrivals = 0
        self.__departures = 0
        self.__current_jobs = 0

        self.__current_time = 0
        self.__old_time = 0
        self.__area = 0
        self.__btime = 0

        self.n_mean = 0
        self.U = 0
        self.w_mean = 0
        self.throughput = 0

        self.__lam = lam
        self.__generator = PoissonRandom(self.__lam)

        self.__events = EventList()
        self.__events.schedule(Event(Event.ARRIVAL, 0))       
        self.__events.schedule(Event(Event.DEPARTURE, self.__end))

    def start(self):
        self.__running = True

        while self.__running:
            self.__clock()

        print("End Simulation 🚀")

    def __clock(self):
        event = self.__events.get()
        self.__current_time = event.time

        if event.type == Event.ARRIVAL:
            self.history.append([deepcopy(event), None]) # ricontrollare
            self.__arrival()

        elif event.type == Event.DEPARTURE:
            self.history[self.__departures][1] = deepcopy(event)
            self.__departure()

        elif event.type == Event.SIM_END:
            self.__sim_end()
            self.__running = False

    def __arrival(self):
        self.__stat_accumulate()
        self.__current_jobs += 1
        self.__arrivals += 1

        next_arrival_time = self.__generator.generate()

        self.__events.schedule(Event(Event.ARRIVAL, self.__current_time + next_arrival_time))       
        
    def __departure(self):
        self.__stat_accumulate()
        self.__current_jobs -= 1
        self.__departures += 1

        if self.__current_jobs > 0:
            next_departure_time = self.__generator.generate()
            self.__events.schedule(Event(Event.DEPARTURE, self.__current_time + next_departure_time))

    def __sim_end(self) -> list:
        self.n_mean = self.__area / self.__current_time
        self.w_mean = self.__area / self.__departures
        self.throughput = self.__departures / self.__current_time
        self.U = self.__btime / self.__current_time
        
        print("Risultati della simulazione")
        print("Arrivi: {0}".format(self.__arrivals))
        print("Partenze: {0}".format(self.__departures))
        print("Throughput: {0}".format(self.throughput))
        print("Utilizzazione: {0}".format(self.U))
        print("Numero medio di clienti nel sistema: {0}".format(self.n_mean))
        print("Tempo medio di permanenza nel sistema: {0}".format(self.w_mean))

        return (self.__arrival, self.__departures, self.throughput, self.U, self.n_mean, self.w_mean)

    def __stat_accumulate(self):
        interval = self.__current_time - self.__old_time
        self.__old_time = self.__current_time

        if self.__current_jobs > 0:
            self.__area += interval * self.__current_jobs
            self.__btime += interval
