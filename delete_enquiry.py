# shruti
import os

def delete_data_by_eq_no(X,dataList):
    found = False
    for i in range(len(dataList)):
        if dataList[i][0] == X:
            del dataList[i]
            found = True
            break

    if not found:
        print("Data Not found")
        return

    mainList = []
    for i in range(len(dataList)):
        x = ','
        z = x.join(dataList[i])
        mainList.append(z)
        
    return '\n'.join(mainList)

def deleting_enquiry():

    # Read CSV data
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "data//enquiry.csv")
    with open(filename, "r") as enquiries:
        data = enquiries.readlines()

    headers = data[0]
    # print(headers)
    # Remove column names
    del data[0]

    # Convert data to list of lists
    dataList = [line.strip().split(",") for line in data]

    print("Available eq:\n")
    print(headers.replace(',',"|"),end="")

    for data in dataList:
        for col in data:
            print(f"{col}|",end="")
        print()
    # User input for eq_no
    X = input('\nEnter the eq_no: ')

    # Call function to delete data
    result = delete_data_by_eq_no(X,dataList)
    if(not result):
        return
    overwrite = headers + result
    print(overwrite+"\n")

    overwrite_file = open(filename, "w")
    overwrite_file.write(overwrite+"\n")
    overwrite_file.flush()
    overwrite_file.close()
    print("Deleted successfully")