# shruti
import re
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,"data//enquiry.csv")
enquiries = open(filename,"r")
data = enquiries.readlines()
print(data)
'''def delete_data_by_eq_no (eq_no):
    if eq_no in data :'''
#deleting the first row of column names
del data[0]
enquiries.close()
dataList = []
for line in data:
    line = line.replace("\n","")
    res = line.split(",")
    dataList.append(res)
print(dataList)
X = input('Enter the eq_no') 
    #key=data[0]
key =0
for i in range(len(dataList)):
    print(dataList[i][0])
    if dataList[i][0] == X:
        key = i
    else:
        print("Data Not found")

del dataList[key]   
print(dataList) 

    


   
    
'''print (dataList)
for data in dataList :
    print(data)
   # data[0]
    print (data[0])'''