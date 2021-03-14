# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:41:11 2021

@author: steph
"""


from siever import sievecomments

file_input = input("Enter file path: ")
file_output = input("Name of result file: " )+".xlsx"

sievecomments(file_input, file_output)

