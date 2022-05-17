# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

w = {
    "A": {
        "f": 3,
        "w": 6,
        'a': 6000
    },
    "B": {
        'f': 1, 'w': 1, 'a': 2000
    }
}

target = 10000
typeof = 'a'
obj = 'A'
sec = 'B'

maxF = {'A': 0, 'B': 0, 'f': 0 }

for i in range(6001):
    for j in range(2001):
        amountA = w[obj]['w'] * i
        amountB = w[sec]['w'] * j
        amount = amountA + amountB;
        if (amount < target):
            continue

        # calc food
        remain = w[obj]['a'] - i
        foodA = (w[obj]['f'] * remain)
        remainB = (w[sec]['a'] - j)
        brate = w[sec]['f']
        foodB =  brate * remainB
        food = foodA + foodB
        if (maxF['f'] < food and food >= 14999):
            maxF['A'] = i
            maxF["remainA"] = remain
            maxF["B"] = j
            maxF["f"] = food
            
            
print(maxF)
print(maxF)
print(maxF)
print(maxF)

