import os
import random
import time

print('High Score Table\n\n')

while True:
  f = open('high.score.txt', 'a+')

  user_data = input(
      'enter your Initials then a tab High sore ---> ').strip().upper().split()
  f.write('\n')
  for i in user_data:
    X = (f'{i}')
    f.write(f'{X} ')

  f.close()
  print('\033[32m', 'added successfully the the high score record file',
        '\033[0m')

  decision = input(
      '\n\nare you done with high score data entry? -- (yes or no)').strip(
      ).lower()
  if decision == 'no':
    print("\nlet's get you another entry done!!")
    print('\nclearing....')
    time.sleep(2)
    os.system('clear')
    print('High Score Table\n\n')
    continue
  else:
    print('bye🥺')
    break
