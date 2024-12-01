import lib.data_processing as dp
list1 = [2, 3, 1, 5, 2, 1]
list2 = [4, 6, 5, 5, 5, 6]
print(dp.makeFrame(list1, 'accidents'))
print(dp.makeFrame(list2, 'snow'))
print(dp.makeCorrelationFrame(dp.makeFrame(list1, 'accidents'), dp.makeFrame(list2, 'snow')))
print(dp.makeDiscretFrame(dp.makeFrame(list1, 'accidents')))