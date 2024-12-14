import pandas as pd
from decimal import Decimal

def makeCrossMatrix(correlationFrame: pd.DataFrame, firstDiscretFrame: pd.DataFrame, secondDiscretFrame: pd.DataFrame) -> pd.DataFrame:

    result = pd.crosstab(correlationFrame.iloc[:, 0], correlationFrame.iloc[:, 1])

    result['count'] = firstDiscretFrame['count'].values

    count_row = pd.DataFrame([secondDiscretFrame['count'].values], columns=secondDiscretFrame.iloc[:, 0], index=['count'])

    result = pd.concat([result, count_row], axis=0)
    result.at['count', 'count'] = 0
    result = result.astype(int)
    
    return result

def makeRankFrame(correlationFrame: pd.DataFrame) -> pd.DataFrame:

    ranked_df: pd.DataFrame = correlationFrame.rank(method='average')

    ranked_df.columns = [f"Rank_{col}" for col in ranked_df.columns]

    result: pd.DataFrame = pd.concat([correlationFrame, ranked_df], axis=1)

    result['diff'] = result.iloc[:,-2] -  result.iloc[:,-1]

    result['diff quad'] = result['diff'] ** 2
    return result.sort_values(result.columns[0])

def correlationValue(rankedFrame: pd.DataFrame, experCount: int):
    diff_summ: Decimal = Decimal(rankedFrame['diff quad'].sum())
    print(diff_summ)
    result: Decimal = Decimal('1') - ((Decimal('6') * diff_summ)/(experCount*(experCount**2 - 1)))
    return result