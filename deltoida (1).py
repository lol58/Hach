#Дельтоида, рабочаяя на простых полиномах, степени, меньшей 7
from numpy import exp
from vector import VectorModel
from reader import reader

INPUTSIZE = 7

def deltoida(history, size, count=1, start_func=lambda x: 0, returnModel=False, rad=100, epochs=100):
    def macro(data):
        for deep in range(len(data)-1):
            newData = []
            for i in range(len(data)-1):
                newData.append(data[i+1] - data[i])
            data = newData
        return data[0]
    
    def bias(data):
        result = 0
        for deep in range(len(data)-1):
            result += data[-1]
            newData = []
            for i in range(len(data)-1):
                newData.append(data[i+1] - data[i])
            data = newData
        return result
    
    def predict(macroList, need=1, his=[]):
        def normolaiz(x):
            #x = (x*10)**3
            #return (100 / (1 + exp(x)))
            #return 200*(1 / (1 + exp(-x)))
            return 1000 / (1 + (-x*100))
        points = [(normolaiz(macroList[i]), macroList[i+1]*100)
                  for i in range(len(macroList)-1)]
        model = VectorModel(start_func, radonus=rad)
        model.train(points, epochs=epochs, show=False)
        h = his
        for i in range(need):
            mac = model.run(normolaiz(macroList[-1]))/100
            macroList.append(mac)
            pred = mac + bias(h[-size:])
            h.append(pred)
        if not returnModel:
            return h[-need:]
        else:
            return (h[-need:], model)
    macroList = []
    for start in range(len(history)-size-1):
        macroList.append(macro(history[start:start+size]))
    return predict(macroList, count, history)

#his = [x**2 for x in range(-9, 9)]
#print(deltoida(his, INPUTSIZE, 4))


'''
#his = [0, 0.06738449877975927, 0.11973256903797377, 0.17120358248353323, 0.06990200119998032, 0.14462331981045265, 0.19041764624563332, 0.23154228874976984, 0.12416126008331825, 0.20301406729285223, 0.24831320412368477, 0.3064677916508576, 0.19460734021806633, 0.28073878846858946, 0.3270384996960372, 0.3915481658227941, 0.272210658527218, 0.3634048656868735, 0.40560161532475564, 0.479425285821609, 0.35999494358313394, 0.4394530209227005, 0.4677452049916235, 0.4661177685504278, 0.263462328216347, 0.32121660325488366, 0.377615099667935, 0.43990295177759187, 0.3033600628161309, 0.37000624356803147, 0.4151628409089891, 0.48944897907559054, 0.3355734560078834, 0.40241543761880194, 0.4645391518528984, 0.5397609150690195][:-1]
#his = [(2**x) / (x**2) for x in range(1, 20)]
#his = reader('data/Test_example1.xlsx')[]
#his.append(deltoida(his, INPUTSIZE)) #, max(7, int(len(his)/4))))
#print(his[-3:])
#his = reader('data/Test_example1.xlsx')['Quarterly'][1][:4]
#print(deltoida(his, 7))
'''
