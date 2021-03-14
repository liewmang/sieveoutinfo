# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:34:37 2021

@author: steph
"""


from siever import sievename

file_input = input("Enter file path: ")
file_output = input("Name of result file: " )+".xlsx"

sievename(file_input, file_output)