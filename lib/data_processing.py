import pandas as pd
from lib.custom_types.my_fraction import MyFraction as mf
from lib.custom_types.my_intervals import MyIntervals as mi
from decimal import Decimal
def makeFrame(list: list[int], collumn: str) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame(list, columns=[collumn])
    return result

def makeCorrelationFrame(firstFrame: pd.DataFrame, secondFrame: pd.DataFrame, sortValue: str = None) -> pd.DataFrame:
    result: pd.DataFrame = pd.merge(firstFrame, secondFrame, left_index=True, right_index=True)
    if sortValue != None:
        result = result.sort_values(by=sortValue)    
    return result

def makeDiscretFrame(frame: pd.DataFrame) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame(frame.value_counts()).reset_index()
    result.index=pd.RangeIndex(start=1, stop=result.shape[0]+1)
    result['realativeFreq'] = result.iloc[:, 1].astype(str) + '/' + str(frame.shape[0])
    return result.sort_values(by=result.columns[0])

def makeIntervalFrame(discretFrame: pd.DataFrame, step: int, experCount: int) -> pd.DataFrame:
    left: int = discretFrame.iloc[0,0]
    right: int = left + step
    intervalWalls: list[mi] = [mi(left, right)]
    freq: list[int] = [discretFrame.iloc[0,1]]
    relatFreq: list[mf] = [mf(0, 1)]
    j = 0
    
    for i in range(1, discretFrame.shape[0]):
        value: int = discretFrame.iloc[i, 0]
        valueFrec: int = discretFrame.iloc[i, 1]
        if not (value > left and value <= right):
            relatFreq[j] += mf(freq[j], experCount)
            j+=1
            left = right
            right += step
            intervalWalls.append(mi(left, right))
            freq.append(0)
            relatFreq.append(mf(0, 1))

        freq[j] += valueFrec
    relatFreq[j] += mf(freq[j], experCount)
    result: pd.DataFrame = pd.DataFrame({'intervals': intervalWalls, 'freq': freq, 'relatFreq': relatFreq})
    result.index += 1
    return result

def makeEmpiricFuncFrame(intervalFrame: pd.DataFrame) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame()
    result['empiric'] = intervalFrame['relatFreq'].cumsum()
    result.index += 1
    return result

def makeDiscretVariaticFrame(intervalFrame: pd.DataFrame) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame()
    result['mean'] = intervalFrame['intervals'].apply(lambda interval: interval.calculate_mean())
    result['relatFreq'] = intervalFrame['relatFreq'].apply(lambda relatFreq: relatFreq.value())
    result['density'] = result['relatFreq'].apply(lambda relatFreq: relatFreq/intervalFrame.iloc[0,0].calculate_diff())
    return result
            
def makeEqualFreq(discretVarFrame: pd.DataFrame, intervalFrame: pd.DataFrame, experCount: Decimal) -> pd.DataFrame:
    CONF_INTR_MEANVALUE: Decimal = Decimal('1.96')
    result: pd.DataFrame = pd.DataFrame() 
    selectiveAvg: Decimal = (discretVarFrame['mean'] * discretVarFrame['relatFreq']).sum()
    result['mean'] = discretVarFrame['mean']
    result['deviation'] = discretVarFrame['mean'].apply(lambda mean: mean - selectiveAvg)
    dispersion: Decimal = (result['deviation']**2 * discretVarFrame['relatFreq']).sum()
    unclattEvaul: Decimal = ((experCount/Decimal(experCount-1))*dispersion).sqrt()

    
    return result