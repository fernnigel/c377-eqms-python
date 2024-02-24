# alekya

import os 

def adding_products():
    def validate_code(code):
        # Check if code is a 3-digit number and starts with "001", "002", "003", etc.
        return code.isdigit() and len(code) == 3 and int(code) >= 1

    def validate_price(price):
        # Check if price is a valid float value
        try:
            float(price)
            return True
        except ValueError:
            return False

    def Products_csv():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "data\\products.csv")

        while True:
            code = input("Enter product code (3 digits starting from 001): ")
            if validate_code(code):
                break
            else:
                print("Invalid code. Please enter a 3-digit number starting from 001.")

        name = input("Enter product name: ")

        while True:
            price = input("Enter product price: ")
            if validate_price(price):
                break
            else:
                print("Invalid price. Please enter a valid number.")

        description = input("Enter product description: ")

        with open(filename, "a") as products:
            products.write(f"{code},{name},{price},{description}\n")

        # Print the content of the CSV file after writing
        print("Data written to CSV file:")
        with open(filename, "r") as products:
            for line in products:
                print(line.strip())  # Strip newline character for cleaner output
    Products_csv()