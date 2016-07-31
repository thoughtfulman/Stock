import tushare as ts

def nFall(wk, n):
    closePrice = wk['close']
    length = len(closePrice)
    diffPrice = [None]*length
    for i in range(1,length):
        diffPrice[i] = closePrice[i]-closePrice[i-1] 
    list = diffPrice[1:]
    res = 0
    count = 0
    start = False
    for i in range(1,len(list)):
        if list[i] >= 0 and count == n: 
            res += 1 
            count = 0
            print("\n")
            print(wk[i-n-1:i+2])
        elif list[i] < 0 and list[i-1] >=0:
            start = True
            count = 1
        elif list[i] < 0  and count < n and start:
            count += 1
        else:
            count = 0
    return res

wk = ts.get_h_data('600332', start='2010-06-30', end='2016-07-30')
wk = wk[::-1]
fall3 = nFall(wk, 3)
fall4 = nFall(wk, 4)
fall5 = nFall(wk, 5)
fall6 = nFall(wk, 6)
fall7 = nFall(wk, 7)
fall8 = nFall(wk, 8)

print(fall3, fall4, fall5, fall6, fall7, fall8)

