import pandas as pd
from lib.custom_types.my_fraction import MyFraction as mf
from lib.custom_types.my_intervals import MyIntervals as mi
from lib.utils import laplass as lp
from decimal import Decimal
def makeFrame(list: list[int], collumn: str) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame(list, columns=[collumn])
    return result

def makeCorrelationFrame(firstFrame: pd.DataFrame, secondFrame: pd.DataFrame, sortValue: str = None) -> pd.DataFrame:
    result: pd.DataFrame = pd.merge(firstFrame, secondFrame, left_index=True, right_index=True)
    if sortValue:
        result = result.sort_values(by=sortValue)
        result.reset_index()
        result.index += 1
    return result

def makeDiscretFrame(frame: pd.DataFrame) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame(frame.value_counts()).reset_index()
    result['realativeFreq'] = result.iloc[:, 1].astype(str) + '/' + str(frame.shape[0])
    result = result.sort_values(by=result.columns[0])
    result = result.reset_index(drop=True)
    result.index += 1
    return result

def makeIntervalFrame(discretFrame: pd.DataFrame, step: int, experCount: int) -> pd.DataFrame:
    left: int = discretFrame.iloc[0,0]
    right: int = left + step
    intervalWalls: list[mi] = [mi(left, right, quantize_val='1', delimeter='-')]
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
            intervalWalls.append(mi(left, right, quantize_val='1', delimeter='-'))
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
    return result

def makeDiscretVariaticFrame(intervalFrame: pd.DataFrame) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame()
    STEP: Decimal = intervalFrame.iloc[0,0].calculate_diff()
    result['mean'] = intervalFrame['intervals'].apply(lambda interval: interval.calculate_mean())
    result['relatFreq'] = intervalFrame['relatFreq'].apply(lambda relatFreq: relatFreq.value())
    result['density'] = result['relatFreq'].apply(lambda relatFreq: relatFreq / STEP)
    return result
            
def makeEqualFreq(discretVarFrame: pd.DataFrame, intervalFrame: pd.DataFrame, EXPER_COUNT: Decimal, STR_Q_VALUE: str):
    CONF_INTR_MEANVALUE: Decimal = Decimal('1.96')
    ONE_DECIMAL = Decimal(1)
    DEC_Q_VALUE = Decimal(STR_Q_VALUE)
    STEP: Decimal = intervalFrame.iloc[0,0].calculate_diff()

    result: pd.DataFrame = pd.DataFrame() 
    selectiveAvg: Decimal = (discretVarFrame['mean'] * discretVarFrame['relatFreq']).sum()
    result['mean'] = discretVarFrame['mean']
    result['deviation'] = discretVarFrame['mean'].apply(lambda mean: mean - selectiveAvg)
    dispersion: Decimal = (result['deviation']**2 * discretVarFrame['relatFreq']).sum()

    unclattEvaul: Decimal = ((EXPER_COUNT / (EXPER_COUNT - ONE_DECIMAL)) * dispersion).sqrt()
    temp = CONF_INTR_MEANVALUE*((dispersion / EXPER_COUNT).sqrt())
    trustMeanInterval: mi = mi(selectiveAvg - temp, selectiveAvg + temp, quantize_val='1.0000', delimeter='-')
    trustAvgQuadInterval: mi = mi(unclattEvaul / (ONE_DECIMAL + DEC_Q_VALUE), unclattEvaul /  (ONE_DECIMAL - DEC_Q_VALUE), quantize_val ='1.0000', delimeter='-')
    result['u_i'] = result['deviation'].apply(lambda deviation: deviation/trustAvgQuadInterval.calculate_mean())
    result['laplass'] = result['u_i'].apply(lambda u_i: lp(u_i))
    EQUAL_FREQ_AMPLIFYER: Decimal = (EXPER_COUNT*STEP)/trustAvgQuadInterval.calculate_mean()
    result['equalFreq'] = result['laplass'].apply(lambda laplass: laplass * EQUAL_FREQ_AMPLIFYER)
    result['roundedEqualFreq'] = result['equalFreq'].apply(lambda equlFreq: equlFreq.quantize(Decimal('1')))
    freq_sum: Decimal = result['roundedEqualFreq'].sum()
    rejection: int = int(EXPER_COUNT - freq_sum)
    if(rejection != 0):
        num_elements = len(result)
        base_value = rejection // num_elements
        remainder = rejection % num_elements

        result['roundedEqualFreq'] = result['roundedEqualFreq'] + base_value
        result.loc[:remainder, 'roundedEqualFreq'] += 1

    result['freq^*'] = result['roundedEqualFreq'].apply(lambda roundedEqualFreq: roundedEqualFreq/EXPER_COUNT)

    print ('среднее выборочное: ' + str(selectiveAvg.quantize(Decimal("1.0000"))))
    print('дисперсия: ' + str(dispersion.quantize(Decimal("1.0000"))))
    print('Среднеквадратическое отклонение: ' + str((dispersion.sqrt()).quantize(Decimal("1.0000"))))
    print('s: ' + str(unclattEvaul.quantize(Decimal("1.0000"))))
    print('интервал матожидания: ')
    print(trustMeanInterval)
    print('интервал среднего квадратического')
    print(trustAvgQuadInterval)

    return result, unclattEvaul, selectiveAvg

def makeCritRealFrame(equalFreqFrame: pd.DataFrame, unclattValue: Decimal, accidentsSelectiveAvg: Decimal)  -> pd.DataFrame:
    intervals: list[str] = [f"-inf ÷ {equalFreqFrame.iloc[0,0]}"]
    freq: list[int] = [0]
    laplass: list[Decimal] = [Decimal('-0.500')]
    ditribution: list[Decimal] = [Decimal('0')]

    for i in range(0):
        intervals.append(f"{equalFreqFrame.iloc[i,0]} ÷ {equalFreqFrame.iloc[i+1,0]}")
        z_i: Decimal = (equalFreqFrame.iloc[0,0] - accidentsSelectiveAvg)/unclattValue
        
        freq.append(equalFreqFrame['r'].str[i])
        laplass.append()


    result: pd.DataFrame = pd.DataFrame({'intervals': intervals, 'freq' : freq, 'laplass': laplass})

    return result