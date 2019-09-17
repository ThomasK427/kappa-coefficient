# This is a python script for computing cohen's kappa.

import numpy as np

def cohen_kappa(a: np.int32, b: np.int32) -> float:
    assert a.shape == b.shape
    po = (a == b).astype(np.float32).mean()
    categories = sorted(set(list(np.concatenate((a, b), axis=0))))
    mp = {}
    for i, c in enumerate(categories):
        mp[c] = i
    k = len(mp)
    sa = np.zeros(shape=(k,), dtype=np.int32)
    sb = np.zeros(shape=(k,), dtype=np.int32)
    n = a.shape[0]
    for x, y in zip(list(a), list(b)):
        sa[mp[x]] += 1
        sb[mp[y]] += 1
    pe = 0
    for i in range(k):
        pe += (sa[i] / n) * (sb[i] / n)
    kappa = (po - pe) / (1.0 - pe)
    return kappa