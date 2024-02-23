# shruti
import os

def deleting_enquiry():
    def delete_data_by_eq_no(X):
        found = False
        for i in range(len(dataList)):
            if dataList[i][0] == X:
                del dataList[i]
                found = True
                break

        if not found:
            print("Data Not found")

        mainList = []
        for i in range(len(dataList)):
            x = ', '
            z = x.join(dataList[i])
            mainList.append(z)

        return '\n'.join(mainList)

    # Read CSV data
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "data//enquiry.csv")
    with open(filename, "r") as enquiries:
        data = enquiries.readlines()

    # Remove column names
    del data[0]

    # Convert data to list of lists
    dataList = [line.strip().split(",") for line in data]

    # User input for eq_no
    X = input('Enter the eq_no: ')

    # Call function to delete data
    result = delete_data_by_eq_no(X)
    print(result)