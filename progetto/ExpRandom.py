import numpy as np


class ExpRandom:
    def __init__(self, lam):
        self.__lam = lam

    def generate(self):
        # return np.random.exponential(1/self.d__lam) 
        return np.random.exponential(self.__lam) 
    
    def __repr__(self) -> str:
        return f"EXPO<λ:{self.__lam}>"

    # def generate(self):
    #     return ((-np.log(1-(np.random.uniform(low=0.0,high=1.0)))) / self.__lam)