## file: testseqs.py

from mytools import timer

@timer(label='[CCC]==>')
def listcomp(N):                           # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]       # listcomp(...) triggers Timer.__call__

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return map((lambda x: x * 2), range(N))

for func in (listcomp, mapcall):
    print('')
    result = func(5)        # Time for this call, all calls, return value
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s' % func.alltime)   # Total time for all calls

print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))



