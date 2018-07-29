import matplotlib.pyplot as plt
import sys
import os

arguments = sys.argv
print(arguments)

print('current script:', sys.argv[0])

if arguments[1] == '-d':
  print('analyze directory', arguments[1])
  path = arguments[2]
  try:
    os.chdir(path)
    print('path changed to:', path)
  except FileNotFoundError:
    print('bad path!')
    sys.exit()
else:
  print('bad argument!')



