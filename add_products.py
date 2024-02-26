# alekya

import os 

def adding_products():

    def validate_price(price):
        # Check if price is a valid float value
        try:
            float(price)
            return True
        except ValueError:
            return False

    def Products_csv():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "data")

        enquiries = open(filename+"\\products.csv","r")

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

        name = input("Enter product name: ")

        while True:
            price = input("Enter product price: ")
            if validate_price(price):
                break
            else:
                print("Invalid price. Please enter a valid number.")

        description = input("Enter product description: ")

        with open(filename+"\\products.csv", "a") as products:
            products.write(f"{int(dataList[-1][0]) + 1},{name},{price},{description}\n")

        # Print the content of the CSV file after writing
        print("Product added ✔")
        # with open(filename+"\\products.csv", "r") as products:
        #     for line in products:
        #         print(line.strip())  # Strip newline character for cleaner output
    Products_csv()