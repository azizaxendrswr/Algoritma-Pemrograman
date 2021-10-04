# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:15:21 2021

@author: Aziza Ananta
NAMA : AZIZA ANANTA ENDRASWARA
NIM  : 064002100008
"""

print("-------------------------------")
print("   Menentukan jenis segitiga")
print("-------------------------------")

a = int(input("Sisi A : "))
b = int(input("Sisi B : "))
c = int(input("Sisi C : "))

if (a + b <= c) or (a + c <= b) or (b + c <= a) :
    print("-> Bukan Segitiga")
elif a == b == c :
    print("-> Segitiga Sama Sisi")
elif (a == b) or (a == c) or (b == c) :
    print("-> Segitiga Sama Kaki")
elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a) :
    print("-> Segitiga Siku-siku")
else :
    print("-> Segitiga Sembarang")
