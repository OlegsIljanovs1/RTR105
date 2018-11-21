import sys
sys.path.append( '/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace

def f(x):
    return sin(x)

x = linspace( 0, 7, 71)
y = f(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt. ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x, y, color= "#FF0000")
plt.legend (['$sin(x)$'])
plt.show()

delta_x = x[1] - x[0]

y_first_derivative = ( f(x+delta_x) - f(x) ) / delta_x
plt.plot(x, y_first_derivative, color = "#00F00")

plt.legend(['$sin(x)$','$sin\'(x)$'])
plt.show ()
N = len(x)

y_first_derivative_build_from_array =[]
for i in range(5):
    temp = ( y[i+1] - y[i]) / (delta_x)
    #temp = ( y[i+1] - y[i] ) / ( x[i+1] - x[i] )
    y_first_derivate_build_from_array.appent(temp)
    print(i,x[i],x[i+1],y[i],y[i+1],temp,y_first_derivate_build_from_array)
    
