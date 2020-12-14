with open('input.txt') as f:
	lines = f.read().splitlines()


def getBus(lines):
    buses = []
    for bus in lines[1].split(","):
        if bus != "x":
            buses.append(int(bus))
            
    def getDepart(bus, minute):
        return minute % bus == 0
        

    timepoint = int(lines[0])
    busNotFound = True
    while busNotFound:
        for bus in buses:
            if getDepart(bus, timepoint):
                print("Bus ", bus, " at Minute ", timepoint)
                wait = timepoint - int(lines[0])
                print("Output: ", wait * bus)
                busNotFound = False
        timepoint += 1
    return wait * bus
    
print(getBus(lines))
    
from functools import reduce

def calcTime(lines):
    offBuses = []
    buses = []
    for i, bus in enumerate(lines[1].split(",")):
        if bus != "x":
            offBuses.append(int(bus) - i)
            buses.append(int(bus))

    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a*b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
    res = int(chinese_remainder(buses, offBuses))
    print(res)
    return res

print(calcTime(lines))