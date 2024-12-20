import lib.data_processing as dp
import lib.plots_draw as plt
import lib.correalation as corr
import pandas as pd
from decimal import *
from parsing_module import parse_fallout

url = 'http://www.pogodaiklimat.ru/history/26063_2.htm'
accidentsString = """467 478 568 346 486 557 395 543 621 594 467 534 345 587 387 421 376 654 634 485 470 428 382 490 502 411 520 495 385 602 463 428 527 483 621 544 490 567 573 556 634 674 753 346 663 587 597 532 486 464 582 480 575 456 437 534 634 642 534 563 516 500 528 608 603 616 624 691 615 601 641 700 453 378 443 478 579 539 519 565 572 580 476 522 485 436 457 436 505 547 544 554 583 651 569 544 489 433 436 432 620 551 557 587 622 610 570 566 423 383 517 513 577 566 575 617 614 607 564 678 507 509 431 213 299 405 416 526 547 491 437 424 376 348 384 401 406 443 458 445 459 522 439 325 268 236 326 327 337 441 324 403 403 393 409 294"""

EXPER_COUNT = 156
accidents = [int(x) for x in accidentsString.split(' ')]
fallout = parse_fallout(url)

accidentsFrame: pd.DataFrame = dp.makeFrame(accidents, 'accidents')
falloutFrame: pd.DataFrame = dp.makeFrame(fallout, 'fallout')

correlationFrame: pd.DataFrame = dp.makeCorrelationFrame(falloutFrame, accidentsFrame)
rankedCorrelationFrame: pd.DataFrame = corr.makeRankFrame(correlationFrame)
rankedValue: Decimal = corr.correlationValue(rankedCorrelationFrame, EXPER_COUNT)
falloutRangedFrame: pd.DataFrame = dp.makeCorrelationFrame(falloutFrame, accidentsFrame, sortValue='fallout')
accidentsRangedFrame: pd.DataFrame = dp.makeCorrelationFrame(falloutFrame, accidentsFrame, sortValue='accidents')
print(rankedValue)
accidentsDiscretFrame: pd.DataFrame = dp.makeDiscretFrame(accidentsFrame)
accidentsIntervalFrame: pd.DataFrame = dp.makeIntervalFrame(accidentsDiscretFrame, 36, 156)
accidentsEmpiricFunc: pd.DataFrame = dp.makeEmpiricFuncFrame(accidentsIntervalFrame)
accidentsDiscretVariaricFrame: pd.DataFrame = dp.makeDiscretVariaticFrame(accidentsIntervalFrame)
accidentsUnclatt: Decimal
accidentsEqualFrame: pd.DataFrame
accidentsEqualFrame, accidentsUnclatt, accidentsSelectiveAvg = dp.makeEqualFreq(accidentsDiscretVariaricFrame, accidentsIntervalFrame, 156, 0.115)
accidentsCritRealFrame: pd.DataFrame = dp.makeCritRealFrame(accidentsEqualFrame, accidentsDiscretFrame, accidentsUnclatt, accidentsSelectiveAvg, 156)


falloutDiscretFrame: pd.DataFrame = dp.makeDiscretFrame(falloutFrame)
correlationMatrix: pd.DataFrame = corr.makeCrossMatrix(correlationFrame, falloutDiscretFrame, accidentsDiscretFrame)
falloutIntervalFrame: pd.DataFrame = dp.makeIntervalFrame(falloutDiscretFrame, 26, 156)
falloutEmpiricFunc: pd.DataFrame = dp.makeEmpiricFuncFrame(falloutIntervalFrame)
falloutDiscretVariaricFrame: pd.DataFrame = dp.makeDiscretVariaticFrame(falloutIntervalFrame)
falloutUnclatt: Decimal
falloutEqualFrame: pd.DataFrame
falloutEqualFrame, falloutUnclatt, falloutSelectiveAvg = dp.makeEqualFreq(falloutDiscretVariaricFrame, falloutIntervalFrame, 156, 0.115)

falloutCritRealFrame: pd.DataFrame = dp.makeCritRealFrame(falloutEqualFrame, falloutDiscretFrame, falloutUnclatt, falloutSelectiveAvg, 156)

correlationFrame.to_csv('output/correlationFrame.csv')
falloutRangedFrame.to_csv('output/falloutRangedFrame.csv')
accidentsRangedFrame.to_csv('output/accidentsRangedFrame.csv')
correlationMatrix.to_csv('output/correlationMatrix.csv')
rankedCorrelationFrame.to_csv('output/rankedCorrelationFrame.csv')



accidentsDiscretFrame.to_csv('output/accidentsDiscretFrame.csv')
accidentsIntervalFrame.to_csv('output/accidentsIntervalFrame.csv')
accidentsEmpiricFunc.to_csv('output/accidentsEmpiricFunc.csv')
accidentsDiscretVariaricFrame.to_csv('output/accidentsDiscretVariaricFrame.csv')
accidentsEqualFrame.to_csv('output/accidentsEqualFrame.csv')
accidentsCritRealFrame.to_csv('output/accidentsCritRealFrame.csv')
                              
falloutDiscretFrame.to_csv('output/falloutsDiscretFrame.csv')
falloutIntervalFrame.to_csv('output/falloutIntervalFrame.csv')
falloutEmpiricFunc.to_csv('output/falloutEmpiricFunc.csv')
falloutDiscretVariaricFrame.to_csv('output/falloutDiscretVariaricFrame.csv')
falloutEqualFrame.to_csv('output/falloutsEqualFrame.csv')
falloutCritRealFrame.to_csv('output/falloutCritRealFrame.csv')

plt.drawScatterDots(correlationFrame, 'output/scatterDots.png')

plt.drawEmpiricPlot(accidentsEmpiricFunc, accidentsDiscretVariaricFrame, 'output/accidentsEmpiricFunc.png', 'Accidents')
plt.drawHist(accidentsIntervalFrame, accidentsDiscretVariaricFrame, 'output/accidentsDiscretVariaricFrame.png', 'Intervals')
plt.drawEqualFreqPlot(accidentsEqualFrame, accidentsDiscretVariaricFrame, 'output/accidentsEqualFrame.png', 'Accidents')

plt.drawEmpiricPlot(falloutEmpiricFunc, falloutDiscretVariaricFrame, 'output/falloutEmpiricFunc.png', 'Fallout')
plt.drawHist(falloutIntervalFrame, falloutDiscretVariaricFrame, 'output/falloutDiscretVariaricFrame.png', 'Intervals')
plt.drawEqualFreqPlot(falloutEqualFrame, falloutDiscretVariaricFrame, 'output/falloutEqualFrame.png', 'Fallout')


