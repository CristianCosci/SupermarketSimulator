# non ne ho la più pallida idea
from numpy import random


class PoissonRandom:

    # è possibile chiamare i parametri anche λ
    def __init__(self, lam=0.61) -> None:
        self.__lam = lam
        self.__generator = random.default_rng(seed=69)

    def generate(self) -> float:
        return self.__generator.poisson(self.__lam)
