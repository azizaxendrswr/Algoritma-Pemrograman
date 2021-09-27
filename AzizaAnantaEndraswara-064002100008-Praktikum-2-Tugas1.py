# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:03:39 2021

@author: Aziza Ananta
"""

import math


a = float(input("masukkan nilai a : "))
b = float(input("masukkan nilai b : "))

hasil = a + b
print("a ditambah b :", hasil)

hasil = a - b
print("selisih a dan b :", abs(hasil))

hasil = a * b
print("a dikali b :", hasil)

hasil = a % b
print("sisa pembagian a dan b :", hasil)

hasil = a / b
print("pembagian a dan b :", hasil)

hasil = math.log10(a)
print("log(a) :", hasil)

hasil = a ** b
print("a pangkat b :", hasil)
