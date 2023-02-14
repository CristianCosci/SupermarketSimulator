from ExpRandom import ExpRandom
# from Event import Event
from Starter import Starter
from Ender import Ender
from Processor import Processor


gen = ExpRandom(10)
ender = Ender()


cassa = Processor(gen, ender, "Cassa")
gastronomia = Processor(gen, {True: (70, cassa)}, "Gastronomia")
scaffali = Processor(gen, {True: (80, cassa)}, "Scaffali")
gastronomia.neighbors[False]= (30, scaffali)
scaffali.neighbors[False] = (20, gastronomia)

starter = Starter(
    gen, 
    1000,
    {True: (85, scaffali), False: (15, gastronomia)} 
)


starter.start()

print()
print(ender.history)