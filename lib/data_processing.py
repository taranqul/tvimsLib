import pandas as pd
from fractions import Fraction as Fr
def makeFrame(List: list[float], Collumn: str) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame(List, columns=[Collumn])
    return result

def makeCorrelationFrame(firstFrame: pd.DataFrame, secondFrame: pd.DataFrame, sortValue: str = None) -> pd.DataFrame:
    result: pd.DataFrame = pd.merge(firstFrame, secondFrame, left_index=True, right_index=True)
    if sortValue != None:
        result = result.sort_values(by=sortValue)    
    return result

def makeDiscretFrame(Frame: pd.DataFrame) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame(Frame.value_counts()).reset_index()
    result['freq'] = result.iloc[:, 1].astype(str) + '/' + str(Frame.shape[0])
    return result