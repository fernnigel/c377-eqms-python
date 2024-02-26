# sejal

import os 

def adding_source():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "data")

    enquiries = open(filename+"\\sources.csv","r")

    data = enquiries.readlines()

    #deleting the first row of column names
    del data[0]

    enquiries.close()

    dataList = []

    for line in data:
        line = line.replace("\n","")
        res = line.split(",")
        dataList.append(res)

    # print(data)

    # print(f"Last index: {dataList[-1][0]}")

    type = input("Enter source type: ")

    with open(filename+"\\sources.csv", "a") as sources:
        sources.write(f"{int(dataList[-1][0]) + 1},{type}\n")

    # # Printing the content of the CSV file after writing
    # print("Data written to CSV file:")
    # with open(filename, "r") as sources:
    #     for line in sources:
    #         print(line.strip())