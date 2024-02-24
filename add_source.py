# sejal

import os 

def adding_source():
    def validate_id(id):
        # Checking if id is a positive integer
        return id.isdigit() and int(id) >= 1

    def source_csv():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "data\\sources.csv")

        while True:
            id = input("Enter source id (positive integer): ")
            if validate_id(id):
                break
            else:
                print("Invalid id. Please enter a positive integer.")

        type = input("Enter source type: ")

        with open(filename, "a") as sources:
            sources.write(f"{id},{type}\n")

        # Printing the content of the CSV file after writing
        print("Data written to CSV file:")
        with open(filename, "r") as sources:
            for line in sources:
                print(line.strip())  
    source_csv()