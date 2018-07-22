#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# James Covino, Lab 9 21,22 July2018

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    def test_constructor(self):
        # verify the constructor raises an error if not passed a string
        test_input = [9, True]
        for test in test_input:
            test_result = False
            try:
                textproc.Processor(test)
            except textproc.TextProcError:
                test_result = True    
            self.assertEqual(True, test_result, "constructor input error- taking in: " + str(test))
       
    def test_count(self):
        # verify the functionality of count()
         test_texts = ['1234', 'phi phi pho phum', 'the cake is a lie', '99 red balloons']
         for text in test_texts:
            p = textproc.Processor(text)
            self.assertEqual(p.count(), len(text), "length is off: " + text)    
     
    def test_count_alpha(self):
        # verify the functionality of count_alpha() 
        test_texts = ['abcde','abcde9', '9999!23*&A', 'ABC', '239831*&71 , !%' ] 
        test_solutions =[ 5, 5, 1, 3, 0]
        for index in range(len(test_texts)):
            p = textproc.Processor(test_texts[index])
            self.assertEqual(p.count_alpha(), test_solutions[index], "alphabetic characters count is off: " + 
                str(test_texts[index]))
        # error found in function: doesn't count uppercase letters - Fixed
            
    def test_count_numeric(self):        
        # verify the functionality of count_numeric()
        test_texts = ['abcde','abcde9', '9999!23*&A', 'ABC', '239831*&71 , !%', '000' ] 
        test_solutions =[ 0, 1, 6, 0, 8, 3]
        for index in range(len(test_texts)):
            p = textproc.Processor(test_texts[index])
            self.assertEqual(p.count_numeric(), test_solutions[index], "numeric characters count is off: " + 
                str(test_texts[index])) 
         # error found in function: doesn't include 0 as number - Fixed

    def test_count_vowels(self):        
        # verify the functionality of the count_vowels()
        test_texts = ['abcde','abcde9', '9999!23*&A', 'ABC', '239831*&71 , !%', 'aeiou', 'BCDFGHJKLMNPQRSTVWXYZ' ] 
        test_solutions =[ 2, 2, 1, 1, 0, 5, 0]
        for index in range(len(test_texts)):
            p = textproc.Processor(test_texts[index])
            self.assertEqual(p.count_vowels(), test_solutions[index], "count of vowels is off: " + 
                str(test_texts[index]))         

        # error found in function: **i** missing vowel in function - Fixed

    def test_is_phonenumber(self):
        #verify the functionality of is_phonenumber()
        test_texts = ['303-333-3333','(333)-333-3333','303-3333333', '303333-3333', 'abc-ab-abcd', 
        '99-9999-9999', '333-(33)3-3333'] 
        test_solutions =[ True, True, False, False, False, 
        False, False]
        for index in range(len(test_texts)):
            p = textproc.Processor(test_texts[index])
            self.assertEqual(p.is_phonenumber(), test_solutions[index], "phone number verificaiton is off: " + 
                str(test_texts[index]) + str( (p.is_phonenumber()))  )

        # error found in function. Incorrect Regex - Fixed




# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
