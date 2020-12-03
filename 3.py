import sys

trees = sys.stdin.readlines()
mod = len(trees[0]) - 1 # trim space
def isTree(x, y):
  return trees[x][y % mod] == '#'

prd = 1
for (dx, dy) in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
  x = dx
  y = dy
  count = 0
  while x < len(trees):
    if isTree(x, y):
      count = count + 1
    x = x + dx
    y = y + dy
  prd = prd * count

print(prd)