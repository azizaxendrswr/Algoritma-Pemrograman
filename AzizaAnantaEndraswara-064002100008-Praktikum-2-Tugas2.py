# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 19:11:08 2021

@author: Aziza Ananta
NAMA : AZIZA ANANTA ENDRASWARA
NIM : 064002100008
"""

from math import sin, cos, atan2, radians, sqrt, ceil

print("----------------------------------------")
print("Latitude/Longitude Distance Calculator")
print("----------------------------------------")
lat1 = int(input("Latitude 1 = "))
lat2 = int(input("Latitude 2 = "))
lon1 = int(input("Longitude 1 = "))
lon2 = int(input("Longitude 2 = "))
print("\n")
R = 6371
lat1, lat2, lon1, lon2 = map(radians, [lat1, lat2, lon1, lon2])
dlat = lat2 - lat1
dlon = lon2 - lon1
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
d = c * R

print("---------------------------------")
print(f"distance = {ceil(d)} km")
print("hasil pada jarak sudah dibulatkan")
print("---------------------------------")
