import pandas as pd

def parse_fallout(url):
  dfs = pd.read_html(url)

  df = dfs[1]

  start_index = 271
  end_index = start_index + 13
  fallout_array = []
  for index in range(start_index, end_index):
      row = df.iloc[index]
      fallout_array.append(row[:12].values)
  fallout_array = [int(item) for sublist in fallout_array for item in sublist]
  
  
  #LEGACY, MAYBE USEFULL
  # fallout_array[fallout_array.index(min(fallout_array))] += 2
  

  # AT_27_36 = 4
  # AT_36_45 = 4
  # AT_45_54 = 4

  # AT_126_135 = 2
  # AT_81_90= 3

  # for i in range(len(fallout_array)) :

  #   if fallout_array[i] in range(18, 27):
      
  #     if AT_27_36 != 0:
  #       fallout_array[i] = random.randrange(28, 35)
  #       AT_27_36 -= 1
  #     elif AT_36_45 != 0:
  #       fallout_array[i] = random.randrange(37, 44)
  #       AT_36_45 -=1
  #     elif AT_45_54 != 0:
  #       fallout_array[i] = random.randrange(46, 53)
  #       AT_45_54 -= 1
  #   elif fallout_array[i] in range(90, 99):
  #     print('find ' + str(fallout_array[i]))

  #     if AT_126_135 != 0:
  #       AT_126_135 -= 1
  #       fallout_array[i] = random.randrange(127, 134)
  #     elif AT_81_90 != 0:
  #       AT_81_90 -= 1
  #       fallout_array[i] = random.randrange(82, 89)

  #     print('now ' + str(fallout_array[i]))

  return fallout_array

