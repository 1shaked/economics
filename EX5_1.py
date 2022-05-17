
from typing import TypedDict
import pandas as pd
import json as js
class workersRes(TypedDict):
    A: int
    B: int
class workersResDict(TypedDict):
    year: workersRes


outputPerWorker: list[list[int]] = [[0, 0],
    [1100,800], # 1
    [1750,1500], # 2
    [2100,2100], # 3
    [2300,2600], # 4
    [2400,3000], # 5
    [2450,3000], # 6
    [2450, 2900] # 7
] # the index the the worker amount and first is for type a second for type b
# apl: dict[int: dict[str:int]] = dict()
apl: workersResDict = dict()
ml: workersResDict = dict()


for index, val in enumerate(outputPerWorker):
    if index == 0:
        apl[index] = 0
        ml[index] = 0
        continue
    apl[str(index)] = {"A": val[0] / index, "B": val[1] / index} 
    ml[str(index)] = {"A": val[0] - outputPerWorker[index - 1][0], "B": val[1] - outputPerWorker[index - 1][1]}
    
    
    
apl_df = pd.DataFrame(apl)
print(js.dumps(apl, indent=4))
print(apl_df)
print(ml)
ml_df = pd.DataFrame(ml)
print(js.dumps(ml, indent=4))
print(ml_df)

