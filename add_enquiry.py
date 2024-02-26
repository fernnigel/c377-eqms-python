# nigel

import re
import os 
dirname = os.path.dirname(__file__) 
filename = os.path.join(dirname,"data")

def not_null(input_str):
    if(input_str != ""):
        return True
    else:
        return False

def new_enquiry():

    enquiries = open(filename+"\\enquiry.csv","r")

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


    """
    Taking input
    """

    while True:
        eq_date = input('enter date(yyyy-mm-dd): ')
        if(re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$",eq_date)):
            break
        else:
            print("wrong format")

    while True:
        name = input('Enter customer name: ')
        if(re.match("^[^ ][a-zA-Z ]+$",name)):
            break
        else:
            print("name cannot be null")

    while True:
        contact_person = input('Enter name of contact_person: ')
        if(re.match("^[^ ][a-zA-Z ]+$",contact_person)):
            break
        else:
            print("contact_person cannot be null")

    while True:
        address = input('Enter customer address: ')
        if(not_null(address)):
            break
        else:
            print("address cannot be null")

    while True:
        phone = input('Enter phone:')
        if(re.match("^[0-9]{10}$",phone)):
            break
        else:
            print("wrong format")
    
    while True:
        email = input('Enter email:')
        if(re.match("^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$",email)):
            break
        else:
            print("wrong format")

    """
    Source logic
    """

    source = open(filename+"\\sources.csv","r")
    source_data = source.readlines()
    source.close()

    source_ids = {}

    print('------Select Source id---------')

    for line in source_data:
        line = line.replace("\n","")
        res = line.split(",")
        print(f"{res[0]}\t{res[1]}")
        source_ids[res[0]] = res[1]

    while True:
        source = input('Enter source id:')
        if(source in source_ids.keys()):
            sourceType = source_ids[source]
            break
        else:
            print("No such id")

    print(sourceType)

    remarks = input('Enter remarks:')

    if(remarks==""):
        remarks = "NA"
    
    """
    Product logic
    """

    products = open(filename+"\\products.csv","r")
    product_data = products.readlines()
    products.close()

    product_ids = {}

    print('------Select product id---------')

    for line in product_data:
        line = line.replace("\n","")
        res = line.split(",")
        print(f"{res[0]}\t{res[1]}")
        product_ids[res[0]] = res[1]

    while True:
        product = input('Enter product id:')
        if(product in product_ids.keys()):

            productType = product_ids[product]

            break
        else:
            print("No such id")

    print(productType)
    # product_id = input('Enter product_id')
    # product_name = input('Enter ')
    quantity = int(input('Enter Quantity:'))
    price = float(input('Enter price:'))
    total = int(quantity) * float(price)

    final_add = f"{int(dataList[-1][0]) + 1},{eq_date},{name},{contact_person},{address},{phone},{email},{sourceType},{remarks},{product},{productType},{quantity},{price},{total}\n"
    print(final_add)

    enquiries = open(filename+"\\enquiry.csv","a")

    enquiries.write(final_add)

    enquiries.flush()

    enquiries.close()
new_enquiry()