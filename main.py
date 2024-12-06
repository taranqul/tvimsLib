import lib.data_processing as dp
import pandas as pd
from parsing_module import parse_snow
import matplotlib.pyplot as plt
url = 'http://www.pogodaiklimat.ru/history/26063_2.htm'
accidentsString = """467 478 568 346 486 557 395 543 621 594 467 534 345 587 387 421 376 654 634 485 470 428 382 490 502 411 520 495 385 602 463 428 527 483 621 544 490 567 573 556 634 674 753 346 663 587 597 532 486 464 582 480 575 456 437 534 634 642 534 563 516 500 528 608 603 616 624 691 615 601 641 700 453 378 443 478 579 539 519 565 572 580 476 522 485 436 457 436 505 547 544 554 583 651 569 544 489 433 436 432 620 551 557 587 622 610 570 566 423 383 517 513 577 566 575 617 614 607 564 678 507 509 431 213 299 405 416 526 547 491 437 424 376 348 384 401 406 443 458 445 459 522 439 325 268 236 326 327 337 441 324 403 403 393 409 294"""

accidents = [int(x) for x in accidentsString.split(' ')]
snow = parse_snow(url)

accidentsFrame: pd.DataFrame = dp.makeFrame(accidents, 'accidents')
snowFrame: pd.DataFrame = dp.makeFrame(snow, 'snow')

correlationFrame: pd.DataFrame = dp.makeCorrelationFrame(snowFrame, accidentsFrame)
snowRangedFrame: pd.DataFrame = dp.makeCorrelationFrame(snowFrame, accidentsFrame, sortValue='snow')
accidentsRangedFrame: pd.DataFrame = dp.makeCorrelationFrame(snowFrame, accidentsFrame, sortValue='accidents')

accidentsDiscretFrame: pd.DataFrame = dp.makeDiscretFrame(accidentsFrame)
accidentsIntervalFrame: pd.DataFrame = dp.makeIntervalFrame(accidentsDiscretFrame, 54, 156)
accidentsEmpiricFunc: pd.DataFrame = dp.makeEmpiricFuncFrame(accidentsIntervalFrame)
accidentsDiscretVariaricFrame: pd.DataFrame = dp.makeDiscretVariaticFrame(accidentsIntervalFrame)
acvidentsEqualFrame: pd.DataFrame = dp.makeEqualFreq(accidentsDiscretVariaricFrame, accidentsIntervalFrame, 156, 0.115)

snowDiscretFrame: pd.DataFrame = dp.makeDiscretFrame(snowFrame)
snowIntervalFrame: pd.DataFrame = dp.makeIntervalFrame(snowDiscretFrame, 26, 156)
snowEmpiricFunc: pd.DataFrame = dp.makeEmpiricFuncFrame(snowIntervalFrame)
snowDiscretVariaricFrame: pd.DataFrame = dp.makeDiscretVariaticFrame(snowIntervalFrame)
snowEqualFrame: pd.DataFrame = dp.makeEqualFreq(snowDiscretVariaricFrame, snowIntervalFrame, 156, 0.115)

correlationFrame.to_csv('output/correlationFrame.csv')
snowRangedFrame.to_csv('output/snowRangedFrame.csv')
accidentsRangedFrame.to_csv('output/accidentsRangedFrame.csv')

accidentsDiscretFrame.to_csv('output/accidentsDiscretFrame.csv')
accidentsIntervalFrame.to_csv('output/accidentsIntervalFrame.csv')
accidentsEmpiricFunc.to_csv('output/accidentsEmpiricFunc.csv')
accidentsDiscretVariaricFrame.to_csv('output/accidentsDiscretVariaricFrame.csv')
acvidentsEqualFrame.to_csv('output/accidentsEqualFrame.csv')

snowDiscretFrame.to_csv('output/snowsDiscretFrame.csv')
snowIntervalFrame.to_csv('output/snowIntervalFrame.csv')
snowEmpiricFunc.to_csv('output/snowEmpiricFunc.csv')
snowDiscretVariaricFrame.to_csv('output/snowDiscretVariaricFrame.csv')
snowEqualFrame.to_csv('output/snowsEqualFrame.csv')

