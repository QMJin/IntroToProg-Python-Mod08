# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# QimingJin,11.24.2019,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
list_of_product_objects = []
strChoice = ""

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        QimingJin,11.25.2019,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class
    def AddData(lstRow):
        lstRow=[productname, productprice]
        list_of_product_objects.append(lstRow)  # Add the new row to the list/table
        print("Data is added!")
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        QimingJin,11.25.2019,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    def read_data_to_file(file_name, list_of_rows):
        file = open(file_name, "r")
        for line in file:
                data = line.split(",")
                line = [data[0],data[1]]
                list_of_rows.append(line)
        file.close()
        return list_of_rows

    # TODO: Add Code to process data to a file
    def save_data_from_file(file_name, list_of_product_objects):
        file = open(file_name, "w")
        for row in list_of_product_objects:  # Write each row of data to the file
            file.write(str(row[0])+','+ str(row[1])+'\n')
        file.close()
        print("Data was saved!")

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    def add_docstring(classname):
      print(classname.__doc__)

    # TODO: Add code to show menu to user
    def show_menu():
        print('''
          Menu of Options
          1) Show current data in the list of product objects
          2) Add add to the list of product objects
          3) Save current data to file and exit program
          ''')
        print()

    # TODO: Add code to get user's choice
    def get_choice():
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    def show_current_data_from_file(list_of_objects):
        print("******* The current data: *******")
        for row in list_of_objects:
            print(' '+str(row[0]) +','+ str(row[1])+'\n')
        print("*******************************************")
        print()

    # TODO: Add code to get product data from user
    def get_product_data ():
        try:
            global productname
            productname = str(input("What is the product's name? "))# Get product name from user
            global productprice
            productprice = float(input("What is the product's standard price? ")) # Get product's standard price from user
            lstRow = [productname, productprice]
            print()
            return productname
            return productprice
        except Exception as e:
            print("There was an error! Double check the format of your input.")
            print(e,e.__doc__,type(e),sep='\n')

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_to_file(strFileName, list_of_product_objects)

# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
while(True):
    IO.show_menu()
    strChoice = IO.get_choice()

    # Main Body of Script  ---------------------------------------------------- #
    if (strChoice == '1'):
        IO.show_current_data_from_file(list_of_product_objects) # Show current data in the list/table
        continue

    elif(strChoice == '2'):
        IO.add_docstring(Product)
        IO.get_product_data()
        Product.AddData(list_of_product_objects)
        continue

    elif (strChoice == '3'):
         IO.add_docstring(FileProcessor)
         FileProcessor.save_data_from_file(strFileName,list_of_product_objects)
         break