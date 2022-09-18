#!/usr/bin/python3
def divisible_by_2(my_list=[]):
  mol = []
  for i in range(0, len(my_list)):
    if i % 2 == 0:
      mol.append(True)
    else:
      mol.append(False)
  return mol
    
