>>> import sys
>>> sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages'°
  File "<stdin>", line 1
    sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages'°
                                                                      ^
SyntaxError: invalid character in identifier
>>> sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
>>> from numpy import *
>>> x = linspace ( 0, 4, 70)
>>> y = cos(x)
>>> from matplotlib import pyplot as plt
plt.grid(0>>> 
>>> plt.grid()
>>> plt.xlabel('x')
Text(0.5,0,'x')
>>> plt.ylabel('f(x)')
Text(0,0.5,'f(x)')
>>> plt.title('Funkcija$cos(x)$')
Text(0.5,1,'Funkcija$cos(x)$')
>>> plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x7f0628168128>]
>>> plt.show()
