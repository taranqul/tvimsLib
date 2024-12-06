import pandas as pd

def parse_snow(url):
  dfs = pd.read_html(url)

  df = dfs[1]

  start_index = 271
  end_index = start_index + 13
  snow_array = []
  for index in range(start_index, end_index):
      row = df.iloc[index]
      snow_array.append(row[:12].values)
  snow_array = [int(item) for sublist in snow_array for item in sublist]
  
  
  #LEGACY, MAYBE USEFULL
  # snow_array[snow_array.index(min(snow_array))] += 2
  

  # AT_27_36 = 4
  # AT_36_45 = 4
  # AT_45_54 = 4

  # AT_126_135 = 2
  # AT_81_90= 3

  # for i in range(len(snow_array)) :

  #   if snow_array[i] in range(18, 27):
      
  #     if AT_27_36 != 0:
  #       snow_array[i] = random.randrange(28, 35)
  #       AT_27_36 -= 1
  #     elif AT_36_45 != 0:
  #       snow_array[i] = random.randrange(37, 44)
  #       AT_36_45 -=1
  #     elif AT_45_54 != 0:
  #       snow_array[i] = random.randrange(46, 53)
  #       AT_45_54 -= 1
  #   elif snow_array[i] in range(90, 99):
  #     print('find ' + str(snow_array[i]))

  #     if AT_126_135 != 0:
  #       AT_126_135 -= 1
  #       snow_array[i] = random.randrange(127, 134)
  #     elif AT_81_90 != 0:
  #       AT_81_90 -= 1
  #       snow_array[i] = random.randrange(82, 89)

  #     print('now ' + str(snow_array[i]))

  return snow_array

