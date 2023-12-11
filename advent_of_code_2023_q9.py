import numpy as np

f = open("input.txt", 'r')
out = f.read().split('\n')


def lagrange(x, x_values, y_values):
    def L(k):
        out = [(x - x_values[j]) / (x_values[k] - x_values[j])
               for j in range(len(x_values)) if j != k]
        return np.prod(out)

    return sum(y_values[k] * L(k) for k in range(len(x_values)))


total = 0
for line in out:
    vals = list(map(int, line.split()))
    next_val = lagrange(-1, list(range(len(vals))), vals)
    total += next_val
print(total)