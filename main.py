import itertools
import functools

identities = [
  {"name": "user"},
  {"name": "post"},
  {"name": "comment"},
  {"name": "friend"}
]
index = {}
import itertools



def number(grid):
  for item in range(0, len(grid)):
    grid[item]["number"] = item

def createindex(index, grid):
  for item in grid:
    index[item["name"]] = item

def multiply(item, item2):
  return item * item2
def add(item, item2):
  return item + item2

def docalculation(previous, current):
  print(current)
  return current[1][0](previous, current[0])

def findcombinations(identities, number, length):
  numbers = [identity["number"] for identity in identities]
  print(numbers)
  target = number
  formula = [multiply, add]
  calculations = list(itertools.product(formula))
  print(calculations)
  results = []

  chained = []
  for index in range(0, length):
    chained.append(itertools.permutations(numbers, index))
  
  print(chained)
  for seq in itertools.chain(chained):
      if functools.reduce(docalculation, zip(seq, calculations), 0) == target:
            results.add(list(zip(seq, calculations)))
  
  return results



number(identities)
createindex(index, identities)
items = findcombinations(identities, 20, 4)
for item in items:
  print(list(item))
