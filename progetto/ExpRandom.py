import numpy as np


class ExpRandom:
    def __init__(self, lam):
        self.__lam = lam

    def generate(self):
        return np.random.exponential(self.__lam) 
    
    def __repr__(self) -> str:
        return f"EXPO(λ:{self.__lam})"
