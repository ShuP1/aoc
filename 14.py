import sys
import math
import itertools

mask = ['X'] * 36
mem = {}
for line in sys.stdin.readlines():
    (var, val) = line.rstrip().split(" = ")
    if var == 'mask':
        mask = val
    else:
        key = int(var[4:-1])
        value = int(val)
        """ #part 1
        for i, bit in enumerate(reversed(mask)):
          if bit == '0':
            value &= ~ (1 << i)
          elif bit == '1':
            value |= (1 << i)
        mem[key] = value
        """
        paths = []
        for i, bit in enumerate(reversed(mask)):
          if bit == '1':
            key |= (1 << i)
          elif bit == 'X':
            paths.append(i)

        def branch(key, paths):
          if paths:
            i = paths[0]
            branch(key & ~ (1 << i), paths[1:])
            branch(key | (1 << i), paths[1:])
          else:
            mem[key] = value
        branch(key, paths)

print(sum(mem.values()))