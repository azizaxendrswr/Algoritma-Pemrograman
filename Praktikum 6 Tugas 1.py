# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:33:48 2021

@author: Aziza Ananta
"""

nilai = [4.00 , 3.75 , 3.50 , 3.00 , 2.75 , 2.50 , 2.00 , 1.75 , 1.50 , 1.25]

def scoredata(x):
    
    if x == 'A':
        score = float(nilai[0])
    elif x == 'A-':
        score = float(nilai[1])
    elif x == 'B+':
        score = float(nilai[2])
    elif x == 'B':
        score = float(nilai[3])
    elif x == 'B-':
        score = float(nilai[4])
    elif x == 'C+':
        score = float(nilai[5])
    elif x == 'C':
        score = float(nilai[6])
    elif x == 'C-':
        score = float(nilai[7])
    elif x == 'D':
        score = float(nilai[8])
    elif x == 'E':
        score = float(nilai[9])
    else:
        print('INVALID!')
        score = 0
    return score
        
def average(data):
    total = sum(data)
    ratarata = float(total / len(data))
    return ratarata

def inputdata():
        varnilai = str.upper(input('"x" to stop!\nEnter student score : '))
        return varnilai
    
def result():    
    print(('''
          
          
          Student Score :
          {0}
          
          Number of Student : 
          {1}
          
          Total score : 
          {2}
          
          Average Score = 
          {3}
          
          
          ''').format(datanilai,len(datanilai),sum(datanilai),average(datanilai)))
    
datanilai = []
# User Interface
ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    nilaivar = inputdata()
    s = scoredata(nilaivar)
    if nilaivar == 'X':
        ulang = 1
    elif s == 0:
        print()
    else:
        print(('{0} Student = {1}').format(nomor,s))
        datanilai.append(s)
          
result()