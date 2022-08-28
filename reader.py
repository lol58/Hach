import pandas
def reader(fileName):
    result = {}
    for sheet in ['Quarterly', 'Monthly']:
        try:
            df = pandas.read_excel(fileName, sheet)
            columns = df.columns.values.tolist()
            columns[0] = ''
            df = df.T
            values = df.values.tolist()
            result[sheet] = [columns, values]
        except ValueError:
            continue
    return result
"""
def write(clova,filename):
    writer = pandas.ExcelWriter(filename, engine='xlsxwriter')
    for i in list(clova.keys()):
         pt = (list(clova[i]))
         df = pandas.DataFrame(pt)
         df.to_excel(writer, i, index=False, )
    writer.save()
"""

def write(clova,filename):
    writer = pandas.ExcelWriter(filename, engine='xlsxwriter')
    for i in list(clova.keys()):
         pt = clova[i][1]
         df = pandas.DataFrame(pt).T
         df.to_excel(writer, i, index=False)# header=None)#header=clova[i][0])
    writer.save()


#print(write(reader("data/Test_example1.xlsx"),f'data/Test_input_{1}.xlsx'))
#print(reader('data/Test_example1.xlsx'))
