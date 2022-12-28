import pandas as pd
import numpy as np

def range():
    #calculate the range of pw#
    df = pd.read_csv("iris.csv")
    range_pw =  np.max(df["pw"]) - np.min(df["pw"])
    return (range_pw) 

rn = range()
print(rn)

