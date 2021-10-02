from matplotlib.cm import ScalarMappable
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np

'''
def printName(firstName, lastName):
    # definition of the parameters and computations.

    print('the first name is :', firstName)
    print('The last name is :', lastName)
    return
'''
'''
printName('ali', 'reza')

x = np.linspace(-5, +5, 100)
y = x*x
z = x*x*x
plt.plot(x, y)
plt.plot(x,z)
plt.title('kossher')
plt.grid()
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
'''
'''
def f(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return 1/x
fx_name = r'$f(x)=\frac{1}{x}$'

x=np.linspace(-10,10,101)
y=f(x)
plt.plot(x, y, label=fx_name)
plt.legend(loc='upper left')
plt.show()

'''
'''
dx = 1 
x = np.arange(0,6.1,dx)
print(x)

'''
'''

def sumCalculatuion(array):

    sum = 0 
    for member in array:
        sum = member + sum 
    return sum

arr = [2,5,55,2,33]
sample = sumCalculatuion(arr)
print(sample)

'''
'''

car = {
    "brand" : 'Ford',
    'model': 'Mustang',
    'year' : 2012,
}
car['year'] = 1995
print (car['year'])
values = car.values()
keys = car.keys()
print (keys)
car['color'] = 'red'
print (car['color'])
items = car.items()
print (items)

'''
car = {
    "year" : 1964,
    'model': 'Mustang',
    'brand': 'Ford',
    'address': {
        'name':'Ali',
        "city":'Milan'
    }
}

'''
car.update({ 'brand' : 'BMW' })
print(car)
car['brand'] = 'Benz'
print(car)
car.pop('model')
print(car)
for i,j in car.items():
    print(i,j)

'''

automobile = car.copy()
automobile['address'] = {'name':'reza','city':'karaj'}
print(automobile)
print(car)
