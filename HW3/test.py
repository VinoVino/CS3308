#!/usr/bin/env python3
# James Covino, HW 3 29 July2018

import unittest
import storedb
import os
import sqlite3


def db_setUp():
    # Implement a setUp method that creates a new sqlite3 database file test.db and runs both functions.
    database = storedb.database()

    database.create('test.db')
    database.fill('test.db')


def db_tearDown():
    # Implement a tearDown method that deletes the test.db
    os.remove('test.db')


class TextprocTestCase(unittest.TestCase):

    #Each test should run a SELECT statement on the table, and assert that the results are what you expect them to be.
    def test_category(self):
        #(idCategory int, Name varchar, Description varchar)
         category_dict = {1: 'Dairy', 2: 'Automotive', 3: 'Deli'}
         conn = sqlite3.connect('test.db')
         cursor = conn.cursor()
         #Category_Table
         Category = cursor.execute("select * from Category;")
         # (1, 'Dairy', 'products that are made from Dairy')

         for row in Category:
            id_cat = row[0]
            self.assertEqual(row[1], category_dict[id_cat], "ID and Name don't match")

         conn.close()

    def test_store(self):
        #(idStore int, SquareFeet int, StoreType varchar, LocationType varchar, Address varchar City varchar, StoreState varchar, ZipCode varchar)
         store_dict = {1: '99 Cliffside road', 2: '33 Tamichi Creek road', 3: '357 Apple Valley road'}
         conn = sqlite3.connect('test.db')
         cursor = conn.cursor()
         store = cursor.execute("select * from Store;")

         # (1, 10000, 'convenient store', 'Town', '99 Cliffside road', 'Boulder', 'Utah', '84716')
         for row in store:
            id_store = row[0]
            self.assertEqual(row[4], store_dict[id_store], "Store ID and address don't match")

         conn.close()

    def test_product(self):
        #(IdProduct int, Name varchar, Price decimal, CategoryID int, Description varchar)
         product_dict_name = {1: 'Whole milk', 2: 'Motor oil', 3:'Genoa salami', 99:'test'}
         product_dict_price = {1: 4.5, 2: 6.5, 3: 9.5, 99: 1.0}

         conn = sqlite3.connect('test.db')
         cursor = conn.cursor()

         product = cursor.execute("select * from Product;")
         # (1, 'whole milk', 4.5, 1, 'cows unadulterated milk')
         for row in product:
            idproduct = row[0]
            #name check
            self.assertEqual(row[1], product_dict_name[idproduct], "Product ID and Name are wrong")
            #price check
            self.assertEqual(row[2], product_dict_price[idproduct], "Product ID and price are wrong")

         conn.close()

    def test_store_product(self):
        #(ProductID int, StoreID int, Quantity int)
         conn = sqlite3.connect('test.db')
         cursor = conn.cursor()
         store_product = cursor.execute("select * from Store_Product;")
          #  (3, 3, 10)
          # assert that each value is and int

         for row in store_product:
            for item in row:
                is_integer = isinstance(item, int)
                self.assertEqual(True, is_integer, "Values in table aren't integers")
         conn.close()

    def test_add_product(self):
        # (IdProduct int, Name varchar, Price decimal, CategoryID int, Description varchar)
        database = storedb.database()
        product_list = database.add_product('test.db')
        #[name, price, categoryID, description]

        # addProduct should raise a ValueError if name or description are empty or not strings.
        name_is_string = isinstance(product_list[0], str)
        self.assertEqual(True, name_is_string, "name is not string!")

        # addProduct should raise a ValueError if price is less than 0 or not a number.
        price_is_float = isinstance(product_list[1], float)
        if product_list[1] < 0:
            price_is_float = False
        self.assertEqual(True, price_is_float, "price is not a number or less than 0!")

        # addProduct should raise a ValueError if categoryID is not a valid rowid in the category table.
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        category_rowid = cursor.execute('select rowid from Category;')

        # addProduct should raise a ValueError if categoryID is not a valid rowid in the category table.
        categoryID = product_list[2]
        valid_rowid = False
        for row in category_rowid:
            rowid = row[0]  #1, 2, 3 ....
            if int(rowid) == int(categoryID):
                valid_rowid = True
                break
        self.assertEqual(True, valid_rowid, "categoryID is not a valid rowid!")

        conn.commit()
        conn.close()

    def test_remove_product(self):
        database = storedb.database()
        product_list = database.remove_product('test.db')

        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        store_product = cursor.execute("select * from Product;")

        removed = True
        for row in store_product:
            #(3, 'Genoa salami', 9.5, 3, 'Genoa Salami made from veal')
            if row[1] == "test":
                removed = False
                break
        self.assertEqual(True, removed, "product not removed!")


        conn.commit()
        conn.close()

# Main: Run Test Cases
if __name__ == '__main__':

    db_setUp()
    unittest.main()
