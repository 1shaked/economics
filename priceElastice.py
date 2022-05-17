
def changePrecantage(x , y):
    return abs(x - y) / x

prices = {}
for i in range(1,10):
    q = 50 - 5 * i
    next_q = q - 5
    elastic = changePrecantage(q, next_q) / changePrecantage(i,i+1)
    prices[i] = {'elastic': elastic, 'q': q}
print(prices)
