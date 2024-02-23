# main script

import add_enquiry
import add_products
import add_source
import delete_enquiry
import view_enquiry

while True:
    print('''       ~~~ Menu ~~~
    1. Add a product
    2. Add a source
    3. Add an enquiry
    4. View enquiry
    5. Delete enquiry
    6. Exit the program''')
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("1. Add a product")
        add_products
        print("The product has been successfully added!!")

    elif choice==2:
        print("2. Add a source")
        add_source
        print("The source has been successfully added!!")

    elif choice==3:
        print("3. Add an enquiry")
        add_enquiry
        print("The enquiry has been successfully added!!")

    elif choice==4:
        print("4. View enquiry")
        print("Enquiry Details:")
        view_enquiry

    elif choice==5:
        print("5. Delete enquiry")
        delete_enquiry
        print("Successfully deleted the enquiry!!")

    elif choice==6:
        print("6. Exit")
        print("Exiting the Menu....")
        break
    else:
        print("Invalid input! Try again!!")

print("Thank you for choosing us, please visit again 😄")