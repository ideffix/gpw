import json
import numpy as np
import matplotlib.pyplot as plt


def normalize(arr):
    norm = np.linalg.norm(arr)
    return arr / norm


with open('result-1602942380101014.json', 'r') as fp:
    d = json.load(fp)
    maxArrLen = 0
    for key, value in d.items():
        maxArrLen = max(maxArrLen, len(value))

    d = dict(filter(lambda el: len(el[1]) == maxArrLen, d.items()))

    matrix = []
    names = []
    for key, value in d.items():
        arr = []
        for el in value:
            arr.append(el[1])
        d[key] = arr
        matrix.append(arr)
        names.append(key)

    k = 5
    cov = np.corrcoef(matrix)
    for i in range(k):
        minValue = np.amin(cov)
        minIndexes = np.argwhere(cov == np.min(cov))[0]
        print(f'{i + 1} min cov value: {minValue} for {names[minIndexes[0]]} and {names[minIndexes[1]]}')
        cov.itemset((minIndexes[0], minIndexes[1]), 1)
        cov.itemset((minIndexes[1], minIndexes[0]), 1)

        plt.plot(normalize(matrix[minIndexes[0]]), label=names[minIndexes[0]])
        plt.plot(normalize(matrix[minIndexes[1]]), label=names[minIndexes[1]])
        plt.legend()
        plt.show()


