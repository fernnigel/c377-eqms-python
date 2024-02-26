# kartik
import re
import os 
dirname = os.path.dirname(__file__) 
filename = os.path.join(dirname, "data\\enquiry.csv" )

def enquiry_listing():
    enquiries = open(filename, "r")
    data = enquiries.readlines()
    enquiries.close()
    datalist = []
    for line in data:
        line = line.replace("\n"," ")
        res = line.split(",")
        datalist.append(res)

    while True:
        print("\n1. Print all enquires\n2. Print enquiry by id\n3.exit")
        choice = int(input("choice:"))
        if(choice == 1):
            for data in datalist:
                for col in data:
                    print(f"{col}|",end="")
                print()
        elif(choice == 2):
            id = int(input("Enter id:"))
            for i in range(1,len(datalist)):

                if(int(datalist[i][0]) == id):
                    for data in datalist[0]:
                        print(f"{data}|",end="")
                    print()
                    for data in datalist[i]:
                        print(f"{data}|",end="")
                    print()
                    break
            else:
                print("Not found")
        elif(choice == 3):
            break
        else:
            print("invalid choice")
        # print(datalist)