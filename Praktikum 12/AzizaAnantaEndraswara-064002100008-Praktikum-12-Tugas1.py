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

import pandas as hey

result = hey.DataFrame(data)
print('\nVast data and population countries in the world\n\n',result)

mean = result.groupby(['Continent']).mean()
std = result.groupby(['Continent']).std()

print('\nThe average from the above data : \n',mean)
print('\nStandard deviation of the above data : \n',std)
input('\nThis program created by Aziza Ananta Endraswara!\nThank you for using my program. See you next time. Press Enter!')
