import pandas as pd
import matplotlib.pyplot as plt
from lib.custom_types.my_fraction import MyFraction as mf
from lib.custom_types.my_intervals import MyIntervals as mi

def drawEmpiricPlot(empiricFrame: pd.DataFrame, discretVarFrame: pd.DataFrame,  path: str, messure: str):
    plt.plot(discretVarFrame['mean'], empiricFrame['empiric'].apply(lambda fraction: fraction.value()), color='blue', marker='o')
    plt.xlabel(messure)
    plt.ylabel('F*(x)')
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()

def drawHist(intervalFrame: pd.DataFrame, discretVarFrame: pd.DataFrame, path: str, messure: str):
    plt.bar(discretVarFrame.index, discretVarFrame['density'])
    plt.xlabel(messure)
    plt.xticks(discretVarFrame.index, intervalFrame['intervals'], rotation=90)
    plt.ylabel('ni/(hN)')
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()

def drawEqualFreqPlot(equalFreqFrame: pd.DataFrame, discretVarFrame: pd.DataFrame, path: str, messure: str):
    plt.plot(discretVarFrame['mean'], equalFreqFrame['freq^*'], label='Теоретические частоты', color='red', marker='o')
    plt.plot(discretVarFrame['mean'], discretVarFrame['relatFreq'], label='Эмпирические частоты', color='blue', marker='o')
    plt.xlabel(messure)
    plt.ylabel('P*')
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()

def drawScatterDots(correlationFrame: pd.DataFrame, path: str):
    plt.scatter(correlationFrame[correlationFrame.columns[1]], correlationFrame[correlationFrame.columns[0]], color='blue', label='Экспериментальные точки')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Экспериментальных точки')
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
