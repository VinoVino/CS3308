#!/usr/bin/env python3
# James Covino, 29July2018
import sqlite3


class database:

    def __init__(self):
        self.table_names = ['Store', 'Store_Product', 'Product', 'Category']

    def create(self, dbname):
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()

        #create Store
        cursor.execute("create table Store(idStore int, SquareFeet int, StoreType varchar, LocationType varchar, Address varchar," +
            " City varchar, StoreState varchar, ZipCode varchar);")

        #create Store_Product
        cursor.execute("create table Store_Product(ProductID int, StoreID int, Quantity int);")

        #create Product
        cursor.execute("create table Product(idProduct int, Name varchar, Price decimal, CategoryID int, Description varchar);")

        #create Category
        cursor.execute("create table Category(idCategory int, Name varchar, Description varchar );")
        conn.commit()
        conn.close()

    def fill(self, dbname):
         conn = sqlite3.connect(dbname)
         cursor = conn.cursor()

         #Insert a few categories into the table Category.
         #(idCategory int, Name varchar, Description varchar)
         cursor.execute("insert into Category values(1, 'Dairy', 'products that are made from Dairy');")
         cursor.execute("insert into Category values(2, 'Automotive', 'products for automobiles');")
         cursor.execute("insert into Category values(3, 'Deli', 'products from the deli');")

         #Insert a few stores into the table Store.
         #(idStore int, SquareFeet int, StoreType varchar, LocationType varchar, Address varchar City varchar, StoreState varchar, ZipCode varchar)
         cursor.execute("insert into Store values(1, 10000, 'convenient store', 'Town', '99 Cliffside road', 'Boulder', 'Utah', 84716);")
         cursor.execute("insert into Store values(2, 600, 'convenient store', 'Town', '33 Tamichi Creek road', 'White Pine', 'Colorado', 81230);")
         cursor.execute("insert into Store values(3, 1000, 'convenient store', 'Town', '357 Apple Valley road', 'Lyons', 'Colorado', 80540);")

         #Insert into Product. Use an insert with a select sub-query on Category to get the correct rowid.
         #(idProduct int, Name varchar, Price decimal, CategoryID int, Description varchar);")
         cursor.execute("insert into Product values(1, 'Whole milk', 4.50, (select rowid from Category where Name = 'Dairy'), 'cows unadulterated milk');")
         cursor.execute("insert into Product values(2, 'Motor oil', 6.50, (select rowid from Category where Name = 'Automotive'), 'car engine oil 0W-20');")
         cursor.execute("insert into Product values(3, 'Genoa salami', 9.50, (select rowid from Category where Name = 'Deli'), 'Genoa Salami made from veal');")

         #Insert into Store_Product. Take care to ensure that ProductID and StoreID correctly match the rowids of their respective tables.
         #You can insert whatever values you like as long as they make sense and match the database schema.
         #(ProductID int, StoreID int, Quantity int)
         #store 1 Boulder Utah
         cursor.execute("insert into Store_Product values(1, 1, 5); ")
         cursor.execute("insert into Store_Product values(2, 1, 1); ")
         cursor.execute("insert into Store_Product values(3, 1, 2); ")

         #store 2 White Pine Colorado
         cursor.execute("insert into Store_Product values(1, 2, 0); ")
         cursor.execute("insert into Store_Product values(2, 2, 0); ")
         cursor.execute("insert into Store_Product values(3, 2, 0); ")

         #store 3 Lyons Colorado
         cursor.execute("insert into Store_Product values(1, 3, 10);")
         cursor.execute("insert into Store_Product values(2, 3, 5);" )
         cursor.execute("insert into Store_Product values(3, 3, 10);")

         conn.commit()
         conn.close()

    def add_product(self, dbname, id_product=99, name="test", price=1.0, categoryID="1", description='blah'):
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        #(2, 'Motor oil', 6.50, (select rowid from Category where Name = 'Automotive'), 'car engine oil 0W-20');")

        #Id = cursor.execute("select rowid from Category where idCategory=?", categoryID)
        Id ="(select rowid from Category where idCategory = " + categoryID +")"
        params = (id_product, name, price, Id, description)

        cursor.execute("insert into Product values (?, ?, ?, ?, ?)", params)
        #c.execute("INSERT INTO People VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)

        conn.commit()
        conn.close()
        return [name, price, categoryID, description]

    def remove_product(self, dbname, name="test"):
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("Delete from Product where name = ?", (name,))
        conn.commit()
        conn.close()

