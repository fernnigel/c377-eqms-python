# nigel
import re
import os 
dirname = os.path.dirname(__file__) 
filename = os.path.join(dirname,"data")

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

    print(f"Last index: {dataList[-1][0]}")


    """
    Taking input
    """

    eq_date = input('enter date(yyyy-mm-dd): ')
    while True:
        if(re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$",eq_date)):
            break
        else:
            print("wrong format")


    name = input('Enter name: ')
    contact_person = input('Enter contact_person: ')
    address = input('Enter address:')
    phone = input('Enter phone:')
    email = input('Enter email:')
    """
    Source logic
    """

    source = open(filename+"\\source.csv","r")
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
    quantity = input('Enter Quantity:')
    price = input('Enter price:')
    total = int(quantity) * float(price)

    final_add = f"{int(dataList[-1][0]) + 1},{eq_date},{name},{contact_person},{address},{phone},{email},{sourceType},{remarks},{product},{productType},{quantity},{price},{total}\n"
    print(final_add)

    enquiries = open(filename+"\\enquiry.csv","a")

    enquiries.write(final_add)

    enquiries.flush()

    enquiries.close()