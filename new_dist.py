from dot import *

def D(A, B):
    return A != B

for A in random_dots():
  for B in random_dots():
      for C in random_dots():
          if not validator(D, A, B, C):
              print(False)
              exit(0)
print(True)
