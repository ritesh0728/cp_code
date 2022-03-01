#CONCANATE TWO NUMBERS

def countPairs(N, X, numbers):
    # code here
    d = {}
    for i in numbers:
        d[str(i)] = d.get(str(i), 0) + 1
    x = str(X)
    l = x[0]
    r = x[1:];
    ans = 0
    while len(r) > 0:
        if l in d and r in d:
            if l == r:
                ans += (d[l] * d[r]) - d[l]
            else:
                ans += (d[l] * d[r])
        l += r[0]
        r = r[1:]
    return ans;
N = 4
numbers = [1, 212, 12, 12]
X = 1212
print(countPairs(N,X,numbers))