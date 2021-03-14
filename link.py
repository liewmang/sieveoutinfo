# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:46:10 2021

@author: steph
"""


from siever import sievelink

file_input = input("Enter file path: ")
file_output = input("Name of result file: " )+".xlsx"

sievelink(file_input, file_output)