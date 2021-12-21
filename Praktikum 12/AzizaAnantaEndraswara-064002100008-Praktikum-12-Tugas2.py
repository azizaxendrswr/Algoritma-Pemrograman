print("=================================================")
print("Programs Create Mean Data and Standard Deviations")
print("=================================================")

title = str(input("Enter the title of file : "))
filename = (f"{title}.csv")
f = open(filename, "w")
f.close()

print(f"{filename} file has been created!")
print("Press 'S' to stop the program!")

file = open('Negara.csv','r')

class my_dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

data = my_dictionary()
a1 = []
b2 = []
c3 = []
d4 = []
e5 = []

x = 0
for cache in file:
    x += 1
    cache = cache.split(',')
    if x == 1:
        pass
    else:
        p1 = cache[0]
        a1.append(p1)
        p2 = cache[1]
        b2.append(p2)
        p3 = cache[2]
        c3.append(p3)
        p4 = int(cache[3])
        d4.append(p4)
        p5 = int(cache[4])
        e5.append(p5)

data.add('Country',a1)
data.add('Capital city',b2)
data.add('Continent',c3)
data.add('Extensive',d4)
data.add('Population',e5)

import pandas as DATAFILE

def write(string):
    file = open(f"{title}.csv","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{title}.csv", "r")
    teks = file.read()
    print(teks)

xy = True
while xy == True:
    result = DATAFILE.DataFrame(data)
    print('\nThe vast and population of countries in the world\n\n',result)
    print("Enter 1 to find the mean data")
    print("Enter -1 to find the standard deviation")
    
    content = int(input("Enter your choice : "))
    mean = result.groupby(['Continent']).mean()
    std = result.groupby(['Continent']).std()
    if content == 0:
        print("\nThe text has been saved!")
        X = False
    elif content == 1:
        print('\nData average : \n',mean)
        write(mean)
        read()
    elif content == -1:
        print('\nStandard Deviation : \n',std)
        write(std)
        read()
