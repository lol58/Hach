from reader import reader, write
from deltoida import deltoida

INPUTSIZE = 5

def wieght(aPred, aReal):
    return 

def selfPrediction(a):
    return deltoida(a, INPUTSIZE)[0]

def reduction(a, b):
    r = []
    for i in range(len(a)-1):
        r.append(a[i+1]-b[i])
    rPred = deltoida(r, INPUTSIZE)[0]
    aPred = b[len(a)-1] + rPred
    return aPred

def getWeigths(data):
    for sheet in list(data.keys()):
        info = data[sheet]
        del info[0]
        wieghts = [[None for i in range(len(info))] for j in range(len(info))]
        for i in range(len(info)-1):
            for j in range(i+1, len(info)):
                aIndex = i
                bIndex = j
                a = info[i]
                b = info[j]
                if len(a) > len(b):
                    aIndex, bIndex = bIndex, aIndex
                    a, b = b, a
                aPred = reduction(a[:-1], b)
                aReal = a[-1]
                wieghts[aIndex][bIndex] = weigth(aPred, aReal)

def genshinImpact(fileName, outputFileName):
    data = reader(fileName)
    newdata = {}
    for sheet in list(data.keys()):
        f = lambda x: 0
        epochs = 10
        rad = 1000
        newdata[sheet] = [data[sheet][0], [data[sheet][1][0]]]
        info = data[sheet][1]
        for i in range(1, len(info)):
            if 'Forecast' in info[i]:
                inx = info[i].index('Forecast')-1
                need = len(info[i])-inx
                info[i] = info[i][:inx]
                res, mod = deltoida(info[i], size=INPUTSIZE, count=need,
                                    start_func=f, returnModel=True,
                                    epochs=epochs, rad=rad)
                newdata[sheet][1].append(info[i])
                epochs = 10
                rad = 200
                mod.vectors = mod.vectors[:100] 
                f = mod.run
    write(newdata, outputFileName)
for i in range(1, 4446+1):
    genshinImpact('input/Test_input_{i}.xlsx', 'output/Test_output_{i}.xlsx')
