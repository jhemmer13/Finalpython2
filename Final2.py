import sqlite3
import csv
from contextlib import closing
#create product class
class Product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity


    #has price, id and quantity

class book(Product):
    BOOK = ""
    def __init__(self, name, price, id, quantity, author):
        super().__init__(price, id, quantity)
        self.author = author
        self.name = name


    def print_info(self):
        name = self.name.ljust(25, " ")
        factor1 = int(self.quantity)
        factor2 = float(self.price)
        total = factor1 * factor2
        total = round(total, 2)
        total = str(total)
        total = "$" + total
        total = total.ljust(5, " ")
        price = str(self.price)
        price = "$" + price
        price = price.ljust(25, " ")
        quantity = str(self.quantity)
        quantity = quantity.ljust(25, " ")


        return f"{self.id} {name} {price} {quantity} {total}"

class movie(Product):
    MOVIE = ""
    def __init__(self, id, name, genre, year, price, quantity):
        super().__init__(price, id, quantity)
        self.__name = name
        self.__genre = genre
        self.__year = year

    def get_total(self):
        factor1 = int(self.quantity)
        factor2 = float(self.price)
        total = factor1 * factor2
        return total

    def print_info(self):
        name = self.__name.ljust(25, " ")
        factor1 = int(self.quantity)
        factor2 = float(self.price)
        total = factor1 * factor2
        total = round(total, 2)
        total = str(total)
        total = "$" + total
        total = total.ljust(5, " ")
        price = str(self.price)
        price = "$" + price
        price = price.ljust(25, " ")
        quantity = str(self.quantity)
        quantity = quantity.ljust(25, " ")


        return f"{self.id} {name} {price} {quantity} {total}"

#2 child classes of Product class:
    #book class with author info and class attribute of "BOOK"

def initialize_csv(filename):
    with open(filename, "r") as data_file:
        csv_data = csv.reader(data_file)
        print(topmenu())

        for item in csv_data:
            if (item[0] == "BOOK"):

                id = item[1]
                name = item[2]
                author = item[3]
                price = item[4]
                quantity = item[5]

                newbook = book(name, price, id, quantity, author)
                print(newbook.print_info())
            elif (item[0] == "MOVIE"):
                id = item[1]
                name = item[2]
                genre = item[3]
                year = item[4]
                price = item[5]
                quantity = item[6]
                newmovie = movie(id, name, genre, year, price, quantity)
                print(newmovie.print_info())
            else:
                print("Something went wrong")

def topmenu():
    product = "PRODUCT"
    name = "NAME"
    name.ljust(25, " ")
    price = "PRICE"
    price = price.rjust(25, " ")
    quantity = "QTY"
    quantity = quantity.rjust(23, " ")
    total = "TOTAL"
    total = total.rjust(27, " ")
    return f" {product}  {name} {price} {quantity} {total}"

def add_movie(filename):
    #Asks for movie attributes
    #writes to the csv file

    id = int(input("What is the id? "))
    if id >= 0 and id <10:
        id = str(id)
        id = "PROD00" + id
    elif id >=10 and id <100:
        id = str(id)
        id = "PROD0" + id
    else:
        id = str(id)
        id = "PROD" + id
    name = input("What is the name? ")
    genre = input("What is the genre? ")
    release_date = int(input("What is the release date? "))
    price = float(input("What is the price? $"))
    # price = price.replace("?", "")
    quantity = int(input("What is the quantity? "))
    addrow = ("MOVIE", id, name, genre, release_date, price, quantity)
    with open(filename, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(addrow)
        file.close()
    #with open(csv, mode='w') as movie_file:

        #movie_writer = csv.writer(movie_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #movie_writer.writerow(["MOVIE", id, name, genre, release_date, price, quantity])


def add_book(filename):
    #asks for book attributes
    #writes to the csv file
    id = int(input("What is the id? "))
    if id >= 0 and id <10:
        id = str(id)
        id = "PROD00" + id
    elif id >=10 and id <100:
        id = str(id)
        id = "PROD0" + id
    else:
        id = str(id)
        id = "PROD" + id
    name = input("What is the name? ")
    author = input("Who is the author? ")
    price = float(input("What is the price? $"))
    quantity = int(input("What is the quantity? "))
    addrow = ("BOOK", id, name, author, price, quantity)
    with open(filename, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(addrow)
        file.close()


def total(filename):
    with open(filename, "r") as data_file:
        csv_data = csv.reader(data_file)
        total = float()
        for row in csv_data:
            if (row[0] == "MOVIE"):

                product1 = float(row[5])
                product2 = int(row[6])
                product3 = product1 * product2
                total += product3
            elif (row[0] == "BOOK"):
                product1 = float(row[4])
                product2 = int(row[5])
                product3 = product1 * product2
                total += product3
    print("-" * 95)
    print("TOTAL", end = '')
    total = round(total, 2)
    total = str(total)
    total = "$" + total
    total = total.rjust(91, " ")
    print(total)


continues = True
while continues is True:
    #starting menu
    print("""
    PRODUCT INVENTORY PROGRAM
    1. Show all products
    2. Add a product
    3. Exit""")
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
    except ValueError:
        pass
    if choice == 1:
        initialize_csv("productlist.csv")
        total("productlist.csv")
        # for item in inventory:
        #     print("PROD", end = '')
        #     print(item)
    elif choice == 2:
        while True:
            choice2 = input("""Would you like to add a book or movie (enter a letter to esc)?
            1. Movie
            2. Book
            """)
            try:
                choice2 = int(choice2)
            except ValueError:
                break
            if choice2 == 1:
                add_movie("productlist.csv")
                initialize_csv("productlist.csv")
                total("productlist.csv")
                break
            elif choice2 ==2:
                add_book("productlist.csv")
                initialize_csv("productlist.csv")
                total("productlist.csv")
                break
            else:
                print("Please enter a valid number")

    elif choice == 3:
        print("Bye")
        continues = False