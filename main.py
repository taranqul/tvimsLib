import lib.data_processing as dp
import pandas as pd
accidentsString = """467 478 568 346 486 557 395 543 621 594 467 534 345 587 387 421 376 654 634 485 470 428 382 490 502 411 520 495 385 602 463 428 527 483 621 544 490 567 573 556 634 674 753 346 663 587 597 532 486 464 582 480 575 456 437 534 634 642 534 563 516 500 528 608 603 616 624 691 615 601 641 700 453 378 443 478 579 539 519 565 572 580 476 522 485 436 457 436 505 547 544 554 583 651 569 544 489 433 436 432 620 551 557 587 622 610 570 566 423 383 517 513 577 566 575 617 614 607 564 678 507 509 431 213 299 405 416 526 547 491 437 424 376 348 384 401 406 443 458 445 459 522 439 325 268 236 326 327 337 441 324 403 403 393 409 294"""
accidents = [int(x) for x in accidentsString.split(' ')]

accidentsFrame: pd.DataFrame = dp.makeFrame(accidents, 'accidents')
accidentsDiscretFrame: pd.DataFrame = dp.makeDiscretFrame(accidentsFrame)
accidentsIntervalFrame: pd.DataFrame = dp.makeIntervalFrame(accidentsDiscretFrame, 54, 156)
accidentsEmpiricFunc: pd.DataFrame = dp.makeEmpiricFuncFrame(accidentsIntervalFrame)
accidentsDiscretVariaricFrame: pd.DataFrame = dp.makeDiscretVariaticFrame(accidentsIntervalFrame)
acvidentsEqualFrame: pd.DataFrame = dp.makeEqualFreq(accidentsDiscretVariaricFrame, accidentsIntervalFrame, 156)
print(acvidentsEqualFrame)
